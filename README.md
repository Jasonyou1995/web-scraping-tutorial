# Web Scraping Tutorial

A fun and comprehensive tutorial for you to learn web scraping using Python.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [macOS](#macos)
  - [Windows](#windows)
  - [Linux](#linux)
- [Running the Hello World Tutorial](#running-the-hello-world-tutorial)
- [What You'll Learn](#what-youll-learn)
- [Required Packages](#required-packages)

## Prerequisites

Before starting this tutorial, you should have:
- Basic knowledge of Python programming
- A text editor or IDE (VS Code, PyCharm, etc.)
- Terminal/Command Prompt access

## Setup Instructions

### macOS

1. **Install Python** (if not already installed):
   ```bash
   # Using Homebrew (recommended)
   brew install python3
   
   # Verify installation
   python3 --version
   ```

2. **Create a virtual environment**:
   ```bash
   # Navigate to the project directory
   cd web-scraping-tutorial
   
   # Create virtual environment
   python3 -m venv venv
   
   # Activate virtual environment
   source venv/bin/activate
   ```

3. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

### Windows

1. **Install Python** (if not already installed):
   - Download Python from [python.org](https://www.python.org/downloads/)
   - Run the installer and **check "Add Python to PATH"**
   - Verify installation:
     ```cmd
     python --version
     ```

2. **Create a virtual environment**:
   ```cmd
   # Navigate to the project directory
   cd web-scraping-tutorial
   
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   venv\Scripts\activate
   ```

3. **Install required packages**:
   ```cmd
   pip install -r requirements.txt
   ```

### Linux

1. **Install Python** (if not already installed):
   ```bash
   # Ubuntu/Debian
   sudo apt update
   sudo apt install python3 python3-pip python3-venv
   
   # Fedora
   sudo dnf install python3 python3-pip
   
   # Arch Linux
   sudo pacman -S python python-pip
   
   # Verify installation
   python3 --version
   ```

2. **Create a virtual environment**:
   ```bash
   # Navigate to the project directory
   cd web-scraping-tutorial
   
   # Create virtual environment
   python3 -m venv venv
   
   # Activate virtual environment
   source venv/bin/activate
   ```

3. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Hello World Tutorial

Once you have completed the setup, run the hello world script:

**macOS/Linux:**
```bash
python3 hello_world.py
```

**Windows:**
```cmd
python hello_world.py
```

### Expected Output

You should see output similar to:
```
==================================================
Hello World - Web Scraping Tutorial
==================================================

1. Making a simple HTTP request...
   Status Code: 200
   Content Length: XXXX bytes
   ✓ Request successful!

2. Parsing HTML content...
   Page Title: Herman Melville - Moby-Dick
   First Heading: Herman Melville - Moby-Dick
   ✓ Parsing successful!

3. Extracting all paragraphs...
   Found X paragraph(s)
   ...

==================================================
Tutorial complete! All packages are working correctly.
==================================================
```

## What You'll Learn

This tutorial will teach you:

1. **Basic HTTP Requests**: How to fetch web pages using the `requests` library
2. **HTML Parsing**: How to parse HTML content using `BeautifulSoup4`
3. **Data Extraction**: How to extract specific information from web pages
4. **Best Practices**: Proper error handling and timeout management

## Required Packages

The tutorial uses the following Python packages (defined in `requirements.txt`):

- **requests** (≥2.31.0): For making HTTP requests
- **beautifulsoup4** (≥4.12.0): For parsing HTML/XML documents
- **lxml** (≥4.9.0): Fast XML and HTML parser
- **selenium** (≥4.15.0): For advanced scraping with JavaScript support
- **pandas** (≥2.1.0): For data processing and analysis
- **pytest** (≥7.4.0): For testing (optional)

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Make sure you activated your virtual environment and installed all requirements
   ```bash
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

2. **Connection errors**: Check your internet connection and firewall settings

3. **Permission errors on Linux**: You may need to use `sudo` for system-wide package installation (not recommended; use virtual environments instead)

## Next Steps

After completing the hello world tutorial, you can:
- Explore more complex web scraping scenarios
- Learn about handling JavaScript-heavy websites with Selenium
- Study API interactions and data storage
- Practice ethical web scraping and respect robots.txt

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
