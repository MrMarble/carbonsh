from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='carbonsh',
    version='0.0.1',
    packages=['carbonsh'],
    url='https://github.com/MrMarble/carbonsh',
    license='GPL-3.0-or-later',
    author='MrMarble',
    author_email='',
    description='carbon.now.sh python module',
    long_description=long_description,
    long_description_content_type="text/markdown", install_requires=['pyppeteer']
)
