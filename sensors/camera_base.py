from typing import *
from abc import ABCMeta
import numpy as np

class ImageFrame(NamedTuple):
    name: str = ''
    color: Optional[np.ndarray]
    depth: Optional[np.ndarray]
    Extrinsic: Optional[np.ndarray]




class CameraBase(metaclass=ABCMeta):
    def __init__(self):
        pass

    def capture_frame(self):
        pass


