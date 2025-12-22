#This file looks for new folders inside user uploads and converts them to reel if they are not already converted
import os
def text_to_audio(folder):
    print("tta -",folder)

def create_reel(folder):
    print("cr -",folder)


if __name__ == "__main__":
    with open("done.txt","r") as f:
        done_folders = f.readlines()

    done_folders = [f.strip() for f in done_folders]
    folders = os.listdir("user_uploads")
    for folder in folders: 
        if (folder not in done_folders):   
            text_to_audio(folder)
            create_reel(folder)
            with open("done.txt","a") as f:
                f.write(folder + "\n")