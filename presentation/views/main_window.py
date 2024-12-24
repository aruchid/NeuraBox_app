from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NeuraBox")
        self.setMinimumSize(800, 600)
        
        # 创建中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建布局
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # 添加组件
        title_label = QLabel("NeuraBox - 神经网络应用")
        layout.addWidget(title_label)
        
        self.train_button = QPushButton("训练模型")
        layout.addWidget(self.train_button)
        
        self.predict_button = QPushButton("预测")
        layout.addWidget(self.predict_button) 