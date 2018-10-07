set UIFILE=%1
set UIDIR=%~dp1
set FILENAME=%~n1
set PSTNAME=%UIDIR%%FILENAME%_uis.py

call C:\Python27\Scripts\pyside-uic.exe %UIFILE% -o %PSTNAME%
