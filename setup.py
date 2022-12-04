import os
import glob
import shutil
from setuptools import setup, find_packages, Command

class CompleteClean(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        shutil.rmtree('./build', ignore_errors=True)
        shutil.rmtree('./dist', ignore_errors=True)
        shutil.rmtree('./' + project + '.egg-info', ignore_errors=True)
        for d in glob.glob('./**/__pycache__', recursive=True):
            shutil.rmtree(d, ignore_errors=True)
        for f in glob.glob('./**/*.pyc', recursive=True):
            os.remove(f)

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

project = "proyecto"
setup(
    name=project,
    python_requires='>=3.8',
    version = "1.0.0",
    author="Usuario",
    author_email="usuario@localhost.local",
    description="Proyecto Python con setuptools",
    long_description=read('README.md'),
    url='http://localhost/proyecto',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    cmdclass={'clean': CompleteClean},
    test_suite='nose.collector'
)
