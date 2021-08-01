import os
import torch
import random
import numpy as np


def device():
    """Returns CUDA if GPU is present else returns CPU"""
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def set_seed(seed):
    """Completely reproducible results are not guaranteed across 
    PyTorch releases, individual commits, or different platforms. 
    Furthermore, results may not be reproducible between CPU 
    and GPU executions, even when using identical seeds.

    However, there are some steps you can take to limit the 
    number of sources of nondeterministic behavior for a 
    specific platform, device, and PyTorch release. 
    First, you can control sources of randomness that can 
    cause multiple executions of your application to behave 
    differently. Second, you can configure PyTorch to avoid 
    using nondeterministic algorithms for some operations, 
    so that multiple calls to those operations, given the
    same inputs, will produce the same result.

    Sets seed for random, np.random and for torch.manual_seed. 
    If GPU is present then it torch.manual_seed_all is also set 
    to the same value"""
    random.seed(26)
    np.random.seed(26)
    torch.manual_seed(26)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def get_model():
    """Returns pretained model path or if not exists 
    downloads te model else raise FileNotFoundError."""
    relative_path = os.path.join(os.path.abspath(os.path.dirname(
        os.path.dirname(os.path.dirname(__file__)))), "model")
    return os.path.abspath(relative_path)
