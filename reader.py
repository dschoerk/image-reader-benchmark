
class ImageReader:
    def __init__(self) -> None:
        pass

    def read_image(self, path: str):
        raise NotImplementedError()

import cv2
class OpencvImageReader(ImageReader):
    def __init__(self) -> None:
        super().__init__()

    def read_image(self, path: str):
        return cv2.imread(path)

import jpeg4py
class Jpeg4PyImageReader(ImageReader):
    def __init__(self) -> None:
        super().__init__()

    def read_image(self, path: str):
        return jpeg4py.JPEG(path).decode()

from PIL import Image
class PILImageReader(ImageReader):
    def __init__(self) -> None:
        super().__init__()

    def read_image(self, path: str):
        return Image.open(path)

import simplejpeg
class SimplejpegImageReader(ImageReader):
    def __init__(self) -> None:
        super().__init__()

    def read_image(self, path: str):
        with open(path, 'rb') as fp:
            data = fp.read()
            im = simplejpeg.decode_jpeg(data)
            return im

# https://github.com/etemesi254/zune-jpeg