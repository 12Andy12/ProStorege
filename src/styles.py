import pickle


CONFIG_PATH = "config.bin"

styles_config = {
    "main_background_color": str((50, 50, 50, 255)),
    "font_color": str((240, 240, 240, 255)),
    "alternative_background_color": str((60, 60, 60, 255)),
    "object_background_color": str((65, 65, 65, 255)),
    "object_hover_color": str((70, 70, 70, 255)),
    "object_press_color": str((75, 75, 75, 255)),
    "font_family": "Times New Roman",
    "font_size": "14",
    "error": str((150, 0, 0, 255)),
}


def load_config():
    global styles_config
    try:
        with open(CONFIG_PATH, "rb") as file:
            styles_config = pickle.load(file)
            # save_config()
            # pass
    except FileNotFoundError:
        save_config()
    except Exception as err:
        print(f"Exception on loading config from path = {CONFIG_PATH}. {err}")


def save_config():
    global styles_config
    try:
        with open(CONFIG_PATH, "wb") as file:
            pickle.dump(styles_config, file)
    except Exception as err:
        print(f"Exception on saving config to path = {CONFIG_PATH}. {err}")


def background_color(using_config):
    return (
        """
            color: rgba"""
        + styles_config["font_color"]
        + """;
            background: rgba"""
        + styles_config[using_config]
        + """;
            """
    )


def vertical_scroll_bar_style(using_config="main_background_color") -> str:
    vertical_scroll_bar = (
        """
            QScrollBar:vertical {
                border:none;
                background: rgba"""
        + styles_config[using_config]
        + """;
                width: 10px;
            }

            QScrollBar::handle:vertical {
                background: rgb(100, 100, 100);
                min-height: 20px;
                border-radius: 5px;
            }

            QScrollBar::add-line:vertical {
                border:none;
                background: rgba"""
        + styles_config[using_config]
        + """;
                height: 20px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }

            QScrollBar::sub-line:vertical {
                border:none;
                background: rgba"""
        + styles_config[using_config]
        + """;
                height: 20px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }

            QScrollBar::add-page:vertical {
                background: rgba"""
        + styles_config[using_config]
        + """;
            }

            QScrollBar::sub-page:vertical {
                background: rgba"""
        + styles_config[using_config]
        + """;
            }
            """
    )
    return vertical_scroll_bar


def main_style():
    return (
        """
                font: """
        + styles_config["font_size"]
        + """pt """
        + styles_config["font_family"]
        + """;
                background-color: rgba"""
        + styles_config["main_background_color"]
        + """;
                color: rgba"""
        + styles_config["font_color"]
        + """;
            """
    )


def combo_box_style():
    return (
        """
            QComboBox { 
                border:none;
                color: rgba"""
        + styles_config["font_color"]
        + """;
                background-color: rgba"""
        + styles_config["object_background_color"]
        + """;
                selection-background-color: rgba"""
        + styles_config["object_press_color"]
        + """;
                selection-color: rgba"""
        + styles_config["font_color"]
        + """;
            }
            QComboBox:hover {
                background-color: rgba"""
        + styles_config["object_hover_color"]
        + """;
            }
            QComboBox::drop-down {
                width: 0px;
                height: 0px;
                border: 0px;
            }
            QComboBox QAbstractItemView {
                color: rgba"""
        + styles_config["font_color"]
        + """;
                background-color: rgba"""
        + styles_config["alternative_background_color"]
        + """;
                padding: 10px;
                border: 2px solid rgb(55, 55, 55);
                border-radius: 5px;
                padding-left: 5px;
                padding-right: 5px;
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: rgba"""
        + styles_config["object_hover_color"]
        + """;
            }
            QComboBox QAbstractItemView::item:selected {
                background-color: rgba"""
        + styles_config["object_press_color"]
        + """;
            }
            """
    )


