import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


# I used the design template page object to solve the given task.
# The given file contains locators and also functional methods that are used by the test file

class CarriersPage:

    # Locators
    def __init__(self, driver):
        self.driver = driver
        self.carriers_page_header = (By.XPATH, "//h1[contains(text(),'Build your career at Veeam')]")
        self.dropBox_menu = (By.ID, "sl")
        self.vacancies = "//div[@class='h-100 d-flex flex-column']//h3"

    # Method to open page
    def open_carriers_page(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.carriers_page_header))

    # Method to choose department
    def choose_department(self, department):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.dropBox_menu)).click()
        time.sleep(2)
        actual_department = self.driver.find_elements(By.LINK_TEXT, department)
        actual_department[0].click()
        time.sleep(2)

    # Method to count number of vacancies
    def count_number_of_vacancies(self):
        WebDriverWait(self.driver, 20).until(ec.presence_of_element_located((By.XPATH, self.vacancies)))
        count_of_jobs = len(self.driver.find_elements(By.XPATH, self.vacancies))
        return count_of_jobs

    # Method to assert number of found vacancies and number of expected vacancies for this department
    def assert_number_of_vacancies(self, expected_number_of_vacancies):
        actual_number = self.count_number_of_vacancies()
        assert actual_number == expected_number_of_vacancies
