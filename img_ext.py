import os
import shutil
import pandas as pd

# Set folder paths
source_folder = r"C:\Users\admin\Desktop\FY24-25\desk\img\JUNE"  # Folder with 322 images
destination_folder = r"C:\Users\admin\Desktop\FY24-25\desk\img\FOLDER 27"  # Folder to store selected 226 images
excel_file = r"C:\Users\admin\Desktop\FY24-25\desk\img\image_list.xlsx"  # Excel file with list of image names

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Read image names from Excel
df = pd.read_excel(excel_file)
image_names = df['Image Name'].astype(str).tolist()

# Copy matching files
not_found = []
for image_name in image_names:
    src_path = os.path.join(source_folder, image_name)
    dest_path = os.path.join(destination_folder, image_name)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dest_path)
    else:
        not_found.append(image_name)

print(f"Copied {len(image_names) - len(not_found)} images to: {destination_folder}")
if not_found:
    print(f"\n⚠️ {len(not_found)} images were not found in the source folder:")
    for nf in not_found:
        print(f" - {nf}")
