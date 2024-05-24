# KeepAlive.py

![KeepAlive Preview](preview.png)

<div style="text-align: center;">

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/Version-1.0-brightgreen.svg)](#version)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-lightgrey.svg)](#platforms)
[![Contributors](https://img.shields.io/github/contributors/oceanofanythingofficial/KeepAlive.svg)](#contributing)
[![Issues](https://img.shields.io/github/issues/oceanofanythingofficial/KeepAlive.svg)](https://github.com/oceanofanythingofficial/KeepAlive/issues)
[![Stars](https://img.shields.io/github/stars/oceanofanythingofficial/KeepAlive.svg)](https://github.com/oceanofanythingofficial/KeepAlive/stargazers)
[![Forks](https://img.shields.io/github/forks/oceanofanythingofficial/KeepAlive.svg)](https://github.com/oceanofanythingofficial/KeepAlive/network/members)
[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

</div>


KeepAlive.py is a Python script designed to prevent system sleep or screen lock by simulating mouse movements at random intervals. It utilizes the pyautogui library for controlling the mouse, as well as the threading and keyboard modules for concurrent execution and key press detection, respectively.

## Features

- **Randomized Mouse Movement**: The script generates random mouse movements within the screen boundaries at specified intervals, ensuring that the system remains active.
- **Smooth Movement**: Mouse movements are interpolated to provide smooth transitions across the screen.
- **User Interaction**: Users can start and stop the mouse movement using designated key presses ('s' to start and 'q' to stop).

## Platforms

KeepAlive.py is compatible with the following platforms:

- Windows
- Mac
- Linux

## Prerequisites

Before running KeepAlive.py, ensure that you have Python installed on your system along with the necessary dependencies:

- Python 3.x
- pyautogui
- keyboard

You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

To use KeepAlive.py, follow these steps:

1. Clone or download the KeepAlive.py script to your local system.
2. Install the required dependencies as mentioned above.
3. Run the script using the following command:

```bash
python KeepAlive.py
```

4. Once the script is running, follow the instructions displayed on the console:
   - Press 's' to start mouse smooth random movement.
   - Press 'q' to quit and stop the mouse movement.

## Contributing

Contributions to KeepAlive.py are welcome! If you encounter any bugs, have suggestions for improvements, or would like to add new features, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/oceanofanythingofficial/KeepAlive.py).

## Version

KeepAlive.py is currently on version 1.0.

## License

KeepAlive.py is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Disclaimer

This script is intended for educational and informational purposes only. Use it responsibly and at your own risk. The authors and contributors of KeepAlive.py are not responsible for any misuse or damage caused by the script.
