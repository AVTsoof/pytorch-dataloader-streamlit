# PyTorch DataLoader Streamlit

# Makefile
[Makefile](./Makefile) is used to run some check on the project.  
Use by running: 
```bash
$ make all
```

# Usage

File: `my_app.py`
```python
from torch.utils.data import DataLoader, Dataset
from pytorch_dataloader_streamlit import run_dataloader_app

dataset: Dataset = ...
dataloader: DataLoader = DataLoader(dataset, ...)

run_dataloader_app(DataLoader)
```

Command Line:
```bash
$ streamlit run my_app.py
```

