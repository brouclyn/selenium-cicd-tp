from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def load_page(self):
        file_path = (Path(__file__).resolve().parent.parent / "src" / "index.html").as_posix()
        self.driver.get(f"file:///{file_path}")

    def first_number_input(self):
        return self.driver.find_element(By.ID, "num1")

    def second_number_input(self):
        return self.driver.find_element(By.ID, "num2")

    def operation_select(self):
        return Select(self.driver.find_element(By.ID, "operation"))

    def calculate_button(self):
        return self.driver.find_element(By.ID, "calculate")

    def enter_first_number(self, value):
        el = self.first_number_input()
        el.clear()
        el.send_keys(str(value))

    def enter_second_number(self, value):
        el = self.second_number_input()
        el.clear()
        el.send_keys(str(value))

    def select_operation(self, operation):
        self.operation_select().select_by_value(operation)

    def click_calculate(self):
        self.calculate_button().click()

    def get_result_text(self):
        result = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))
        )
        return result.text

    def wait_until_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "calculator"))
        )

    def calculate(self, operation, num1, num2):
        self.enter_first_number(num1)
        self.enter_second_number(num2)
        self.select_operation(operation)
        self.click_calculate()
        return self.get_result_text()