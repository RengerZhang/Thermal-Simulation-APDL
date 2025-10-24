from ansys.mapdl.core import launch_mapdl

project_root = r"C:\Users\24880\Desktop\Thermal-Simulation-APDL\.MAC\image.mac"

mapdl = launch_mapdl(exec_file="D:\Program Files\ANSYS Inc\v251\ansys\bin\winx64\ANSYS251.exe")
mapdl.clear()
mapdl.input(project_root)


print('calcuelate done!')
mapdl.exit()