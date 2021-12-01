@echo off
title Iris - Terminal
set title=[94mIris - Terminal[0m
echo %title%
echo.
echo Pushing to GitHub? (Y/N)
set /p pushyn=
cls
echo %title%
echo.
if "%pushyn%"=="Y" (
    git add .
    echo Input Commit Message:
    set /p commit_message=
    echo %commit_message%
    if not "%commit_message%"=="" (
        echo %commit_message%
        pause
        cls
        echo %title%
        echo.
        git commit -m "%commit_message%"
        git remote remove origin
        git remote add origin https://github.com/xspo-oky/iris-test
        git fetch
        echo GitHub Repository Branches:
        git branch
        echo.
        echo Which branch do you want to push to?
        set /p branch=
        git push origin "%branch%"
        timeout /t 5
        cls
        echo %title%
        python index.py
    ) else (
        cls
        echo %title%
        echo.
        echo Invalid commit message input
        timeout /t 5
      )
) else (
    if "%pushyn%"=="y" (
    git add .
    echo Input Commit Message:
    set /p commit_message=
    echo %commit_message%
    if not "%commit_message%"=="" (
        echo %commit_message%
        pause
        cls
        echo %title%
        echo.
        git commit -m "%commit_message%"
        git remote remove origin
        git remote add origin https://github.com/xspo-oky/iris-test
        git fetch
        echo GitHub Repository Branches:
        git branch
        echo.
        echo Which branch do you want to push to?
        set /p branch=
        git push origin "%branch%"
        timeout /t 5
        cls
        echo %title%
        python index.py
    ) else (
        cls
        echo %title%
        echo.
        echo Invalid commit message input
        timeout /t 5
      )
    ) else (
        if "%pushyn%"=="n" (
            cls
            echo %title%
            python index.py
        ) else (
            echo This is not a valid input.
            goto:end
          )
      )
  )
pause