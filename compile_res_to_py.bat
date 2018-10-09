set UIFILE=%1
set UIDIR=%~dp1
set FILENAME=%~n1
set PSTNAME=%UIDIR%%FILENAME%_rc.py

call C:\Python27\Lib\site-packages\PySide\pyside-rcc.exe %UIFILE% -o %PSTNAME%
