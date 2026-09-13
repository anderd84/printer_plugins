# from . import screws_tilt_adjust_mesh
import logging

class PluginManager:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.test = config.get("test2")
        logging.info(f"test2: {self.test}")
        # self.STAM = screws_tilt_adjust_mesh.ScrewsTiltAdjustMesh(config)

def load_config(config):
    return PluginManager(config)