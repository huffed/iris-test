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
    echo Input Commit Message:
    set /p commit_message=
    echo %commit_message%
    if not "%commit_message%"=="" (
        cls
    ) else (
        cls
        echo %title%
        echo.
        echo Invalid commit message input
        timeout /t 5
      )
) else (
    if "%pushyn%"=="y" (
    echo Input Commit Message:
    set /p commit_message=
    echo %commit_message%
    if not "%commit_message%"=="" (
        cls
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
        ) else (
            echo This is not a valid input.
            goto:end
          )
      )
  )
pause