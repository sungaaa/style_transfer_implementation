import click
import os
import torch
import random

from torch import nn, optim
from torch.utils.data import DataLoader

from tqdm import tqdm
import numpy as np

from dataset import CartoonGANDataset
from model_cartoongan import CartoonGANGenerator, CartoonGANDiscriminator