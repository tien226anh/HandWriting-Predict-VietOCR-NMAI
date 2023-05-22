from vietocr.tool.config import Cfg

config = Cfg.load_config_from_name("vgg_transformer")
config["weights"] = "./transformerocr.pth"
config["cnn"]["pretrained"] = False
config["device"] = "cpu"
