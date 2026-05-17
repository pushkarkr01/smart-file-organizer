import os
import shutil

# -----------------------------
# STEP 1: Folder path input
# -----------------------------
folder_path = input("Enter the folder path to organize: ")

# -----------------------------
# STEP 2: Define file types
# -----------------------------
file_types = {
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav"],
    "Code": [".py", ".java", ".cpp", ".js", ".html", ".css"]
}

# -----------------------------
# STEP 3: Create folders if not exist
# -----------------------------
for folder in file_types.keys():
    path = os.path.join(folder_path, folder)
    if not os.path.exists(path):
        os.mkdir(path)

# "Others" folder
others_path = os.path.join(folder_path, "Others")
if not os.path.exists(others_path):
    os.mkdir(others_path)

# -----------------------------
# STEP 4: Organize files
# -----------------------------
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    file_moved = False

    # Check file type
    for folder_name, extensions in file_types.items():
        if any(file.lower().endswith(ext) for ext in extensions):
            shutil.move(file_path, os.path.join(folder_path, folder_name, file))
            file_moved = True
            break

    # If no match
    if not file_moved:
        shutil.move(file_path, os.path.join(folder_path, "Others", file))

print("✅ Files organized successfully!")