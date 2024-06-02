# import psycopg2
import sqlite3


# host = "127.0.0.1"
# user = "postgres"
# password = "adminadmin"
#
# db_name = "ProStorageDB"

# connection = sqlite3.connect("ItemDataBase.db")
#         cur = connection.cursor()
#
#         for row in cur.execute("SELECT * FROM FolderControl WHERE parentName = ?", (self.currentFolder,)):
#             self.folders.append(row[0])
#
#         for row in cur.execute("SELECT * FROM ItemControl WHERE folder = ?", (self.currentFolder,)):
#             thisData = []
#             for i in range(6):
#                 thisData.append(row[i])
#             self.data.append(thisData)


class DataBaseConnector:
    def __init__(self):
        super().__init__()
        self.connection = None
        self.cursor = None
        try:
            self.connection = sqlite3.connect("DataBase/ProDataBase.db")
            self.cursor = self.connection.cursor()
            print("[INFO] SQL connection successful")
        except Exception as _ex:
            print("[ERROR] Error while working with SQL: ", _ex)

        self.init_tables()

    def init_tables(self):
        try:
            self.cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS folders(
                        id text PRIMARY KEY,
                        name,
                        parent_name text,
                        UNIQUE(id));
                    """
                    )
            self.cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS items(
                        id text PRIMARY KEY,
                        name text,
                        price double precision,
                        original_price double precision,
                        count double precision,
                        type double precision,
                        folder text REFERENCES folders (name));
                    """
                    )
            self.cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS tags(
                        id INTEGER REFERENCES items (id),
                        tags text);
                    """
                    )
            self.connection.commit()
            print("[INFO] SQL initialization tables successful")
        except Exception as _ex:
            print("[ERROR] Error while working with SQL: ", _ex)

    def request(self, command):
        result = None
        try:
            self.cursor.execute(command)
            result = self.cursor.fetchall()
            self.connection.commit()
            print(f"[INFO] SQL request [{command}] successful, result = {result}")
        except Exception as _ex:
            print(f"[ERROR] Error while working with SQL:\nin line: {command}\nerror: {_ex}")

        return result

    def __del__(self):
        if self.connection:
            self.connection.close()
            print("[INFO] SQL connection closed")

#
#
# def request(command):
#     connection = None
#     res = []
#     try:
#
#         connection = psycopg2.connect(
#             host=host,
#             user=user,
#             password=password,
#             database=db_name
#         )
#         connection.autocommit = True
#
#         with connection.cursor() as cursor:
#             cursor.execute(command)
#             res = cursor.fetchall()
#
#     except Exception as _ex:
#         print("[INFO] Error while working with postgres SQL: ", _ex)
#     finally:
#         if connection:
#             connection.close()
#             print("[INFO] Postgres SQL connection closed")
#
#     return res
#
#
# def test_conection():
#     connection = None
#     try:
#         connection = psycopg2.connect(
#             host=host,
#             user=user,
#             password=password,
#             database=db_name
#         )
#         connection.autocommit = True
#
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 "SELECT version();"
#             )
#
#             print(f"Server version: {cursor.fetchone()}")
#
#         with connection.cursor() as cursor:
#
#
#         # with connection.cursor() as cursor:
#         #     cursor.execute(
#         #         """INSERT INTO folders(name, parent_name) VALUES('testFolder2', 'root')"""
#         #     )
#
#         # with connection.cursor() as cursor:
#         #     cursor.execute(
#         #         """SELECT * FROM folders;"""
#         #     )
#         #     print(f"SELECT * FROM folders: {cursor.fetchone()}")
#
#
#
#     except Exception as _ex:
#         print("[INFO] Error while working with postgres SQL: ", _ex)
#     finally:
#         if connection:
#             connection.close()
#             print("[INFO] Postgres SQL connection closed")
