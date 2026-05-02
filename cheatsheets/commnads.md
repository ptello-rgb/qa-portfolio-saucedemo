# commands cheat sheet

## pip

# instalar pytest en el entorno actual
python -m pip install pytest

# instalar pytest-html para generar reportes html
python -m pip install pytest-html

# instalar dependencias desde requirements.txt
python -m pip install -r requirements.txt

## pytest

# revisar que pytest quedó instalado
pytest --version

# ejecutar todos los tests encontrados por pytest
python -m pytest -v

# ejecutar tests desde la carpeta tests
python -m pytest tests -v

# ejecutar solo un archivo de tests
python -m pytest tests/test_login.py -v

# ejecutar tests y generar reporte html
python -m pytest -v --html=reports/report.html --self-contained-html

## playwright

# revisar la versión instalada de playwright
python -m pip show playwright

# instalar navegadores necesarios para playwright
python -m playwright install

## git

# revisar si git está instalado y disponible en la terminal
git --version

# instalar git usando winget en windows
winget install --id Git.Git -e --source winget

# inicializar git en la carpeta local del proyecto
git init

# conectar el repo local con el repo remoto de github
git remote add origin https://github.com/ptello-rgb/qa-portfolio-saucedemo.git

# corregir o actualizar la url del repo remoto
git remote set-url origin https://github.com/ptello-rgb/qa-portfolio-saucedemo.git

# definir la rama principal como main
git branch -M main

# revisar el estado del repo local
git status

# preparar todos los cambios para commit
git add .

# guardar los cambios preparados en un commit local
git commit -m "Add SauceDemo UI automation project"

# subir commits locales a github
git push -u origin main

# subir forzando el remoto para reemplazar su contenido
git push -u origin main --force

# descargar un repo desde github a una carpeta local
git clone https://github.com/ptello-rgb/qa-portfolio-saucedemo.git saucedemo-repo

