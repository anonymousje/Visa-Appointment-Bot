
**Dependencies:**

* Python
* Selenium WebDriver
* ChromeDriver
* requests
* PIL.Image
* playsound

**Installation Guide (Windows):**

**Downloading Python:**

1. Visit the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Choose the appropriate Python version (usually the latest stable version) for your Windows system (32-bit or 64-bit).
3. Download the executable file.

**Running the Installer:**

1. Double-click the downloaded Python installer file.
2. Follow the on-screen instructions:
   * Customize installation: You can choose the installation location, add Python to the PATH environment variable, and select optional features.
   * Install: Click the "Install Now" button to proceed.
   * Finish: Once the installation is complete, click the "Finish" button.

**Verifying Python Installation:**

1. Open a command prompt or terminal window.
2. Type `python --version` and press Enter.
3. If Python is installed correctly, you'll see the installed Python version displayed.

**Installing pip:**

* Automatic installation: Pip is usually included with modern Python installations. To verify if it's installed, try running the following command in the command prompt:

```bash
pip --version
```

* If no version is shown, you have to install it manually.

**Installing Dependencies:**

Open a command prompt or terminal window and run:

```bash
pip install selenium requests PIL playsound google-generativeai
```

**Installing ChromeDriver:**

1. Download the appropriate ChromeDriver executable for your Windows version from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
2. Place the `chromedriver.exe` file in a directory included in your system PATH environment variable, or in a directory where you store these files.

**Getting API key (if using google-generativeai):**

1. Go to [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) and generate an API key.
2. Open `main.py` and navigate to line 91 (approximately). Look for the comment that mentions the API key.
3. Paste your generated API key on that line.

**Running the Script:**

1. Navigate to the folder where you have placed the `main.py` and `chromedriver.exe` file.
2. Open a command prompt in that folder and run this command:

```bash
python main.py
```

          
