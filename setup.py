import os

from setuptools import setup, find_packages, version


here = os.path.abspath(os.path.dirname(__file__))


setup(
    name="notify",
    version='0.0.1',
    url='https://github.com/abdullahbodur/gtm_notify',
    author="bodur",
    author_mail="abdullahbodur.abbdr@gmail.com",
    packages=find_packages(),
    install_requires=[
    ],
    description="GTM Social Media Bots for notify actions for users."

)
