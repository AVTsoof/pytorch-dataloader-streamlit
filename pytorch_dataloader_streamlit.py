from typing import Dict

import plotly.express as px
import streamlit as st
from torch.utils.data import DataLoader


def run_dataloader_app(
    dataloaders: Dict[str, DataLoader], labels_id_to_str: Dict[int, str]
):
    st.title("Pytorch Dataloader Viewer")
    dataset_to_show = st.radio("DATA TO LOAD", list(dataloaders.keys()))

    n_images = len(dataloaders[dataset_to_show])
    img_idx = st.slider("IMAGE", 0, n_images - 1)

    # postprocess
    img, label = dataloaders[dataset_to_show].dataset[img_idx]
    img = img.squeeze() * 255

    # label
    label_name = labels_id_to_str[int(label)]
    st.write(f"Label: ({label}) {label_name}")

    # show image
    fig = px.imshow(img, aspect="equal")
    st.plotly_chart(fig)
