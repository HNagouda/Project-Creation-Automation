## Project Information

A work inspired by Kalle Hallden's ProjectInitializationAutomation: https://github.com/KalleHallden/ProjectInitializationAutomation

Uses Webscraping with Selenium to initialize a GitHub Repository

Built for Windows OS.

---

## How To Use: 

> ### Preperation
Make sure you have a valid and authenticated SSH key for GitHub 

More information can be found here: https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

---

> ### Setup

1. Run the following commands from shell:
    ```bash
    git clone "https://github.com/HNagouda/Project-Creation-Automation.git"
    cd Project-Creation-Automation
    pip install -r requirements.txt
    python create_executables.py
    ```
2. Open the `.env` file in the cloned repository and enter your credentials

3. Copy the three files; `create.exe`, `open.exe`, and `.env` into your scripts folder
   
4. Add the scripts folder to your `PATH` environment variables

    The how-to can be found here: https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/


> ## Usage
***Note: Following commands can be executed from any directory, as long as the scripts folder has been added to `PATH`.***

To create a new repository, type the following from any directory in your shell:
   ```bash
   create <Repository-Name>
   ```

To open a folder/repository from your projects folder:
   ```bash
   open
   ```

---

## Base Requirements

Python 3.0+  
Visual Studio Code 
