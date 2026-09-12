from bed_mesh import BedMesh
from screws_tilt_adjust import ScrewsTiltAdjust

class ScrewsTiltAdjustMesh:
    bedMesh : BedMesh
    screwTiltAdjust : ScrewsTiltAdjust


    def __init__(self, config):
        self.printer = config.get_printer()


    def cmd_SCREWS_TILT_ADJUST_MESH(self, gcmd):
        pass

