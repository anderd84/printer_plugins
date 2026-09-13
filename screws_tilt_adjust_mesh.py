from bed_mesh import BedMesh
from screws_tilt_adjust import ScrewsTiltAdjust
import logging

class ScrewsTiltAdjustMesh:
    bedMesh : BedMesh
    screwTiltAdjust : ScrewsTiltAdjust
    gcode : object
    printer : object
    test : str

    def __init__(self, config):
        logging.debug("LOADING STAM plugin")
        self.printer = config.get_printer()
        self.test = config.get("test")
        self.gcode = self.printer.lookup_object('gcode')
        self.gcode.register_command("SCREWS_TILT_ADJUST_MESH",
                                    self.cmd_SCREWS_TILT_ADJUST_MESH,
                                    desc=self.cmd_SCREWS_TILT_ADJUST_MESH_help)

    cmd_SCREWS_TILT_ADJUST_MESH_help = "Tool to help adjust bed leveling " \
                                       "screws by calculating the number " \
                                       "of turns to level it."
    def cmd_SCREWS_TILT_ADJUST_MESH(self, gcmd):
        self.gcode.respond("Running custom gcode")

def load_config(config):
    return ScrewsTiltAdjustMesh(config)