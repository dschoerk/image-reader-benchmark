import wget
import zipfile
import utils
from pathlib import Path

class CocoDataset:
    def __init__(self, force_prepare=False):
        self.url = 'http://images.cocodataset.org/zips/val2017.zip'
        self.path_to_zip = 'data/tmp/val2017.zip'
        self.coco_path = 'data/coco'
        self.prepare(force=force_prepare)
        self.image_paths = list((Path(self.coco_path) / 'val2017').iterdir())

    def __len__(self):
        return len(self.image_paths)

    def paths(self):
        for p in self.image_paths:
            yield str(p)

    def prepare(self, force=False):
        # def download_and_extract_zip(): TODO: refactor to method if need more often
        if force or not (Path(self.coco_path) / 'val2017').is_dir():

            if force or not Path(self.path_to_zip).is_file():
                wget.download(self.url, self.path_to_zip, wget.bar_adaptive )

            hash = utils.md5(self.path_to_zip)
            print(hash)
            if hash != '442b8da7639aecaf257c1dceb8ba8c80':
                raise Exception(f'hash does not match for {self.url} and file {self.coco_path}')

            with zipfile.ZipFile(self.path_to_zip, 'r') as zip_ref:
                zip_ref.extractall(self.coco_path)

            Path(self.path_to_zip).unlink()