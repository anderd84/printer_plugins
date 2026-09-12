from bed_mesh import BedMesh
from screws_tilt_adjust import ScrewsTiltAdjust

class ScrewsTiltAdjustMesh:
    bedMesh : BedMesh
    screwTiltAdjust : ScrewsTiltAdjust
    gcode : object
    printer : object
    test : str

    def __init__(self, config):
        self.printer = config.get_printer()
        self.test = config.get("test")
        self.gcode = self.printer.lookup_object('gcode')
        self.gcode.register_command("SCREWS_TILT_ADJUST_MESH",
                                    self.cmd_SCREWS_TILT_ADJUST_MESH,
                                    desc=self.cmd_SCREWS_TILT_ADJUST_MESH_help)
        self.gcode.respond_info(self.test)

    cmd_SCREWS_TILT_ADJUST_MESH_help = "Tool to help adjust bed leveling " \
                                       "screws by calculating the number " \
                                       "of turns to level it."
    def cmd_SCREWS_TILT_ADJUST_MESH(self, gcmd):
        pass

def load_config(config):
    return ScrewsTiltAdjustMesh(config)