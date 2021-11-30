@echo off
title Iris - Terminal
set title=[94mIris - Terminal[0m
echo %title%
echo.
echo Pushing to GitHub? Y/N
set /p pushyn=
cls
echo %title%
echo.
if "%pushyn%"=="Y" (
	git add .
	echo Input Commit Message:
	set /p commit_message=Input Commit Message
	cls
	echo %title%
	echo.
	git commit -m "%commit_message%"
	git remote remove origin
	git remote add origin https://github.com/xspo-oky/Iris
	git fetch
	git branch -d master
	git push origin main
	git pull origin main
	pause
	cls
	echo %title%
	echo.
	python index.py
	) else (
			if "%pushyn%"=="y" (
				git add .
				echo Input Commit Message:
				set /p commit_message=
				cls
				echo %title%
				echo.
				sleep 0.5
        			echo %commit_message%
				git commit -m "%commit_message%"
				git remote remove origin
				git remote add origin https://github.com/xspo-oky/iris-test
				git fetch
        			git checkout main
				git push origin main
				git pull origin main
				pause
				cls
				echo %title%
				echo.
				python index.py
			) else (
					if "%pushyn%"=="N" (
						cls
						echo %title%
						echo.
						python index.py
					) else (
							if "%pushyn%"=="n" (
								cls
								echo %title%
								echo.
								python index.py
							) else (
									echo This is not a valid input.
									goto:end
									)
							)
					)
			)
pause
