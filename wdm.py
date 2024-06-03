# this is a helper script for setup of a web driver manager
# https://developer.chrome.com/docs/chromedriver/downloads => main location for web drivers / official docs

# modules/libraries:
import os
import requests
import zipfile

# main function:
def webdriver_manager():

    """
    Download, unzip, and store the content of the file within a specific path

    Parameters:
        None

    Returns:
        None

    Output:
        Stores the downloaded and unzipped webdriver.exe file within "C:\\Users\\Public\\driver\\wdriver\\" path
    """

    # urls and file paths:
    url = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.71/win64/chromedriver-win64.zip" # change if necessary!
    filename = url.split("/")[-1]
    location = f"C:\\Users\\Public\\driver\\wdriver\\{filename}"
    files_to_delete = [filename, "chromedriver.exe"]

    try:
        # check and delete existing files within the path:
        [os.remove(file) for file in files_to_delete]
    except Exception as e:
        print(f"Error deleting files: {e}")

    try:
        # download the .zip file:
        response = requests.get(url)
        with open(location, "wb") as file:
            file.write(response.content)
        
        # uncip the .zip file and store the webdriver.exe
        with zipfile.ZipFile(location, "r") as zip_file:
            destination_folder = "\\".join(location.split("\\")[:-1])
            zip_file.extractall(destination_folder, members=[files_to_delete[1]])

        print("Script executed successfully!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    webdriver_manager()
