import time
import pytest
from selenium import webdriver
from pages.carriers_page import CarriersPage


# This is a test file. I used a Pytest framework to implement the task.
# With the help of pytest, I wrote a function that controls the chrome driver.
# I also prepared the parameterization of the inputs for the test.
# The test selects a department by name, then count the number of available jobs
# and compare this value with expected number of vacancies from this department from inputs

# Initialization of chrome driver
@pytest.fixture()
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


# Inputs for test - name of department and an expected number of vacancies
@pytest.mark.parametrize("department, expected_number_of_vacancies", [
    ("Quality Assurance", 10),
    ("Research and Development", 6),
    ("Product Management", 4),
    ("Corporate Technology", 4),
    ("Technical Customer Support", 1)
])
# Test body
def test_number_of_vacancies(driver, department, expected_number_of_vacancies):
    carriers_page = CarriersPage(driver)
    carriers_page.open_carriers_page("https://cz.careers.veeam.com/vacancies")
    carriers_page.choose_department(department)
    carriers_page.count_number_of_vacancies()
    carriers_page.assert_number_of_vacancies(expected_number_of_vacancies)
    time.sleep(5)
