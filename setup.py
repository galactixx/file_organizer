from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='file_organizer',
    version='0.0.10',
    description='CLI program to organize files',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/galactixx/file_organizer',
    author='galactixx',
    license='MIT',
    python_requires='>=3.10'
)