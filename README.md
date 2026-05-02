# QA Portfolio – SauceDemo UI Automation

This project is part of my QA Automation portfolio.  
It demonstrates a basic automated UI testing workflow for a demo e-commerce web application using Python, Playwright, and pytest.

## Application Under Test

- Application: SauceDemo
- URL: https://www.saucedemo.com/
- Type: Web e-commerce demo application

## Project Objective

The objective of this project is to demonstrate how functional test scenarios can be converted into automated UI tests.

The automation covers a basic end-to-end user flow, from login to checkout, using a structured pytest test suite.

## Scope Covered

- Valid login
- Invalid login
- Inventory page validation
- Add product to cart
- Cart navigation
- Checkout information step

## Tech Stack

- Python
- pytest
- Playwright
- pytest-html
- Chromium

## Project Structure

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

## What I Implemented

- Defined functional requirements as the test basis
- Designed test cases from expected application behavior
- Automated core UI flows using Playwright
- Used pytest as the test runner
- Created reusable fixtures in `conftest.py`
- Added assertions to validate expected outcomes
- Generated an HTML test execution report
- Organized documentation and test artifacts for portfolio review

## How to Run the Tests

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Install Playwright browsers:

```bash
python -m playwright install
```

Run all tests:

```bash
python -m pytest -v
```

Generate HTML report:

```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

The report will be generated at:

```text
reports/report.html
```

## Current Status

This is a basic educational automation project focused on understanding the fundamentals of QA automation.

The current suite covers a small but complete set of critical UI flows.  
It does not aim to provide full test coverage of the entire application.

## Latest Execution Result

- Total tests: 5
- Passed: 5
- Failed: 0
- HTML report: `reports/report.html`

## Skills Demonstrated

- Functional UI test automation
- Test case design
- Requirement analysis
- pytest test execution
- Playwright browser automation
- Fixture usage
- HTML test reporting
- Basic regression testing
- QA documentation structure