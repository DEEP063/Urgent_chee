@echo off
echo Activating virtual environment...
call .venv\Scripts\activate.bat
python -m unittest LinearDemo.py
deactivate