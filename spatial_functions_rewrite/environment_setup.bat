@echo off

REM Create virtual environment
python -m venv geocli

REM Activate the virtual environment
call geocli\Scripts\activate.bat

REM Install essential packages
pip install --upgrade pip
pip install shapely matplotlib jupyter

REM Add Jupyter kernel (optional)
python -m ipykernel install --user --name=geocli --display-name "Python (geocli)"

echo ✅ Environment created and ready: 'geocli'