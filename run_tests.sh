pytest --alluredir=allure-results --clean-alluredir
allure generate allure-results -o allure-report --clean
allure serve allure-results 