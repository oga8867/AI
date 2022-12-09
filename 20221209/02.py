import pandas as pd
import os
import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
import numpy as np
import cv2

class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotations_file, names=['file_name','labels'],skiprows=[0])
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir,self.img_labels.iloc[idx,0])
        try:
            image = read_image(img_path)
        except:
            print(self.img_labels.iloc[idx,0])
            exit()
        label = int(self.img_labels.iloc[idx,1])
        if self.transform:
            image - self.transform(image)
        if self.target_transform:
            label= self.target_transform(label)
        return image, label





class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.liner(784,512) #앞이 력 뒤가 출력인 필터
        self.fc2 = nn.liner(512, 256)
        self.fc3 = nn.liner(256, 128)
        self.fc4 = nn.liner(128, 64)
        self.fc5 = nn.liner(64, 32)
        self.fc6 = nn.liner(32, 10)

    def forward(self,x):
        x = x.float()
        h1 = F.relu(self.fc1(x.view(-1,784)))
        h2 = F.relu(self.fc2(h1))
        h3 = F.relu(self.fc3(h2))
        h4 = F.relu(self.fc4(h3))
        h5 = F.relu(self.fc5(h4))
        h6 = self.fc6(h5)
        return F.log_softmax(h6, dim=1)
