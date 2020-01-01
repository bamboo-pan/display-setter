from setuptools import setup, find_packages
from os import path

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
   
setup(
    name='DisplaySetter',
    version='1.0.1',
    description='this is a tool to set display',
    long_description=long_description, 
    long_description_content_type='text/markdown',
    url='https://github.com/pypa/sampleproject', 
    author='bamboo.pan',
    author_email='bamboo.pan@hp.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='display',
    packages=find_packages(where='src'),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
    install_requires=[],
    include_package_data = True,
    package_dir = {'':'src'},
    package_data={'displaysetter': ['*.pyd'],},
)