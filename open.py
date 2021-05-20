"""
Lists all projects in the project directory
Opens user selected project in VSCode
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()

projects_dir = os.getenv("PROJECTS_DIR")

def welcome_user():
    print(f"""\n=============== Welcome Back, {os.getenv("G_USERNAME")}! =============== \n""")

def open_project():
    # Displaying all the projects in the directory
    print("Here are your current projects: \n")

    projects = os.listdir(projects_dir)
    for i, file in enumerate(projects):
        if os.path.isdir(f"{projects_dir}/{file}"): 
            print(f"    {i}. {file}")

    # Gathering info for opening the project
    project_number = int(input("\nWhich project (number) would you like to open? "))
    project_name = projects[project_number]
    project_path = f"{projects_dir}/{project_name}"
    print(project_path)

    os.system(f"cd {project_path} && code .")

if __name__ == "__main__":
    welcome_user()
    open_project()

    