import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed, first_layer=64, second_layer=64):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            first_layer (int): Number of nodes in first hidden layer
            second_layer (int): Number of nodes in second hidden layer
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)

        self.fc1 = nn.Linear(state_size, first_layer)
        self.fc2 = nn.Linear(first_layer, second_layer)
        self.fc3 = nn.Linear(second_layer, action_size)

    def forward(self, state):
        """
        Build a network that maps state -> action values
        """
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))
        
        return self.fc3(x)
