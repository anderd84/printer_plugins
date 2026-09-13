from . import screws_tilt_adjust_mesh
import logging

class PluginManager:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.plugin_val = config.get("plugin_val")
        self.name = config.get_name()
        logging.info("LOADING PLUGIN MANAGER\n")
        logging.info("name : %s\n" % (self.name,))
        self.plugin = screws_tilt_adjust_mesh.ScrewsTiltAdjustMesh(config)
        logging.info("DONE LOADING MANAGER")

def load_config_prefix(config):
    return PluginManager(config)