def date_edit_style():
    return (
        """
            QDateEdit{
                background-color: rgba"""
        + styles_config["object_background_color"]
        + """;
                color: rgba"""
        + styles_config["font_color"]
        + """;
                border: none;
            }
            QDateEdit:hover{
                background-color: rgba"""
        + styles_config["object_hover_color"]
        + """;
                border: none;
            }
            QDateEdit::drop-down {
                color: rgba"""
        + styles_config["font_color"]
        + """;
                background-color: rgba"""
        + styles_config["alternative_background_color"]
        + """;
                width: 25px; 
                border-left-width: 3px;
                border-left-color: rgb(120, 120, 120);
                border-left-style: solid;  
                background-position: center;
                background-repeat: no-reperat;
                image: url(:/iconCalendar.png);
            }
            QDateEdit QAbstractItemView {
                background-color: rgba"""
        + styles_config["object_background_color"]
        + """;
            }
            QDateEdit QAbstractItemView::item:hover {
                background-color: rgba"""
        + styles_config["object_hover_color"]
        + """;
            }
            QDateEdit QAbstractItemView::item:selected {
                background-color: rgba"""
        + styles_config["object_press_color"]
        + """;
            }
            QCalendarWidget QWidget { 
                alternate-background-color: rgba"""
        + styles_config["alternative_background_color"]
        + """;
                background-color: rgba"""
        + styles_config["alternative_background_color"]
        + """;
            }            
            /* меню выбора месяца           */
            CalendarWidget QToolButton QMenu {
                color: rgba"""
        + styles_config["font_color"]
        + """;
                background-color: rgba"""
        + styles_config["object_press_color"]
        + """;
            }
            CalendarWidget QToolButton QMenu::item {
                padding: 10px;
                background-color: rgba"""
        + styles_config["object_background_color"]
        + """;
            }
            CalendarWidget QToolButton QMenu::item:hover {
                background-color: rgba"""
        + styles_config["object_hover_color"]
        + """;
            }
            CalendarWidget QToolButton QMenu::item:selected {
                background-color: rgba"""
        + styles_config["object_press_color"]
        + """;
            }
            CalendarWidget QToolButton::menu-indicator {
                image: none;
                color: rgba"""
        + styles_config["font_color"]
        + """;
            }
            #qt_calendar_prevmonth, #qt_calendar_nextmonth {
                border: none;                     /* убрать границу */ 
                font-weight: bold;              /* шрифт полужирный */
                color: rgba"""
        + styles_config["font_color"]
        + """;
                color: rgba"""
        + styles_config["font_color"]
        + """;
                /* Удалить стандартное изображение клавиши со стрелкой. 
                   Вы также можете настроить                         */
                qproperty-icon: none;    
                background-color: rgba"""
        + styles_config["object_background_color"]
        + """;
            }
            #qt_calendar_prevmonth {
                qproperty-text: "<";         /* Изменить текст кнопки  */
                color: rgba"""
        + styles_config["font_color"]
        + """;
            }
            #qt_calendar_nextmonth {
                qproperty-text: ">";
                color: rgba"""
        + styles_config["font_color"]
        + """;
            }
            #qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {
                background-color: rgba"""
        + styles_config["object_hover_color"]
        + """;
            }
            #qt_calendar_prevmonth:pressed, #qt_calendar_nextmonth:pressed {
                background-color: rgba"""
        + styles_config["object_press_color"]
        + """;
            }
            #qt_calendar_yearbutton, #qt_calendar_monthbutton {
                color: rgba"""
        + styles_config["font_color"]
        + """;
                background-color: rgba"""
        + styles_config["object_background_color"]
        + """;
                border-radius: 30px;
                min-width: 85px;
            }
            #qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {
                background-color: rgba"""
        + styles_config["object_hover_color"]
        + """;
            }
            #qt_calendar_yearbutton:pressed, #qt_calendar_monthbutton:pressed {
                background-color: rgba"""
        + styles_config["object_press_color"]
        + """;
            }
            /* ниже календарной формы */
            #qt_calendar_calendarview {
                outline: 0px;                                 /* Удалить выделенную пунктирную рамку */
                selection-background-color: rgba"""
        + styles_config["object_press_color"]
        + """; /* Выберите цвет фона */
                color: rgba"""
        + styles_config["font_color"]
        + """;
                border-radius: 5px; 
            }
            #qt_calendar_yearedit {
                color: rgba"""
        + styles_config["font_color"]
        + """;
                background-color: rgba"""
        + styles_config["object_background_color"]
        + """;

                min-width: 70px;
            }
            #qt_calendar_yearedit::up-button { 
                color: rgba"""
        + styles_config["font_color"]
        + """;
                width: 20px;
                height: 20px;
                border-radius: 10px;
                background-color: rgba"""
        + styles_config["object_background_color"]
        + """;
                subcontrol-position: right;
                image: url(:/iconUp.png);      
            }
            #qt_calendar_yearedit::up-button:hover { 
                background-color: rgba"""
        + styles_config["object_hover_color"]
        + """;
            }
            #qt_calendar_yearedit::up-button:selected { 
                background-color: rgba"""
        + styles_config["object_press_color"]
        + """;
            }
            #qt_calendar_yearedit::down-button { 
                color: rgba"""
        + styles_config["font_color"]
        + """;
                width: 20px;
                height: 20px;
                border-radius: 10px;
                background-color: rgba"""
        + styles_config["object_background_color"]
        + """;
                subcontrol-position: left;  
                image: url(:/iconDown.png);     
            }
            #qt_calendar_yearedit::down-button:hover { 
                background-color: rgba"""
        + styles_config["object_hover_color"]
        + """;
            }
            #qt_calendar_yearedit::down-button:selected { 
                background-color: rgba"""
        + styles_config["object_press_color"]
        + """;
            }
            """
    )


