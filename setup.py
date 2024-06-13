from setuptools import setup, find_packages

setup(
    name='json2mdheadings',
    version='1.0.0',
    description='A Python package for converting JSON data to Markdown with keys as headings up to the 6th level, then using nested lists after that.',
    author='Brian Novak',
    author_email='tajrkala@gmail.com',
    url='https://github.com/bnovak1/json2mdheadings',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies required by your package here
    ]
)