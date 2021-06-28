"""
Creates a repository locally and uses webscraping to create a repository online
"""

import sys
import os
from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

env_dir = "____________________________________________" # directory which holds your .env file
dotenv_path = os.path.join(env_dir, ".env")

load_dotenv(dotenv_path)

github_username = os.getenv("G_USERNAME")
github_password = os.getenv("G_PASSWORD")
projects_dir = os.getenv("PROJECTS_DIR")

folderName = str(sys.argv[1])
folderName = folderName.replace(' ', '-')

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://github.com/login')

def create_new_dir():
    os.makedirs(os.path.join(projects_dir, folderName))

def create_repo_online():
    python_button = browser.find_elements_by_xpath("//input[@name='login']")[0]
    python_button.send_keys(github_username)
    python_button = browser.find_elements_by_xpath("//input[@name='password']")[0]
    python_button.send_keys(github_password)
    python_button = browser.find_elements_by_xpath("//input[@name='commit']")[0]
    python_button.click()
    browser.get('https://github.com/new')
    python_button = browser.find_elements_by_xpath("//input[@name='repository[name]']")[0]
    python_button.send_keys(folderName)
    python_button = browser.find_element_by_css_selector('button.btn-primary.btn')
    python_button.submit()
    browser.quit()

def create_repo_locally():
    cd_command = f'cd {projects_dir}/{folderName}'
    commands = [
        f'{cd_command} && git init',
        f'{cd_command} && git remote add origin git@github.com:{github_username}/{folderName}.git',
        f'{cd_command} && touch README.md',
        f'{cd_command} && git add .',
        f'{cd_command} && git commit -m "Initial commit',
        f'{cd_command} && git push -u origin master',
        f'{cd_command} && code .'
    ]

    for c in commands:
        os.system(c)

if __name__ == "__main__":
    create_new_dir()
    create_repo_online()
    create_repo_locally()