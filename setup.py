from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as fh:
    requirements = fh.readlines()

setup(
    name='carbonsh',
    version='0.0.5',
    packages=['carbonsh'],
    url='https://github.com/MrMarble/carbonsh',
    license='GPL-3.0-or-later',
    author='MrMarble',
    author_email='alvarotinocomarmol@gmail.com',
    description='carbon.now.sh python module',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    tests_require=['pytest>=6.0.1<7'],
    python_requires=">=3.6<4",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
