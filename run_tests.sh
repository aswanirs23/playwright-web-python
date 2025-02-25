# Test Execution Script
# This script automates the process of running tests and generating reports.
# Usage: ./run_tests.sh

pytest --alluredir=allure-results --clean-alluredir
allure generate allure-results -o allure-report --clean
allure serve allure-results 