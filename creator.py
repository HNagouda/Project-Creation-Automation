#! SHEBANG

"""
Creates a repository locally and uses the GitHub python API to create a repository online
"""

env_dir = "__PASTE-DIRECTORY-HERE__" # directory which holds your .env file


import os
import sys
import shutil
import logging
import argparse
from github import Github
from dotenv import load_dotenv

# Dotenv Configs
load_dotenv(os.path.abspath(os.path.join(env_dir, ".env")))

# Logger Configs
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s', datefmt='%d-%b-%y %H:%M:%S')

handler.setFormatter(formatter)
logger.addHandler(handler)


class repo_creator():
    def __init__(self):
        # Stored .env Credentials
        self.projects_dir = os.getenv("PROJECTS_DIR")
        self.templates_dir = os.getenv("TEMPLATES_DIR")
        self.github_username = os.getenv("G_USERNAME")
        self.github_token = os.getenv("ACCESS_TOKEN")


    def parse_user_cmd(self):
        # Configuring argparse
        parser = argparse.ArgumentParser(description='Collect Project Language and Project Name')
        parser.add_argument('-l', '--language', metavar='Lang', type=str, nargs='?', const='none', default='none',
                            help = 'The language your new project will be using. Your project will be stored in a directory called {your language} under your main projects folder')
        parser.add_argument('-n', '--name', metavar='Name', type=str, required=True,
                            help = 'Name of your new project')  
        parser.add_argument('-t', '--templates', type=str, choices=['y', 'n'],
                            nargs='?', const='n', default='n',
                            help = '[Y]/[N] Specify whether you would want to copy any possible templates from a templates directory to your new project (default: [N])')                           
        args = parser.parse_args()

        # Update class variables and create project_path
        self.project_language = str(args.language).strip().lower().capitalize()
        self.project_name = str(args.name).strip().lower().title().replace(' ', '-')
        self.use_templates = str(args.templates).strip().lower()


    def get_project_path(self):     
        if self.project_language == 'None':
            self.project_path = os.path.abspath(os.path.join(self.projects_dir, 
                                            'No-Language',
                                            self.project_name))

            logger.warning(f' No project language specified. New project will be created at {self.project_path}\n')

        else:
            self.project_path = os.path.abspath(os.path.join(self.projects_dir, 
                                            self.project_language, 
                                            self.project_name))
            
            logger.info(f' New {self.project_language} project will be created at {self.project_path}\n')


    def create_proj_dir(self):
        try:
            os.makedirs(self.project_path)  
            logger.info(f' Created project directory: {self.project_path}\n')

        except PermissionError:
            logger.warning(f' PermissionError occurred while creating directory:\n{self.project_path}\n')

            sys.exit(1)

        except FileExistsError:
            logger.critical(f' FileExistsError: Cannot create an already existing directory: {self.project_path}\n')

            sys.exit(1)

            
    def copy_templates(self):
        if self.templates_dir:
            language_templates_dir = os.path.abspath(os.path.join(self.templates_dir, self.project_language))

            logger.info(f' Templates directory found at {language_templates_dir}. Copying templates...\n')            
            shutil.copytree(src=language_templates_dir, 
                            dst=os.path.abspath(os.path.join(self.project_path, 'templates')))
        else:
            logger.exception(' You requested copying your templates to your new project, but the templates directory does not exist. Check for typos in the .env file. Creating new project without copying templates...\n')


    def create_repo_online(self):
        try: 
            user = Github(self.github_token).get_user()
            logger.info(f' Authenticated GitHub user "{user.login}": Creating new GitHub repository {self.project_name}\n')
            user.create_repo(self.project_name)
        except Exception as e:
            logger.exception(f""" WARNING: Check error message below for details - Most likely caused by Invalid credentials (github token) being provided. Check the .env file for typos and confirm whether the github token provided has the necessary permissions.
            Required Permissions: repo, repo:status, repo_deployment, public_repo, security:events\n""")

            sys.exit(1)

        
    def initialize_repo_locally(self):
        if self.use_templates == 'y':
            self.copy_templates()
        else:
            pass
        
        cd_command = f'cd {self.project_path}'
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
        methods = [
            self.parse_user_cmd,
            self.get_project_path,
            self.create_proj_dir,
            self.create_repo_online,
            self.initialize_repo_locally
        ]

        for method in methods:
            method()


if __name__ == "__main__":
    repo_creator().run_all()