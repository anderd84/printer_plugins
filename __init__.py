from . import screws_tilt_adjust_mesh
import logging

class PluginManager:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.plugin_val = config.get("plugin_val")
        self.name = config.get_name()
        logging.info("LOADING PLUGIN MANAGER")
        logging.info("name : %s", self.name)
        self.plugin = screws_tilt_adjust_mesh.ScrewsTiltAdjustMesh(config)

def load_config_prefix(config):
    return PluginManager(config)