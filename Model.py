import torch
import torch.nn as nn
import numpy as np

class MLPModel(nn.Module):
    def __init__(self, input_dim, hidden_dim=128, output_dim=5):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, output_dim)
        )

    def forward(self, x):
        return self.net(x)

def load_model_and_predict(features: np.ndarray) -> str:
    model = MLPModel(input_dim=len(features))
    model.load_state_dict(torch.load('saved_model.pt', map_location=torch.device('cpu')))
    model.eval()

    with torch.no_grad():
        x = torch.tensor(features, dtype=torch.float32).unsqueeze(0)
        prediction = model(x).squeeze().numpy()

    mbti_map = ['ENFP', 'INTJ', 'ENTP', 'ISFJ', 'INFJ']
    return mbti_map[int(np.argmax(prediction) % len(mbti_map))]
