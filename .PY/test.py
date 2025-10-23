from ansys.mapdl.core import launch_mapdl

project_root = r"C:\Users\24880\Desktop\Thermal-Simulation-APDL\.MAC\image.mac"

mapdl = launch_mapdl()
mapdl.clear()
mapdl.input(project_root)


print('calcuelate done!')
mapdl.exit()