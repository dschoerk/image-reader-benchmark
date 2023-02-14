
import numpy as np
from dataset import CocoDataset
import reader
from tqdm import tqdm


reader_cls = reader.ImageReader.__subclasses__()
reader_cls = [reader.SimplejpegImageReader, reader.Jpeg4PyImageReader]
print(reader_cls)

def do_benchmark(cls):
    ds = CocoDataset()

    reader = cls()
    for p in tqdm(ds.paths()):
        im = reader.read_image(p)
        arr = np.asarray(im)


for cls in reader_cls:
    print(f'Benchmark for {cls}')
    do_benchmark(cls)
    