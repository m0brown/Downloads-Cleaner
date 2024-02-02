import os

# File types to be organized
EXTN_AUDIO = ['.mp3', '.wav', '.flac', '.m4a', '.aac', '.ogg', '.wma']
EXTN_DOC = ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.rtf', '.csv', '.xml', '.json', '.html',
            '.htm']
EXTN_IMAGE = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.eps', '.raw', '.cr2', '.nef', '.orf',
              '.sr2']
EXTN_INSTALLER = ['.exe', '.msi', '.dmg', '.deb', '.rpm', '.apk']
EXTN_VIDEO = ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.vob', '.3gp', '.m4v', '.mpg', '.mpeg']

base_path = os.path.expanduser("~")


# Function to create folders if they do not exist
def create_folders():
    destination_folders = ['Audio', 'Documents', 'Pictures', 'Installers', 'Videos', 'Others']
    for folder in destination_folders:
        # Create folder path
        dir_path = os.path.join(base_path, folder)
        # Check if folder exists, if not create it
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
            print(f"Folder {folder} created successfully!")
        else:
            print(f"Folder {folder} already exists!")


# Function to move files to respective folders
def move_files(folder_name, files):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    for file in files:
        old_path = os.path.join(os.getcwd(), file)
        new_path = os.path.join(os.getcwd(), folder_name, file)
        os.rename(old_path, new_path)
        print(f"Moved: {file} to {folder_name}")


# Function to organize files
def organize_files():
    files = os.listdir(os.getcwd())
    for file in files:
        if os.path.isfile(file):
            file_name, file_extn = os.path.splitext(file)
            if file_extn in EXTN_AUDIO:
                move_files('Audio', [file])
            elif file_extn in EXTN_DOC:
                move_files('Documents', [file])
            elif file_extn in EXTN_IMAGE:
                move_files('Pictures', [file])
            elif file_extn in EXTN_INSTALLER:
                move_files('Installers', [file])
            elif file_extn in EXTN_VIDEO:
                move_files('Videos', [file])
            else:
                move_files('Others', [file])
    print("Files organized successfully!")


# Main function
def main():
    create_folders()
    organize_files()


if __name__ == "__main__":
    main()
