from typing import Dict, List

import plotly.express as px
import torch
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

from pytorch_dataloader_streamlit import run_dataloader_app

labels_id_to_str = {
    0: "T-Shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",
}


def main() -> None:
    dataloaders = get_dataloaders()
    run_dataloader_app(dataloaders, labels_id_to_str=labels_id_to_str)


def get_dataloaders() -> List[DataLoader]:
    training_data = datasets.FashionMNIST(
        root="data", train=True, download=True, transform=ToTensor()
    )

    test_data = datasets.FashionMNIST(
        root="data", train=False, download=True, transform=ToTensor()
    )

    train_dataloader = DataLoader(training_data, batch_size=64, shuffle=False)
    test_dataloader = DataLoader(test_data, batch_size=64, shuffle=False)

    return {"train": train_dataloader, "test": test_dataloader}


if __name__ == "__main__":
    main()
