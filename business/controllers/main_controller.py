from presentation.views.main_window import MainWindow
from business.services.model_service import ModelService

class MainController:
    def __init__(self, view: MainWindow):
        self.view = view
        self.model_service = ModelService()
        
        # 连接信号和槽
        self.view.train_button.clicked.connect(self.handle_train)
        self.view.predict_button.clicked.connect(self.handle_predict)
    
    def handle_train(self):
        # 处理训练逻辑
        pass
    
    def handle_predict(self):
        # 处理预测逻辑
        pass 