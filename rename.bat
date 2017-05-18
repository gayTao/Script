@echo off&setlocal EnableDelayedExpansion 
set a=1 
for /f "delims=" %%i in ('dir /b *.wav') do ( 
if not "%%~ni"=="%~n0" ( 
if !a! LSS 10 (ren "%%i" "surprised0!a!.wav") else ren "%%i" "surprised!a!.wav" 
set/a a+=1 
) 
)