# setup.py

from setuptools import setup, find_packages

setup(
    name="image-ascii",
    version="0.1.0",
    author="Tianhukj",
    author_email="tianhukj@outlook.com",
    description="A simple tool to convert images to ASCII art",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown/ascii",
    url="https://github.com/tianhukj/image-ascii",
    packages=find_packages(),
    install_requires=[
        "Pillow",
    ],
    entry_points={
        'console_scripts': [
            'image_ascii=image-ascii.image-ascii:convert_image_to_ascii',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
