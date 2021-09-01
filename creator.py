"""
Creates a repository locally and uses webscraping to create a repository online
"""

import os
import sys
import shutil
from github import Github
from threading import Thread
from dotenv import load_dotenv

env_dir = "C:/Users/harsh/.0_Personal-Inventory" # directory which holds your .env file
dotenv_path = os.path.join(env_dir, ".env")
load_dotenv(dotenv_path)

class main():
    def __init__(self):
        self.project_name = str(sys.argv[1]).replace(' ', '-')
        self.github_username = os.getenv("G_USERNAME")
        self.github_token = os.getenv("ACCESS_TOKEN")
        self.projects_dir = os.getenv("PROJECTS_DIR")
        self.templates_dir = os.getenv("TEMPLATES_DIR")

    def create_new_dir(self):
        os.makedirs(os.path.join(self.projects_dir, self.project_name))

    def create_repo_online(self):
        from github import Github
        user = Github(self.github_token).get_user()
        repo = user.create_repo(self.project_name)

    def copy_templates(self):
        if self.templates_dir:
            templates = os.listdir(self.templates_dir)
            
            for template in templates:
                src = os.path.join(self.templates_dir, template)
                dest = os.path.join(self.projects_dir, self.project_name, template)
                if os.path.isfile(src):
                    shutil.copyfile(src, dest)
        
    def clone_repo_locally(self, templates=True):
        cd_command = f'cd {self.projects_dir}/{self.project_name}'

        if templates:
            self.copy_templates()
        else:
            pass

        commands = [
            f'{cd_command} && git init',
            f'{cd_command} && git remote add origin git@github.com:{self.github_username}/{self.project_name}.git',
            f'{cd_command} && touch README.md',
            f'{cd_command} && git add .',
            f'{cd_command} && git commit -m "Initial commit',
            f'{cd_command} && git push -u origin master',
            f'{cd_command} && code .'
        ]

        for c in commands:
            os.system(c)
    
    def run_all(self):
        if __name__ == "__main__":
            Thread(target = self.create_new_dir()).start()
            Thread(target = self.create_repo_online()).start()
            Thread(target = self.clone_repo_locally()).start()

run = main()
run.run_all()