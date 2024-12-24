import sys
from PyQt6.QtWidgets import QApplication
from presentation.views.main_window import MainWindow
from business.controllers.main_controller import MainController

def main():
    app = QApplication(sys.argv)
    
    # 加载样式表
    with open('presentation/styles/main.qss', 'r') as style_file:
        app.setStyleSheet(style_file.read())
    
    # 创建主窗口和控制器
    main_window = MainWindow()
    main_controller = MainController(main_window)
    
    main_window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main() 