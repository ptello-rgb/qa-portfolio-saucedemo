# Portafolio QA – Automatización UI SauceDemo

Este proyecto forma parte de mi portafolio de QA Automation.  
Demuestra un flujo básico de automatización de pruebas UI para una aplicación demo de e-commerce usando Python, Playwright y pytest.

## aplicación bajo prueba

- Aplicación: SauceDemo
- URL: https://www.saucedemo.com/
- Tipo: aplicación web demo de e-commerce

## objetivo del proyecto

El objetivo de este proyecto es demostrar cómo escenarios funcionales de prueba pueden convertirse en tests automatizados de UI.

La automatización cubre un flujo básico end-to-end, desde login hasta checkout, usando una suite estructurada con pytest.

## alcance cubierto

- Login válido
- Login inválido
- Validación de página de inventario
- Agregar producto al carrito
- Navegación al carrito
- Paso de información de checkout

## stack técnico

- Python
- pytest
- Playwright
- pytest-html
- Chromium

## estructura del proyecto

```text
saucedemo/
├─ tests/
│  ├─ conftest.py
│  ├─ test_login.py
│  ├─ test_inventory.py
│  ├─ test_cart.py
│  └─ test_checkout.py
│
├─ docs/
│  ├─ requirements.md
│  ├─ test-cases.md
│  ├─ test-data.md
│  ├─ test-execution.md
│  └─ bugs.md
│
├─ cheatsheets/
│  └─ commands.md
│
├─ reports/
│  └─ report.html
│
├─ README.md
├─ README.es.md
├─ requirements.txt
├─ pytest.ini
└─ .gitignore
```

## lo que implementé

- Definí requisitos funcionales como base de prueba
- Diseñé casos de prueba a partir del comportamiento esperado de la aplicación
- Automaticé flujos principales de UI usando Playwright
- Usé pytest como test runner
- Creé fixtures reutilizables en `conftest.py`
- Agregué assertions para validar resultados esperados
- Generé un reporte HTML de ejecución de tests
- Organicé documentación y artefactos de prueba para revisión de portafolio

## cómo ejecutar los tests

Instalar dependencias:

```bash
python -m pip install -r requirements.txt
```

Instalar navegadores de Playwright:

```bash
python -m playwright install
```

Ejecutar todos los tests:

```bash
python -m pytest -v
```

Generar reporte HTML:

```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

El reporte se generará en:

```text
reports/report.html
```

## estado actual

Este es un proyecto básico y educativo de automatización, enfocado en comprender los fundamentos de QA Automation.

La suite actual cubre un conjunto pequeño pero completo de flujos críticos de UI.  
No busca entregar cobertura completa de toda la aplicación.

## último resultado de ejecución

- Total tests: 5
- Passed: 5
- Failed: 0
- HTML report: `reports/report.html`

## habilidades demostradas

- Automatización funcional de UI
- Diseño de casos de prueba
- Análisis de requisitos
- Ejecución de tests con pytest
- Automatización de navegador con Playwright
- Uso de fixtures
- Reporte HTML de ejecución
- Regresión básica
- Estructura de documentación QA