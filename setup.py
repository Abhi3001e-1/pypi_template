import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "IPYNBrendrer"
AUTHOR_USER_NAME = "Abhi3001e-1"
SRC_REPO = "IPYNBrendrer"
AUTHOR_EMAIL = "mastery.india01@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description= "A small python package",
    long_description= long_description,
    long_description_content_type="text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where = "src")
)