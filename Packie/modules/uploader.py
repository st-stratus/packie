import os

def upload(NAME, USER, PASS):
    os.system(f'py -m twine upload --repository pypi packages/{NAME}/dist/* -u {USER} -p {PASS}')