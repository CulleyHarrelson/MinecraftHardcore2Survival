# MinecraftHardcore2Survival

A Python tool to convert Minecraft hardcore worlds to survival mode. This tool allows you to continue playing your hardcore world after death by converting it to survival mode.

## Features

- Converts hardcore worlds to survival mode
- Automatically creates backups before conversion
- Command-line interface for easy use
- Safe error handling with automatic backup restoration

## Installation

You can install this package directly from GitHub:

```bash
git clone https://github.com/CulleyHarrelson/MinecraftHardcore2Survival
cd MinecraftHardcore2Survival
pip install -e .
```

## Usage

### Command Line

```bash
mc-hardcore2survival path/to/level.dat
```

### Example

```bash
mc-hardcore2survival ~/Library/Application\ Support/ModrinthApp/profiles/1.21\ VP/saves/MyWorld/level.dat
```

## Safety Features

- Automatic backup creation before any modifications
- Automatic backup restoration if anything goes wrong
- Non-destructive operation - original files are preserved

## Requirements

- Python 3.7 or higher
- nbtlib 2.0.0 or higher

## Development

To set up the development environment:

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install development dependencies:
   ```bash
   pip install -e .
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the Minecraft community
