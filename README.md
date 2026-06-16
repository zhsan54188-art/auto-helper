# Windows Auto Helper System

A complete automation system for Windows with no programming required.

## Quick Start

### Option 1: Automatic Setup (Recommended)
1. Download the project
2. **Double-click `setup.bat`** - Automatically installs and configures
3. **Double-click `run.bat`** - Start the system

### Option 2: Manual Setup
1. Double-click `install.bat` to install dependencies
2. Edit `config.yaml` and replace `YourUsername` with your Windows username
3. Double-click `run.bat` to start

## Files

- `setup.bat` - Automatic configuration (run first time)
- `run.bat` - Start the program
- `install.bat` - Install Python dependencies
- `config.yaml` - Task configuration
- `main.py` - Main program
- `requirements.txt` - Python dependencies

## Features

✅ Auto-organize files by type
✅ Automatic backups
✅ System monitoring (CPU, memory, disk)
✅ Scheduled task execution
✅ Temporary file cleanup

## How to Configure

Edit `config.yaml` to change tasks:

```yaml
tasks:
  - name: "Task name"
    type: "organize_files"  # Task type
    enabled: true           # Enable/disable
    schedule: "08:00"       # Time to run
```

## Supported Times

- `08:00` - Every day at 8 AM
- `14:30` - Every day at 2:30 PM
- `02:00` - Every day at 2 AM

## Troubleshooting

**Error: 'nul' is not recognized**
- Fixed! Use the new run.bat and install.bat files

**Error: Python not detected**
- Install Python 3.8+: https://www.python.org/downloads/
- Make sure to check "Add Python to PATH"

**Missing dependencies**
- Run `setup.bat` or `install.bat` to install

## Starting the Program

Recommended: **Double-click `setup.bat`**

Or:
1. Double-click `install.bat`
2. Edit `config.yaml`
3. Double-click `run.bat`

## More Info

- All activity logs saved in `logs/` folder
- Backup files saved to path in config.yaml
- Press `Ctrl+C` to stop the program

Enjoy! 🚀
