#! SHEBANG

"""
Lists all projects in the project directory
Opens user selected project in VSCode
"""

import os
from threading import Thread
from dotenv import load_dotenv

env_dir = "C:/Users/harsh/.0_Personal-Inventory" # directory which holds your .env file
dotenv_path = os.path.join(env_dir, ".env")
load_dotenv(dotenv_path)

class main():
    def __init__(self):
        self.projects_dir = os.getenv("PROJECTS_DIR")
        self.github_username = os.getenv("G_USERNAME")

    def welcome_user(self):
        print(f"""\n=============== Welcome Back, {self.github_username}! =============== \n""")

    def open_project(self):
        # Displaying all the projects in the directory
        print("Here are your current projects: \n")

        projects = os.listdir(self.projects_dir)
        for i, file in enumerate(projects):
            if os.path.isdir(f"{self.projects_dir}/{file}"): 
                print(f"    {i}. {file}")

        # Gathering info for opening the project
        project_number = int(input("\nWhich project (number) would you like to open? "))
        project_name = projects[project_number]
        project_path = f"{self.projects_dir}/{project_name}"
        print(project_path)

        os.system(f"cd {project_path} && code .")
    
    def run_all(self):
            Thread(target = self.welcome_user()).start()
            Thread(target = self.open_project()).start()

            
if __name__ == "__main__":
    main().run_all()

    
