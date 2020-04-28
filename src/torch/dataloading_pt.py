import torch
from torch.utils.data import Dataset
import glob
import numpy as np
import random
from edflow.data.util import edu.DatasetMixin

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        elem = l[i : i + n]
        random.shuffle(elem)
        yield elem


class Human3M_Dataset(Dataset):
    def __init__(self, path, chunk_size, n_shuffle):
        vids = [f for f in glob.glob(path + "*/*", recursive=True)]
        frames = []
        for vid in vids:
            for chunk in chunks(
                sorted(
                    glob.glob(vid + "/*.jpg", recursive=True),
                    key=lambda x: int(x.split("/")[-1].split(".jpg")[0]),
                ),
                chunk_size,
            ):
                if len(chunk) == chunk_size:
                    random.shuffle(chunk)
                    frames.append(chunk)

        self.frames = frames

    def __len__(self):
        return len(self.frames)

    def __getitem__(self, i):
        return self.frames[i]


class Toy_StochasticPairs(edu.DatasetMixin):
    def __init__(self):
        super(Toy_StochasticPairs, self)

    def get_example(self, i):
        a = np.zeros((128, 128, 3))
        b = np.zeros((128, 128, 3))
        example = {"a": a, "b": b}
        return example

    def __len__(self):
        return 1000