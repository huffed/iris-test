@echo off
set NLM=^
set NL=^^^%NLM%%NLM%^%NLM%%NLM%
set /p pushyn=Pushing to GitHub? Y/N%NL%
if "%pushyn%"=="Y" (
	git add .
	set /p commit_message=Input Commit Message: 
	git commit -m "%commit_message%"
	git push origin main
	git pull origin main
	pause
	cls
	python index.py
)
if "%pushyn%"=="y" (
	git add .
	set /p commit_message=Input Commit Message: 
	git commit -m "%commit_message%"
	git push origin main
	git pull origin main
	pause
	cls
	python index.py
)
if "%pushyn%"=="N" (
	cls
	python index.py
)
if "%pushyn%"=="n" (
	cls
	python index.py
)
pause