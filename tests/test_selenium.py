import pytest
import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from calculator_page import CalculatorPage


class TestCalculator:

    @pytest.fixture(scope="class")
    def driver(self):
        """Configuration du driver pour les tests (Chrome/Firefox via env BROWSER)"""
        browser = os.getenv("BROWSER", "chrome").lower()

        if browser == "firefox":
            options = FirefoxOptions()
            if os.getenv("CI"):
                options.add_argument("-headless")

            driver = webdriver.Firefox(options=options)

        else:
            # default = chrome
            chrome_options = Options()
            if os.getenv("CI"):
                chrome_options.add_argument("--headless=new")
                chrome_options.add_argument("--no-sandbox")
                chrome_options.add_argument("--disable-dev-shm-usage")
                chrome_options.add_argument("--disable-gpu")
                chrome_options.add_argument("--window-size=1920,1080")

            driver = webdriver.Chrome(options=chrome_options)

        driver.implicitly_wait(10)
        yield driver
        driver.quit()

    @pytest.fixture
    def page(self, driver):
        page = CalculatorPage(driver)
        page.load_page()
        return page

    def test_page_loads(self, driver):
        """Test 1: Vérifier que la page se charge correctement"""
        page = CalculatorPage(driver)
        page.load_page()

        assert "Calculatrice Simple" in driver.title
        assert driver.find_element(By.ID, "num1").is_displayed()
        assert driver.find_element(By.ID, "num2").is_displayed()
        assert driver.find_element(By.ID, "operation").is_displayed()
        assert driver.find_element(By.ID, "calculate").is_displayed()

    def test_addition(self, page):
        """Test 2: Tester l'addition"""
        result_text = page.calculate("add", 10, 5)
        assert "Résultat: 15" in result_text

    def test_division_by_zero(self, page):
        """Test 3: Tester la division par zéro"""
        result_text = page.calculate("divide", 10, 0)
        assert "Erreur: Division par zéro" in result_text

    def test_all_operations(self, page):
        """Test 4: Tester toutes les opérations"""
        operations = [
            ("add", "8", "2", "10"),
            ("subtract", "8", "2", "6"),
            ("multiply", "8", "2", "16"),
            ("divide", "8", "2", "4"),
        ]

        for op, num1, num2, expected in operations:
            result_text = page.calculate(op, num1, num2)
            assert f"Résultat: {expected}" in result_text
            time.sleep(1)

    def test_page_load_time(self, driver):
        """Test 5: Mesurer le temps de chargement de la page"""
        start_time = time.time()

        page = CalculatorPage(driver)
        page.load_page()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "calculator"))
        )

        load_time = time.time() - start_time
        print(f"Temps de chargement: {load_time:.2f} secondes")
        assert load_time < 3.0, f"Page trop lente à charger: {load_time:.2f}s"

    def test_decimal_numbers(self, page):
        """Test 6: Tester avec des nombres décimaux"""
        # Essai 1 : point (format US)
        result_text = page.calculate("add", "10.5", "2.25")

        # Si résultat vide (souvent input number + locale FR), essai 2 : virgule (format FR)
        if not result_text.strip():
            result_text = page.calculate("add", "10,5", "2,25")

        assert ("12.75" in result_text) or ("12,75" in result_text), result_text


    def test_negative_numbers(self, page):
        """Test 7: Tester avec des nombres négatifs"""
        result_text = page.calculate("multiply", -8, 2)
        assert "-16" in result_text, result_text

    def test_ui_styles(self, page):
        """Test 8: Vérifier certains styles UI (couleurs, tailles)"""
        num1 = page.first_number_input()
        num2 = page.second_number_input()
        btn = page.calculate_button()

        assert num1.size["width"] >= 80 and num1.size["height"] >= 20
        assert num2.size["width"] >= 80 and num2.size["height"] >= 20
        assert btn.size["width"] >= 60 and btn.size["height"] >= 20

        btn_bg = btn.value_of_css_property("background-color")
        btn_color = btn.value_of_css_property("color")

        assert btn_bg is not None and btn_bg != "" and btn_bg != "transparent"
        assert btn_color is not None and btn_color != ""

        font_size = btn.value_of_css_property("font-size")
        assert font_size is not None and font_size != ""


if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html", "--self-contained-html"])