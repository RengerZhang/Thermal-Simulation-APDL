from ansys.mapdl.core import launch_mapdl

project_root = r"C:\Users\24880\Desktop\Thermal-Simulation-APDL\.MAC\image.mac"

mapdl = launch_mapdl(exec_file="C:/Program Files/ANSYS Inc/v241/ANSYS/bin/winx64/ansys241.exe")
mapdl.clear()
mapdl.input(project_root)


print('calcuelate done!')
mapdl.exit()