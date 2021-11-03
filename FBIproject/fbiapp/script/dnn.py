import torch 
import torchvision
import os
import numpy as np
from pathlib import Path
from torch import nn

k = 30
net = nn.Sequential(
    nn.Linear(5,k),
    nn.ReLU(),
    nn.BatchNorm1d(k),
    nn.Linear(k,k),
    nn.ReLU(),
    nn.BatchNorm1d(k),
    nn.Linear(k,k),
    nn.ReLU(),
    nn.BatchNorm1d(k),
    nn.Linear(k,5),
    nn.Softmax(dim=1)
)

net_6 = nn.Sequential(
    nn.Linear(5,k),
    nn.ReLU(),
    nn.BatchNorm1d(k),
    nn.Linear(k,k),
    nn.ReLU(),
    nn.BatchNorm1d(k),
    nn.Linear(k,k),
    nn.ReLU(),
    nn.BatchNorm1d(k),
    nn.Linear(k,6),
    nn.Softmax(dim=1)
)


def classify(data):
    device = torch.device('cpu')

    result = []
    model_path = '/Users/choisaywhy/Desktop/졸업작품/FBIproject/fbiapp/script/model/pretrained_'

    model_list = ['생리량', '생리통', '냄새', '신체활동', '실내활동']
    value_list = [0,1,2,3,4]

    for index ,path in zip(value_list, model_list):
        path = model_path + path + '.pt'

        data = np.array(data, dtype= np.int64)
        data = torch.FloatTensor(data)
        data = data.reshape(-1)  
        data = torch.unsqueeze(data, 0)

        if index == 4 :
            model = net_6
            model.load_state_dict(torch.load(path, map_location = device))
            model.eval()

            output = model(data)
            value, index = torch.max(output, 1)

            percentages = torch.nn.functional.softmax(output, dim=1)[0] * 100
            
            result.append(percentages.tolist())
            continue

        model = net
        model.load_state_dict(torch.load(path, map_location = device))
        model.eval()

        output = model(data)
        value, index = torch.max(output, 1)

        percentages = torch.nn.functional.softmax(output, dim=1)[0] * 100

        percentages = np.round(percentages.tolist(), 3).tolist()


        result.append(percentages)
    
    print(result)
    return result
