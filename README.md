# playwright-web-python

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Reporting](#reporting)
- [Who to Contact](#who-to-contact)

## Overview

The **Playwright UI Automation Boilerplate** is designed for **end-to-end UI testing** using [Playwright](https://playwright.dev/python/) and `pytest`. It provides a **scalable and maintainable** framework using the **Page Object Model (POM)** and supports CI/CD execution with **GitHub Actions**.

## Features

- **Page Object Model (POM)**: Enhances maintainability and reusability.
- **Reusable UI Actions**: Simplifies interaction with UI elements.
- **Logging Support**: Uses Python’s `logging` module for better debugging.
- **Parameterized Tests**: Supports `pytest.mark.parametrize` for flexible testing.
- **Tag-Based Execution**: Run tests selectively using tags (`login`, `sorting`, etc.).
- **GitHub Actions Integration**: CI/CD pipeline to run tests automatically.
- **Allure Reporting**: Generates interactive test reports.

## Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/playwright-ui-boilerplate.git
cd playwright-ui-boilerplate
```

### **2️⃣ Create and Activate a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
playwright install
```

### **4️⃣ Set Up Environment Variables**  
Create a `.env` file in the root directory and add:
```
LOGIN_URL=https://your-login-page.com
USERNAME=your_username
PASSWORD=your_password
```

---

## Running Tests

### **Run All Tests**
```bash
pytest
```

### **Run Login Tests Only**
```bash
pytest -m login
```

### **Run Sorting Tests Only**
```bash
pytest -m sorting
```

### **Running Tests with Bash Script**
Use the runtest.sh script to execute tests and generate an Allure report automatically.
```bash
./run_tests.sh
```


### **Run Tests in CI/CD (GitHub Actions)**
1. Navigate to the **Actions** tab in GitHub.
2. Select **Playwright UI Boilerplate** workflow.
3. Click **"Run workflow"** and select a test category (`all`, `login`, or `sorting`).

---

## Reporting

### **Generate Allure Report**
After running tests, generate and view the report using:
```bash
allure serve allure-results
```

---

## Who to Contact?

📩 **ASWANI R S**  
📧 aswanirs321@gmail.com  
🔗 [GitHub Profile](https://github.com/aswanirs23)

---



