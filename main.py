from typing import List

import plotly.express as px
import streamlit as st
import torch
from torch.utils.data import DataLoader, Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor

labels_map = {
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
    st.title("Pytorch Dataloader Viewer")

    dataloaders = get_dataloaders()

    dataset_to_show = st.radio("Dataset", ["train", "test"])

    n_images = len(dataloaders[dataset_to_show])
    img_idx = st.slider("IMAGE", 0, n_images - 1)
    img, label = dataloaders[dataset_to_show].dataset[img_idx]
    img = img.squeeze()
    img = img * 255
    label_name = labels_map[int(label)]
    st.write(f"Label: ({label}) {label_name}")
    fig = px.imshow(img, aspect="equal")
    st.plotly_chart(fig)


@st.cache_resource()
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