def spin_box_style(height="30", background_color="rgb(65, 65, 65)"):
    return (
        """
            QDoubleSpinBox {
                padding-right: 15px; /* make room for the arrows */
                background-color: rgba"""
        + styles_config["object_background_color"]
        + """;
            }
            QDoubleSpinBox::up-button {
                subcontrol-origin: border;
                subcontrol-position: right; /* position at the top right corner */

                width: 25px;
                height: """
        + height
        + """;
                image: url(:/iconPlus.png) 1;
            }

            QDoubleSpinBox::up-button:hover {
                background-color: rgba"""
        + styles_config["object_hover_color"]
        + """;
            }

            QDoubleSpinBox::up-button:pressed {
                background-color: rgba"""
        + styles_config["object_press_color"]
        + """;
            }

            QDoubleSpinBox::down-button {
                subcontrol-origin: border;
                subcontrol-position: left; /* position at the bot right corner */

                width: 25px;
                height: """
        + height
        + """;
                image: url(:/iconMinus.png) 1;
            }

            QDoubleSpinBox::down-button:hover {
                background-color: rgba"""
        + styles_config["object_hover_color"]
        + """;
            }

            QDoubleSpinBox::down-button:pressed {
                background-color: rgba"""
        + styles_config["object_press_color"]
        + """;
            }
            """
    )


def table_style():
    return (
        """
            QTableWidget{
                gridline-color: #666666;
                selection-background-color: rgba"""
        + styles_config["object_press_color"]
        + """;
                selection-color: rgba"""
        + styles_config["font_color"]
        + """;
            }
            QTableWidget::item:hover{
                background-color: rgba"""
        + styles_config["object_hover_color"]
        + """;
            }
            QTableWidget::item:selected{
                background-color: rgba"""
        + styles_config["object_press_color"]
        + """;
            }
            """
        + vertical_scroll_bar_style()
    )


def header_style():
    return (
        """ 
            ::section:pressed {
                background-color: rgba"""
        + styles_config["main_background_color"]
        + """;
                border: none;
            }
            ::section {
                background-color: rgba"""
        + styles_config["main_background_color"]
        + """;
                border: none;
            }
            """
    )


def tree_style():
    return (
        """
            QHeaderView::section {
                background-color: rgba"""
        + styles_config["main_background_color"]
        + """;
                color: rgba"""
        + styles_config["font_color"]
        + """;
                padding-left: 4px;
                border: 1px solid #6c6c6c;
            }
            QHeaderView::section:hover {
                background-color: rgba"""
        + styles_config["main_background_color"]
        + """;
                border: 2px solid #ca8ad8;
                color: rgba"""
        + styles_config["font_color"]
        + """;
            }
            QTreeView {
                show-decoration-selected: 1;
                outline: 0;
                background-color: rgba"""
        + styles_config["alternative_background_color"]
        + """;
            }
            QTreeView::item {
                color: rgba"""
        + styles_config["font_color"]
        + """;
            }
            QTreeView::item:hover {
                background: rgba"""
        + styles_config["object_hover_color"]
        + """;
            }
            QTreeView::item:selected {
                background: rgba"""
        + styles_config["object_press_color"]
        + """;
            }
            """
        + vertical_scroll_bar_style("alternative_background_color")
    )


btn_basket_style = """
            QPushButton{
                border:none
            } 
            :hover{
                background-color: darkgreen;
            }
            :pressed{
                background-color: green;
            }
            """


def btn_clicked_style():
    return (
        """
            QPushButton{
                border:none;
                color: rgba"""
        + styles_config["font_color"]
        + """;
                background-color: rgba"""
        + styles_config["object_background_color"]
        + """;
            } 
            :hover{
                background-color: rgba"""
        + styles_config["object_hover_color"]
        + """;
            }
            :pressed{
                background-color: rgba"""
        + styles_config["object_press_color"]
        + """;
            }
            """
    )


def tab_style():
    return (
        """
            QTabWidget::pane {
              border: 1px solid gray;
              top: -1px; 
              background: rgba"""
        + styles_config["main_background_color"]
        + """; 
            } 
            
            QTabBar::tab {
              background: rgba"""
        + styles_config["object_background_color"]
        + """; 
              border: 1px solid gray; 
              padding: 15px;
            } 
            
            QTabBar::tab:hover { 
              background: rgba"""
        + styles_config["object_hover_color"]
        + """; 
            }
            
            QTabBar::tab:selected { 
              background: rgba"""
        + styles_config["object_press_color"]
        + """; 
              margin-bottom: -1px; 
            }
            """
    )
