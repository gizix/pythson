import os
import seedir as sd
from dotenv import load_dotenv

load_dotenv()
PROJECT_PATH = os.getenv('PROJECT_PATH')


def see_dir_project() -> None:
    sd.seedir(path=PROJECT_PATH, style='lines', itemlimit=10, sort=True,
              exclude_folders=['.git', 'venv311', 'tests', '__pycache__', '.gitattributes',
                               '.gitignore', '.idea'])


if __name__ == '__main__':
    see_dir_project()