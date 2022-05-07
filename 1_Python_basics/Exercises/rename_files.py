import os
import datetime


def rename_files_in_folder(folder):
    for file in [os.path.join(folder, file) for file in os.listdir(folder) if
                 os.path.isfile(os.path.join(folder, file))]:
        dot_index = file.index(".", 2)
        time = datetime.datetime.fromtimestamp(os.path.getctime(file))
        time = time.strftime("%Y%m%d_%H%M")
        renamed_file = file[:dot_index] + time + file[dot_index:]
        os.rename(src=file, dst=renamed_file)


rename_files_in_folder(".\Test")
