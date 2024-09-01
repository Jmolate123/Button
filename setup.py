from setuptools import setup, find_packages

setup(
    name='button',  # Name of your package
    version='0.1.0',  # Initial version
    author='Jmmolate22',
    author_email='jhonmarkmolate@gmail.com',
    description='A Python package for creating buttons',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Jmmolate123/button',  # Replace with your GitHub repository URL
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=[
        # List dependencies here (if any)
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Choose an appropriate license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the minimum Python version
)
