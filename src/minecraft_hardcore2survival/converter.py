# src/minecraft_hardcore2survival/converter.py
from nbtlib import nbt, tag
import shutil
import os
from datetime import datetime
from pathlib import Path
import argparse
import sys
import logging


def setup_logging():
    """Configure logging for the application"""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    return logging.getLogger(__name__)


def convert_hardcore_to_survival(level_dat_path: str | Path) -> bool:
    """
    Convert a Minecraft hardcore world to survival mode.

    Args:
        level_dat_path: Path to the level.dat file

    Returns:
        bool: True if conversion was successful, False otherwise
    """
    logger = logging.getLogger(__name__)
    level_dat_path = Path(level_dat_path)

    if not level_dat_path.exists():
        logger.error(f"Error: {level_dat_path} not found")
        return False

    # Create backup first
    backup_path = level_dat_path.with_name(
        f"level.dat.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    )

    try:
        shutil.copy2(level_dat_path, backup_path)
        logger.info(f"Created backup: {backup_path}")
    except Exception as e:
        logger.error(f"Error creating backup: {e}")
        return False

    try:
        # Load the NBT file
        nbt_file = nbt.load(level_dat_path)
        current_mode = nbt_file["Data"]["Player"]["playerGameType"]
        logger.info(f"Current game mode: {current_mode}")

        # Set to survival mode (0)
        nbt_file["Data"]["Player"]["playerGameType"] = tag.Int(0)

        # Save the changes
        nbt_file.save()
        logger.info("Successfully changed game mode to survival (0)")
        return True

    except Exception as e:
        logger.error(f"Error modifying level.dat: {e}")
        logger.info("Restoring backup...")
        try:
            shutil.copy2(backup_path, level_dat_path)
            logger.info("Backup restored successfully")
        except Exception as restore_error:
            logger.error(f"Error restoring backup: {restore_error}")
        return False


def main():
    """Main entry point for the command line interface"""
    parser = argparse.ArgumentParser(
        description="Convert a Minecraft hardcore world to survival mode"
    )
    parser.add_argument("level_dat", type=str, help="Path to the level.dat file")

    args = parser.parse_args()
    setup_logging()

    success = convert_hardcore_to_survival(args.level_dat)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
