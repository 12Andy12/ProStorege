import src.resources


def vertical_scroll_bar_style(background_color="rgb(50, 50, 50);") -> str:
    vertical_scroll_bar = """
            QScrollBar:vertical {
                border:none;
                background: """ + background_color + """
                width: 10px;
            }

            QScrollBar::handle:vertical {
                background: rgb(100, 100, 100);
                min-height: 20px;
                border-radius: 5px;
            }

            QScrollBar::add-line:vertical {
                border:none;
                background: """ + background_color + """
                height: 20px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }

            QScrollBar::sub-line:vertical {
                border:none;
                background: """ + background_color + """
                height: 20px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }

            QScrollBar::add-page:vertical {
                background: """ + background_color + """
            }

            QScrollBar::sub-page:vertical {
                background: """ + background_color + """
            }
            """
    return vertical_scroll_bar


combo_box_style = """
            QComboBox { 
                background-color: rgb(65, 65, 65);
                selection-background-color: rgb(65, 65, 65);
                selection-color: rgb(177, 177, 177);
            }
            QComboBox:hover {
                background-color: rgb(70, 70, 70);
            }
            QComboBox::drop-down {
                width: 0px;
                height: 0px;
                border: 0px;
            }
            QComboBox QAbstractItemView {
                color: rgb(177, 177, 177);
                background-color: rgb(100, 100, 100);
                padding: 10px;
                border: 2px solid rgb(55, 55, 55);
                border-radius: 5px;
                padding-left: 5px;
                padding-right: 5px;
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: rgb(120, 120, 120);
            }
            QComboBox QAbstractItemView::item:selected {
                background-color: rgb(120, 120, 120);
            }
            """

date_edit_style = """
            QDateEdit{
                background-color: rgb(65, 65, 65);
                color: rgb(177, 177, 177);
                border: none;
            }
            QDateEdit:hover{
                background-color: rgb(70, 70, 70);
                border: none;
            }
            QDateEdit::drop-down {
                background-color: rgb(80, 80, 80);
                width: 25px; 
                border-left-width: 3px;
                border-left-color: rgb(120, 120, 120);
                border-left-style: solid;  
                background-position: center;
                background-repeat: no-reperat;
                image: url(:/iconCalendar.png);
            }
            QDateEdit QAbstractItemView {
                color: rgb(177, 177, 177);  
                background-color: rgb(75, 75, 75);
            }
            QDateEdit QAbstractItemView::item:hover {
                background-color: rgb(90, 90, 90);
            }
            QDateEdit QAbstractItemView::item:selected {
                background-color: rgb(120, 120, 120);
            }
            QCalendarWidget QWidget { 
                alternate-background-color: rgb(55, 55, 55);
            }            
            /* меню выбора месяца           */
            CalendarWidget QToolButton QMenu {
                 background-color: rgb(100, 100, 100);
            }
            CalendarWidget QToolButton QMenu::item {
                padding: 10px;
                background-color: rgb(80, 80, 80);
            }
            CalendarWidget QToolButton QMenu::item:hover {
                background-color: rgb(120, 120, 120);
            }
            CalendarWidget QToolButton QMenu::item:selected {
                background-color: rgb(220, 220, 220);
            }
            CalendarWidget QToolButton::menu-indicator {
                image: none;
            }
            #qt_calendar_prevmonth, #qt_calendar_nextmonth {
                border: none;                     /* убрать границу */ 
                font-weight: bold;              /* шрифт полужирный */
                color: rgb(177, 177, 177);
                /* Удалить стандартное изображение клавиши со стрелкой. 
                   Вы также можете настроить                         */
                qproperty-icon: none;    
                background-color: rgb(50, 50, 50)
            }
            #qt_calendar_prevmonth {
                qproperty-text: "<";         /* Изменить текст кнопки  */
            }
            #qt_calendar_nextmonth {
                qproperty-text: ">";
            }
            #qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {
                background-color: rgb(55, 55, 55);
            }
            #qt_calendar_prevmonth:pressed, #qt_calendar_nextmonth:pressed {
                background-color: rgb(65, 65, 65);
            }
            #qt_calendar_yearbutton, #qt_calendar_monthbutton {
                color: rgb(177, 177, 177);
                background-color:rgb(50, 50, 50);
                border-radius: 30px;
                min-width: 85px;
            }
            #qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {
                background-color: rgb(55, 55, 55);
            }
            #qt_calendar_yearbutton:pressed, #qt_calendar_monthbutton:pressed {
                background-color: rgb(65, 65, 65);
            }
            /* ниже календарной формы */
            #qt_calendar_calendarview {
                outline: 0px;                                 /* Удалить выделенную пунктирную рамку */
                selection-background-color: rgb(120, 120, 120); /* Выберите цвет фона */
                color:rgb(177, 177, 177);
                border-radius: 5px; 
            }
            #qt_calendar_yearedit {
                color: rgb(177, 177, 177);
                background: transparent;   

                min-width: 70px;
            }
            #qt_calendar_yearedit::up-button { 
                color: rgb(177, 177, 177);
                width: 20px;
                height: 20px;
                border-radius: 10px;
                background-color: rgb(50, 50, 50);
                subcontrol-position: right;
                image: url(:/iconUp.png);      
            }
            #qt_calendar_yearedit::up-button:hover { 
                background-color: rgb(70, 70, 70); 
            }
            #qt_calendar_yearedit::up-button:selected { 
                background-color: rgb(80, 80, 80); 
            }
            #qt_calendar_yearedit::down-button { 
                color: rgb(177, 177, 177);
                width: 20px;
                height: 20px;
                border-radius: 10px;
                background-color: rgb(60, 60, 60);
                subcontrol-position: left;  
                image: url(:/iconDown.png);     
            }
            #qt_calendar_yearedit::down-button:hover { 
                background-color: rgb(70, 70, 70); 
            }
            #qt_calendar_yearedit::down-button:selected { 
                background-color: rgb(80, 80, 80); 
            }
            """


