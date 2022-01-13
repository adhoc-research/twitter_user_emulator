from setuptools import setup
from os import path

DIR = path.dirname(path.abspath(__file__))
INSTALL_PACKAGES = open(path.join(DIR, 'requirements.txt')).read().splitlines()

with open(path.join(DIR, 'README.md')) as f:
    README = f.read()

setup(
    name='twitter_user_emulator',
    packages=['twitter_user_emulator'],
    description="Twitter-User Emulating Tweet Generator",
    long_description=README,
    long_description_content_type='text/markdown',
    install_requires=INSTALL_PACKAGES,
    version='0.0.1',
    url='https://github.com/equ1/twitter_user_emulator',
    author='Rushat Rai',
    author_email='rushatrai@gmail.com',
    keywords=['deep-learning', 'gpt-2', 'twitter'],
    include_package_data=True,
    python_requires='>=3.6',
    license="MIT",
)
