import os
import shutil
import datetime

def pack(LOC, SMLDES, AUTH, NAME, VERS, HOME, BUG, EMAIL, LGDESC, _REPACK_):
    if _REPACK_:
        shutil.rmtree(f'packages/{NAME}')
    os.mkdir(f'packages/{NAME}')
    shutil.copytree(LOC, f'packages/{NAME}/src/{NAME}')
    f = open('dat/pyproject.toml', 'r')
    PYPJ = f.read()
    f.close()
    f = open(f'packages/{NAME}/pyproject.toml', 'w')
    f.write(PYPJ.replace('%PNAME%', NAME).replace('%VERSION%', VERS).replace('%MAIL%', EMAIL).replace('%USERNAME%', AUTH).replace('%HOMEPAGE%', HOME).replace('%BUGPAGE%', BUG).replace('%DESC%', SMLDES))
    f.close()
    f = open('dat/README.md', 'r')
    PYRM = f.read()
    f.close()
    f = open(f'packages/{NAME}/README.md', 'w')
    f.write(PYRM.replace('%RDME%', LGDESC))
    f.close()
    f = open('dat/LICENSE', 'r')
    LIC = f.read()
    f.close()
    f = open(f'packages/{NAME}/LICENSE', 'w')
    f.write(LIC.replace('%YR%', str(datetime.date.today().year)))
    f.close()
    os.chdir(f'packages/{NAME}')
    os.system('py -m build')
    os.chdir('..')
