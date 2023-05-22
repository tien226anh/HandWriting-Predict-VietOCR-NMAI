import matplotlib.pyplot as plt
from PIL import Image

from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg


class ImageProcessor:
    def __init__(self):
        self.detector = self.get_detector()
        self.processed_images = []

    def get_config(self):
        config = Cfg.load_config_from_name("vgg_transformer")

        config["weights"] = "./weights/transformerocr.pth"
        # config["cnn"]["pretrained"] = False
        config["device"] = "cpu"
        return config

    def get_detector(self):
        config = self.get_config()
        detector = Predictor(config)
        return detector

    def process_image(self, img_path):
        img = Image.open(img_path)
        plt.imshow(img)

        s = self.detector.predict(img)
        self.processed_images.append(img_path)
        return s

    def get_processed_images(self):
        return self.processed_images
