from setuptools import find_packages,setup
from typing import List
#     this fn will return the list of requirements
edot = "-e ."
def get_requirements(file_path:str) -> List[str]:
    req = []
    with open(file_path) as file_obj:
        req = file_obj.readlines()
        req = [r.replace("\n", "") for r in req]
        if edot in req:
            req.remove(edot)
    return req
setup(
    name='movie-recommender',
    version='0.0.1',
    author="Kavya",
    author_email='kavya.sivaguru@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)