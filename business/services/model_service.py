from data.models.neural_net import NeuralNetwork

class ModelService:
    def __init__(self):
        self.model = None
    
    def create_model(self, input_size, hidden_size, output_size):
        self.model = NeuralNetwork(input_size, hidden_size, output_size) 