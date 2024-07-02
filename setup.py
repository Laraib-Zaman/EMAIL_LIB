# email_service_package/setup.py

from setuptools import setup, find_packages

setup(
    name='email_service',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # No additional dependencies needed for smtplib, ssl, and email.message
    ],
    entry_points={
        'console_scripts': [
            # If you want to add command-line scripts
        ],
    },
)
