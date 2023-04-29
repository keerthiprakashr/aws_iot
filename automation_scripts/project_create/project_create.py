"""
Author : Keerthiprakashr
Date: 29/April/2023
Automation script to create python project

This script creates 
a new Python project with the given name,
and optional git repository 
and virtual environment.

    Parameters:
    project_name (str): The name of the new project.
    create_git_repo (bool): Whether to initialize a new git repository (default False).
    create_virtual_env (bool): Whether to create a new virtual environment (default False).
    encoding (str): The file encoding to use (default 'utf-8').

    Returns:
    None

"""

import os
import shutil
import subprocess


def create_project(project_name: str,
                   create_git_repo: bool = False,
                   create_virtual_env: bool = False,
                   encoding: str = 'utf-8') -> None:
    """
    create project function
    """
    # Copy project template
    shutil.copytree('project-template', project_name)
    os.chdir(project_name)

    # Create README, main, and requirements files
    with open('README.md', mode='w', encoding=encoding) as f:
        f.write(f'# {project_name}\n')

    with open('main.py', mode='w', encoding=encoding) as f:
        f.write('# Your code goes here\n')
        
    # Initialize git repository
    if create_git_repo:
        subprocess.run(['git', 'init'])
        print('Git repository initialized.')

    # Create virtual environment
    if create_virtual_env:
        subprocess.run(['python3', '-m', 'venv', 'env'])
        print('Virtual environment created.')

    #pip install dependencies
    #  subprocess.run(['pip', 'install', '-r', 'requirements.txt'])


if __name__ == "__main__":
    project_name = input("Enter project name: ")
    create_git_repo = input("Create git repository? (y/n): ").lower() == 'y'
    create_virtual_env = input("Create virtual environment? (y/n): ").lower() == 'y'
    create_project(project_name, create_git_repo=='y', create_virtual_env='y')
    