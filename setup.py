from setuptools import setup, find_packages

setup(
    name='ipynb_viewer',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pyfiglet',
    ],
    entry_points={
        'console_scripts': [
            'ipynb_viewer=ipynb_viewer.main:main',
        ],
    },
    author='@PrinceTheProgrammer',
    author_email='princetheprogrammer@gmail.com',
    description='A command-line tool to view Jupyter Notebook files in the terminal',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/the-ai-developer/ipynb_viewer',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
