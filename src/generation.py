import numpy as np
import barebones_ml as bbml
import json

class Generator:
    def __init__(self, model_path):
        amount_layers = 0
        activations = []
        with open(model_path / "model.json") as f:
            raw_unloaded_data = json.load(f)
            amount_layers = raw_unloaded_data["amount_layers"]
            activations = raw_unloaded_data["activations"]
        self.network = bbml.Network("softmax_cross_entropy")
        for i in range(amount_layers - 1, -1, -1):
            self.network.add(bbml.PreTrainedLayer(model_path / f"layer_{i}_weights.npy", model_path / f"layer_{i}_biases.npy", activations[i]))
        for i, layer in enumerate(self.network.layers):
            layer.weights = layer.weights.T

    def generate(self, input_python_array):
        input_np_array = np.array(input_python_array)
        outputs = self.network.forward(input_np_array, reverse=True)
        return outputs