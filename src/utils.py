"""
Utility functions for loading and processing Rouault Exp3 data.
Handles path resolution so notebooks work from any directory.
"""
import sys
from pathlib import Path
import scipy.io as sio
import numpy as np

SRC_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SRC_DIR.parent
DATA_DIR = PROJECT_ROOT / "data"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

def get_data_path(filename="Exp3.mat"):
    filepath = DATA_DIR / filename
    if not filepath.exists():
        raise FileNotFoundError(f"Data file not found: {filepath}")
    return filepath

def load_exp3(mat_path=None):
    if mat_path is None:
        mat_path = get_data_path("Exp3.mat")
    
    mat = sio.loadmat(str(mat_path), squeeze_me=True, struct_as_record=False)
    return mat["Exp3"]

def get_project_root():
    return PROJECT_ROOT

def load_x_ser6_all():
    exp3 = load_exp3()
    return np.array(exp3.X_ser6_all, dtype=float)
