from extras.bed_mesh import BedMesh, ZMesh
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

        self.gcode.register_command("STAM__PROCESS_MESH",
                                    self.cmd_STAM__PROCESS_MESH,
                                    desc=self.cmd_STAM__PROCESS_MESH_help)

    def get_z_mesh(self, profile_name: str) -> ZMesh:
        self.gcode.run_script_from_command("BED_MESH_PROFILE LOAD={profile_name}")
        z_mesh: ZMesh = self.bed_mesh.get_mesh()

    def process_mesh(self, z_mesh: ZMesh) -> None:
        z_mesh.print_mesh(self.gcode.respond_info)
        meshed_mat = z_mesh.get_mesh_matrix()

        for y_ndx, y_line in enumerate(meshed_mat):
            logging.info(y_line)
            y_coord = z_mesh.get_y_coordinate(y_ndx)
            for x_ndx, z_coord in enumerate(y_line):
                x_coord = z_mesh.get_x_coordinate(x_ndx)
                logging.info(f"x: {x_coord}, y: {y_coord}, z: {z_coord}")

# ==========================================================================================
    cmd_SCREWS_TILT_ADJUST_MESH_help = "Tool to help adjust bed leveling " \
                                       "screws by calculating the number " \
                                       "of turns to level it."
    def cmd_SCREWS_TILT_ADJUST_MESH(self, gcmd):
        self.gcode.respond_info("Running custom gcode")

        self.gcode.run_script_from_command("BED_MESH_CALIBRATE PROFILE=STAM_mesh")
        z_mesh = self.get_z_mesh("STAM_mesh")
        self.process_mesh(z_mesh)


    cmd_STAM__PROCESS_MESH_help = "TODO"
    def cmd_STAM__PROCESS_MESH(self, gcmd):
        profile = gcmd.get('PROFILE', "STAM_mesh")
        z_mesh = self.get_z_mesh(profile)
        self.process_mesh(z_mesh)



def load_config(config):
    return ScrewsTiltAdjustMesh(config)