#! SHEBANG

env_dir = "__PASTE-DIRECTORY-HERE__" # directory which holds your .env file

"""
Lists all projects in the project directory
Opens user selected project in VSCode
"""

import os
from dotenv import load_dotenv

# Dotenv configs
dotenv_path = os.path.join(env_dir, ".env")
load_dotenv(dotenv_path)

class project_opener():
    def __init__(self):
        self.projects_dir = os.getenv("PROJECTS_DIR")
        self.github_username = os.getenv("G_USERNAME")

    def welcome_user(self):
        print(f"""\n=============== Welcome Back, {self.github_username}! =============== \n""")

    def open_project(self):
        # Displaying all the languages in the directory
        print("Folders in your project directory:")
        languages = [f.name for f in os.scandir(self.projects_dir) if f.is_dir()]
        for i, lang in enumerate(languages):
            print(f"\t{i}. {lang}")

        chosen_lang_index = int(input("\nWhich language is your project using? "))
        chosen_lang = languages[chosen_lang_index]
        chosen_lang_path = os.path.join(self.projects_dir, chosen_lang)

        print(f"\nThese are your current {chosen_lang} projects: ")
        projects = [f.name for f in os.scandir(chosen_lang_path) if f.is_dir()]
        for i, project in enumerate(projects):
            if os.path.isdir(os.path.join(chosen_lang_path, project)): 
                print(f"\t{i}. {project}")

        # Gathering info for opening the project
        project_number = int(input("\nWhich project (number) would you like to open? "))
        project_name = projects[project_number]
        project_path = os.path.join(chosen_lang_path, project_name)
        print(project_path)

        os.system(f"cd {project_path} && code .")
    
    def run_all(self):
        functions = [
            self.welcome_user(),
            self.open_project()
        ]

        for function in functions:
            function()

            
if __name__ == "__main__":
    project_opener().run_all()

    
