from setuptools import find_packages, setup

HYPEN_E_DOT = "-e ."
def get_requirements(file:str):
    """
    Returns a list of requirements from the given file (one per line)
    """
    requirements = []
    with open(file, "r") as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements



setup(
    name="mlproject",
    version="0.0.1",
    author="Maruthi",
    author_email="marurohi@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)