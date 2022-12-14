from z15_configurator import create_time_file, read_setting_file, read_time_file


read_setting_file(file_path="/home/yeyeto2788/Downloads/camera_recorder/original_files/settings.dat")
print("\n\n\n")
read_time_file(file_path="/home/yeyeto2788/Downloads/camera_recorder/original_files/time.dat")
print("\n\n\n")
# create_settings_file("./setting.dat")
create_time_file(file_path="./time.dat")
read_time_file(file_path="./time.dat")
exit()
