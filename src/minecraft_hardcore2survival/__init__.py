# src/minecraft_hardcore2survival/__init__.py
"""
MinecraftHardcore2Survival - A tool to convert Minecraft hardcore worlds to survival mode.

This package provides functionality to safely convert Minecraft hardcore worlds
to survival mode, allowing players to continue playing after death.
"""

from .converter import convert_hardcore_to_survival

__version__ = "0.1.0"
__author__ = "Jekyl Gaming"
__email__ = "harrelson@gmail.com"

__all__ = ["convert_hardcore_to_survival"]
