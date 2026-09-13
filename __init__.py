import importlib, logging, os

class PluginManager:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.plugin_name = config.get_name().split()[1]

        logging.info(f"========= [PRINTER PLUGIN MANAGER ({self.plugin_name})] =========")
        # logging.info("Plugin : %s" % (self.plugin_name,))

        py_name = os.path.join(os.path.dirname(__file__), self.plugin_name + '.py')
        if not os.path.exists(py_name):
            raise self.config_error("Unable to load module '%s' (doesn't exist)" % (py_name,))

        mod = importlib.import_module(f"{__package__}.{self.plugin_name}", package=__package__)

        init_func = 'load_config'
        init_func = getattr(mod, init_func, None)

        if init_func is None:
            raise self.config_error("Unable to load module '%s' (no load_config function)" % (py_name,))

        self.plugin = init_func(config)

        logging.info("Plugin Load Success!")
        logging.info(f"========= [PRINTER PLUGIN MANAGER ({self.plugin_name})] =========")

def load_config_prefix(config):
    return PluginManager(config)