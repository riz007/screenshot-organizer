import os
import shutil
from datetime import datetime

# Get the root folder from the user. Ex. Desktop
root_folder = input("Enter root folder dir (from): ")

# Get the destination folder from the user. It could be something like /Volumes/JohnDoe
destination_folder = input("Enter destination folder dir (to): ")

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

# Get all the files in the root folder
files = os.listdir(root_folder)

# Loop through all the files
for file in files:

    # Check if the file is a Screenshot or Screen Shot
    if file.startswith(("Screenshot", "Screen Shot")):

        # Split the year, month, and date from the file name
        year, month, date = file.split("-")[:3]

        # Get the current date
        today = datetime.today()

        # Create a new folder for today's screenshots
        screenshot_folder = os.path.join(destination_folder, "Screenshots-{}-{}-{}".format(today.year, today.month, today.day))

        # If the folder doesn't exist, create it
        if not os.path.exists(screenshot_folder):
            os.mkdir(screenshot_folder)

        # Move the screenshot to the new folder
        shutil.move(os.path.join(root_folder, file), os.path.join(screenshot_folder, file))

print("Your root screenshots are being organized, please hold on...")

print("Moving was successful!")
