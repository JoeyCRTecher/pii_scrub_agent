
from setuptools import setup, find_packages

setup(
    name='pii_scrub_agent',
    version='0.1.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.25.0",
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A package for scrubbing PII from data.',
    url='https://github.com/yourusername/pii_scrub_agent',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
