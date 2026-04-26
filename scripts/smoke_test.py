"""Confirm the environment can load a session and the deps import cleanly."""

from pathlib import Path

import matplotlib
import mne
import numpy as np
import scipy.io
import sklearn

DATA = Path(__file__).resolve().parent.parent / "data" / "subject_1_fvep_led_training_1.mat"

print(f"numpy {np.__version__}")
print(f"scipy {scipy.__version__}")
print(f"matplotlib {matplotlib.__version__}")
print(f"mne {mne.__version__}")
print(f"sklearn {sklearn.__version__}")

mat = scipy.io.loadmat(DATA)

print(f"\nLoaded {DATA.name}")
print(f"Top-level keys: {[k for k in mat.keys() if not k.startswith('__')]}")
for k, v in mat.items():
    if k.startswith("__"):
        continue
    shape = getattr(v, "shape", "?")
    dtype = getattr(v, "dtype", "?")
    print(f"  {k}: shape={shape}, dtype={dtype}")
