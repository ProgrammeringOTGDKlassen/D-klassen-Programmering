cd app
start chrome http://127.0.0.1:5000/
@echo off
echo Starting..
:main
python main.py
echo Restarting Webpage...
goto main



