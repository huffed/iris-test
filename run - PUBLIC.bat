@echo off
echo Pushing to GitHub? Y/N
set /p pushyn=
cls
if "%pushyn%"=="Y" (
	git add .
	echo Input Commit Message:
	set /p commit_message=
	git commit -m "%commit_message%"
	git remote remove origin
	git remote add origin https://github.com/xspo-oky/Iris
	git fetch
	git branch -d master
	git push origin main
	git pull origin main
	pause
	cls
	python index.py
	) else (
			if "%pushyn%"=="y" (
				git add .
				echo Input Commit Message:
				set /p commit_message=
				git commit -m "%commit_message%"
				git remote remove origin
				git remote add origin https://github.com/xspo-oky/Iris
				git fetch
				git branch -d master
				git push origin main
				git pull origin main
				pause
				python index.py
			) else (
					if "%pushyn%"=="N" (
						cls
						python index.py
					) else (
							if "%pushyn%"=="n" (
								cls
								python index.py
							) else (
									echo This is not a valid input.
									pause
									)
							)
					)
			)
pause
