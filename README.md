## Project Information

## NOTE: NO LONGER MAINTAINED

A work inspired by Kalle Hallden's [ProjectInitializationAutomation](https://github.com/KalleHallden/ProjectInitializationAutomation)

Uses the pygithub library to initialize a GitHub Repository. Copies templates (for example, a readme file) from your templates folder to the newly created repository folder.

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
    ```
2. Open the `.env` file in the cloned repository and enter your credentials and paths in the given spaces
   - **Note: If you do not have a templates folder, you may leave the `TEMPLATES_DIR` environment variable empty**

3. Copy the `.env` file to your scripts folder or any other folder you choose
   - **Note: This program could use an already existing `.env` file. If you wish to merge the variables in this particular file with your own variables, then copy the contents of this file to your `.env` file.**

4. Open the `creator.py` and `open.py` files and in the blank space, enter the directory in which your copied/previously-existing `.env` file is located
    - Will be assigned to a variable called `env_dir`

5. Run the below command from shell:
    ```bash
    python create_executables.py
    ```
    - This will convert the `create.py` and `open.py` files to executables.
  
6. Copy the two files; `create.exe` and `open.exe` into your scripts folder
   
7. Add the scripts folder to your `PATH` environment variables

    The how-to can be found here: https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/


> ## Usage
***Note: Following commands can be executed from any directory, as long as the scripts folder has been added to `PATH`.***

To create a new repository, type the following from any directory in your shell:
   ```bash
   creator <Repository-Name>
   ```

To open a folder/repository from your projects folder:
   ```bash
   open
   ```

**Note: Feel free to rename the exe files to something of your preference!**
---

## Base Requirements

Python 3.0+  
Visual Studio Code 
