# setup.py
from setuptools import setup, find_packages

setup(
    name="minecraft-hardcore2survival",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "nbtlib>=2.0.0",
    ],
    entry_points={
        "console_scripts": [
            "mc-hardcore2survival=minecraft_hardcore2survival.converter:main",
        ],
    },
    author="Jekyl-Gaming",
    author_email="harrelson@gmail.com",
    description="A tool to convert Minecraft hardcore worlds to survival mode",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/CulleyHarrelson/MinecraftHardcore2Survival",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
