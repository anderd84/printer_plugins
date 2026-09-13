from extras.bed_mesh import BedMesh
from extras.screws_tilt_adjust import ScrewsTiltAdjust
from gcode import GCodeDispatch
import logging

class ScrewsTiltAdjustMesh:
    bed_mesh : BedMesh
    screws_tilt_adjust : ScrewsTiltAdjust
    gcode : GCodeDispatch
    printer : object
    adjust_mesh_val : int

    def __init__(self, config):
        logging.info("LOADING STAM plugin")
        self.printer = config.get_printer()
        self.adjust_mesh_val = config.getint("adjust_mesh_val")
        self.gcode = self.printer.lookup_object('gcode')

        self.screws_tilt_adjust = self.printer.lookup_object('screws_tilt_adjust')
        self.bed_mesh = self.printer.lookup_object('bed_mesh')

        self.gcode.register_command("SCREWS_TILT_ADJUST_MESH",
                                    self.cmd_SCREWS_TILT_ADJUST_MESH,
                                    desc=self.cmd_SCREWS_TILT_ADJUST_MESH_help)

# ==========================================================================================
    cmd_SCREWS_TILT_ADJUST_MESH_help = "Tool to help adjust bed leveling " \
                                       "screws by calculating the number " \
                                       "of turns to level it."
    def cmd_SCREWS_TILT_ADJUST_MESH(self, gcmd):
        self.gcode.respond_info("Running custom gcode")
        self.gcode.run_script("BED_MESH_CALIBRATE")


def load_config(config):
    return ScrewsTiltAdjustMesh(config)