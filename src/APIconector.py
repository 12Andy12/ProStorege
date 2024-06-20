import requests
import json
import uuid
from datetime import datetime
import src.resources_db

api_key = "Application RPbBHeffsEkBdjAXHVWjgN4ie4NMPLqAtOILJzIP05OlMeCZdp1lDdtTV7M5hFG1"
headers = {"x-client-key": api_key}

all_goods = {}


def create_order(positions):
    for pos in positions:
        pos["PaymentMethodType"] = 4 # Полный рассчет
        pos["text"] = pos["name"]

    params = {
        "id": generate_id(),
        "number": get_new_order_number(),
        "dateTime": time_now(),
        'device': 322881,
        "content":{
            "positions": positions,
        },
    }
    response = requests.post("https://api.aqsi.ru/pub/v2/Orders/simple", headers=headers, json=params)



def get_all_orders():
    params = {
        "filtered.dateFrom": "2024-04-01T12:00",
    }
    res = requests.get("https://api.aqsi.ru/pub/v2/Orders", headers=headers, params=params)



def get_directories():
    res = requests.get("https://api.aqsi.ru/pub/v2/GoodsCategory/list", headers=headers)

    return res.json()


# def get_goods_from_dir(dir_name):
#     folder_id = requests.get("https://api.aqsi.ru/pub/v2/GoodsCategory/list", headers=headers, params={"name": dir_name}).json()[0]["id"]
#     print(f"folder_id = {folder_id}, where current_dir_name = {dir_name}")
#     return requests.get("https://api.aqsi.ru/pub/v2/Goods/list", headers=headers).json()


def get_all_goods():
    for i in range(5):
        print(f"try get with page number = {i}")
        result = requests.get("https://api.aqsi.ru/pub/v2/Goods/list", headers=headers,
                              params={
                                  # "group_id": dir_id,
                                  "pageNumber": i,
                              })
        print(f"try get with page number = {i}, result = {result}")
        for row in result.json()["rows"]:
            all_goods[row["id"]] = row
    return all_goods


def del_good(del_id):
    response = requests.delete(f"https://api.aqsi.ru/pub/v2/Goods/{del_id}", headers=headers)



def get_goods_from_dir_id(dir_id):

    result = requests.get("https://api.aqsi.ru/pub/v2/Goods/list", headers=headers,
                          params={
                              "group_id": dir_id,
                              # "pageNumber": 0,
                          })
    return result.json()


def add_good(new_id, name, original_price, price, type, current_folder_id):
    params = {
        "id": new_id,
        "name": name,
        "group_id": current_folder_id,
        "price": price,
        "type": "simple",
        "productionCost": original_price,
        "isWeight": 1,  # Весовой ли товар 0-Штучный 1-Весовой
        "subject": 1,  # 1 == Товар
        "tax": 6,  # НДС не облагается
        "unit": type,  # Ед измерения???
        "paymentMethodType": 4  # Полный расчёт
    }
    response = requests.post("https://api.aqsi.ru/pub/v2/Goods", headers=headers, json=params)



def update_dir(folder):
    response = requests.put("https://api.aqsi.ru/pub/v2/GoodsCategory", headers=headers, json=folder)



def update_good(item):
    response = requests.put("https://api.aqsi.ru/pub/v2/Goods", headers=headers, json=item)



def add_folder(new_id, new_dir_name, parent_id):
    params = {
        "id": new_id,
        "name": new_dir_name,
        "parent": parent_id,
        "defaultSubject": 1,  # 1 == Товар
        "defaultTax": 6,  # НДС не облагается
        "defaultUnit": "Штука",  # Ед измерения категории ???
        "defaultUnitCode": 0,  # 0 - Штука или Единица
        "defaultPaymentMethodType": 4  # Полный расчёт
    }

    response = requests.post("https://api.aqsi.ru/pub/v2/GoodsCategory", headers=headers, json=params)



def del_folder(delete_dir):
    response = requests.delete(f"https://api.aqsi.ru/pub/v2/GoodsCategory/{delete_dir['id']}", headers=headers)



def generate_id():
    new_id = uuid.uuid4()
    return str(new_id)


def get_new_order_number():
    new_number = 0
    path = "DataBase/order_number.txt"
    with open(path, "r") as file:
        number = file.readline()
        new_number = int(number) + 1
    with open(path, "w") as file:
        file.write(str(new_number))

    return f"PS-{new_number}"


def time_now():
    return f"{datetime.now().year}-{datetime.now().month:02}-{datetime.now().day:02}T{datetime.now().hour:02}:{datetime.now().minute:02}:{datetime.now().second:02}"