def spin_box_style(height="30", background_color="rgb(65, 65, 65)"):
    return """
            QDoubleSpinBox {
                padding-right: 15px; /* make room for the arrows */
                background-color: """ + background_color + """;
            }
            QDoubleSpinBox::up-button {
                subcontrol-origin: border;
                subcontrol-position: right; /* position at the top right corner */

                width: 25px;
                height: """ + height + """;
                image: url(:/iconPlus.png) 1;
            }

            QDoubleSpinBox::up-button:hover {
                background-color: rgb(75, 75, 75);
            }

            QDoubleSpinBox::up-button:pressed {
                background-color: rgb(90, 90, 90);
            }

            QDoubleSpinBox::down-button {
                subcontrol-origin: border;
                subcontrol-position: left; /* position at the bot right corner */

                width: 25px;
                height: """ + height + """;
                image: url(:/iconMinus.png) 1;
            }

            QDoubleSpinBox::down-button:hover {
                background-color: rgb(75, 75, 75);
            }

            QDoubleSpinBox::down-button:pressed {
                background-color: rgb(90, 90, 90);
            }
            """


btn_close_style = """
            QPushButton{
                border:none
            }
            :hover{
                background-color: darkred;
            }
            :pressed{
                background-color: red;}
            """

table_style = """
            QTableWidget{
                gridline-color: #666666;
                selection-background-color: rgb(70, 70, 70);
                selection-color: rgb(177, 177, 177);
            }
            QTableWidget::item:hover{
                background-color: rgb(60, 60, 60);
            }
            QTableWidget::item:selected{
                background-color: rgb(70, 70, 70);
            }
            """ + vertical_scroll_bar_style()

header_style = """ 
            ::section:pressed {
                background-color: #323232;
                border: none;
            }
            ::section {
                background-color: #323232;
                border: none;
            }
            """

btn_change_style = """
            QPushButton{
                border:none
            }
            :hover{
                background-color: darkorange;
            }
            :pressed{
                background-color: orange;
            }
            """

btn_open_style = """
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

btn_folder_style = """
            QPushButton{
                border: none;
                text-align: left;
                font: 20px;
            }
            :hover{
                background-color: darkgreen;
            }
            :pressed{
                background-color: green;
            }
            """

tree_style = """
            QHeaderView::section {
                background-color: rgb(50, 50, 50);
                color: #b1b1b1;
                padding-left: 4px;
                border: 1px solid #6c6c6c;
            }
            QHeaderView::section:hover {
                background-color: rgb(50, 50, 50);
                border: 2px solid #ca8ad8;
                color: #fff;
            }
            QTreeView {
                show-decoration-selected: 1;
                outline: 0;
                background-color: rgb(55, 55, 55);
            }
            QTreeView::item {
                color: rgb(177, 177, 177);
            }
            QTreeView::item:hover {
                background: rgb(70, 70, 70);
            }
            QTreeView::item:selected {
                background: rgb(90, 90, 90);
            }
            """ + vertical_scroll_bar_style("rgb(55, 55, 55);")

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

btn_clicked_style = """
            QPushButton{
                border:none;
                background-color: rgb(60, 60, 60);
            } 
            :hover{
                background-color: rgb(65, 65, 65);
            }
            :pressed{
                background-color: rgb(70, 70, 70);
            }
            """

tab_style = """
            QTabWidget::pane {
              border: 1px solid gray;
              top: -1px; 
              background: rgb(50, 50, 50); 
            } 
            
            QTabBar::tab {
              background: rgb(60, 60, 60); 
              border: 1px solid gray; 
              padding: 15px;
            } 
            
            QTabBar::tab:hover { 
              background: rgb(70, 70, 70); 
            }
            
            QTabBar::tab:selected { 
              background: rgb(80, 80, 80); 
              margin-bottom: -1px; 
            }
            """
