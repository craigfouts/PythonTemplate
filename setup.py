from setuptools import find_packages, setup

with open('README.md') as file:
    readme = file.read()

with open('LICENSE') as file:
    license = file.read()

setup(
    name='Python-Application-Template',
    version='1.0',
    description='Python application template.',
    long_description=readme,
    author='Craig Fouts',
    author_email='foutscw@gmail.com',
    url='https://github.com/foutscw/Python-Application-Template',
    packages=find_packages(exclude=('docs', 'tests')),
    license=license
)
