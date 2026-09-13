from . import screws_tilt_adjust_mesh
import logging

class PluginManager:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.test = config.get("test_val")
        logging.info("LOADING PLUGIN MANAGER")
        self.plugin = screws_tilt_adjust_mesh.ScrewsTiltAdjustMesh(config)

def load_config_prefix(config):
    return PluginManager(config)