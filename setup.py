from setuptools import setup, find_packages


NAME = 'cou'
VERSION = '0.1.0'
DESCRIPTION = ('CLI utility that counts lines of code within files '
               'and analyzes directories containing code')
LICENCE = 'MIT'
URL = 'https://github.com/zluuba/cou'
AUTHOR = 'Luybov Nikitina'
AUTHOR_EMAIL = 'zluyba.nikitina@gmail.com'
PYTHON_REQUIRES = '>=3.11'

ENTRY_POINTS = {
    'console_scripts': ['cou=cou.cli.app:main'],
}
CLASSIFIERS = [
    'Environment :: Console',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Intended Audience :: Developers',
    'Operating System :: Unix',
    'Topic :: Utilities',
]


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    license=LICENCE,
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    include_package_data=True,
    entry_points=ENTRY_POINTS,
    python_requires=PYTHON_REQUIRES,
    classifiers=CLASSIFIERS,
)
