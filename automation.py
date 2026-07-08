import os
import shutil

source_folder = "Source_Folder"
destination_folder = "Destination_Folder"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

count = 0

for file_name in os.listdir(source_folder):

    if file_name.endswith(".jpg"):

        old_path = os.path.join(
            source_folder,
            file_name
        )

        new_path = os.path.join(
            destination_folder,
            file_name
        )

        shutil.move(
            old_path,
            new_path
        )

        print(file_name, "Moved Successfully")

        count += 1


print("Task Completed")
print("Total Files Moved:", count)