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
def move_files():
    pass


# Function to organize files
def organize_files():
    pass


# Main function
def main():
    create_folders()
    organize_files()


if __name__ == "__main__":
    main()
