# Remote microphone controller

Mute / unmute your PC's microphone from your phone when the daily meetings are too long and your headphones doesn't have a mute / unmute button.

This project uses `win32api` so it supports only windows computers.

### How to run

1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`.
3. Activate the virtual environment: execute `venv\Scripts\activate`.
4. Install dependencies: `pip install -r requirements.txt`.
5. Run the project: `python main.py` and fill the input, you can run the `bat` script as well that activates the venv and runs the script: `run.bat`.
6. Your local IPv4 will be printed, use it to connect from your phone on port 80.
