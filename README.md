Dependencies:

Python
Selenium WebDriver
ChromeDriver
requests
PIL.Image
playsound


Installation Guide (Windows):

Downloading Python:

Visit the official Python website: https://www.python.org/downloads/
Choose the appropriate Python version (usually the latest stable version) for your Windows system (32-bit or 64-bit).
Download the executable file.

Running the Installer:

Double-click the downloaded Python installer file.
Follow the on-screen instructions:
Customize installation: You can choose the installation location, add Python to the PATH environment variable, and select optional features.
Install: Click the "Install Now" button to proceed.
Finish: Once the installation is complete, click the "Finish" button.

Verifying Python Installation:

Open a command prompt or terminal window.
Type python --version and press Enter.
If Python is installed correctly, you'll see the installed Python version displayed.

Installing pip:

Automatic installation: Pip is usually included with modern Python installations. To verify if it's installed, try running the following command in the command prompt:
  
    `pip --version`
  
If no version is shown, you have to install it manually.

Installing Dependencies:

      `pip install selenium requests PIL playsound google-generativeai`

Installing ChromeDriver:
Download the appropriate ChromeDriver executable for your Windows version from https://chromedriver.chromium.org/downloads
Place the chromedriver.exe file in a directory where you store these files.

Getting API key:
Go to https://aistudio.google.com/app/apikey and generate an API key.
Open main.py and navigate to line 91 and paste the key there. The line is marked with a comment so you should easily find it.

Running:

Navigate to the folder where you have places the main.py and chromedriver file. 
Open command prompt in ther file and run this command
      `python main.py`
    
          
