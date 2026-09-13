from . import screws_tilt_adjust_mesh

class PluginManager:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.STAM = screws_tilt_adjust_mesh.ScrewsTiltAdjustMesh(config)

def load_config(config):
    return PluginManager(config)