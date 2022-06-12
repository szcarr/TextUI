set file="tmp.txt"
del /q %file%
dir /Ad /s /b *__pycache__ > %file%
FOR /F %%i IN (%file%) DO echo "HEI"
del /q %file%