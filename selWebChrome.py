import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class SelWebChrome:
    def __init__(self):
        # Initialization
        service = Service(r'C:\Program Files\Chromium\chromedriver-win64\chromedriver.exe')
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.action = ActionChains(self.driver)

        # Wait
        self.driver.implicitly_wait(7)
        self.wait = WebDriverWait(self.driver, 10)



        # Get into website
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        print(self.driver.current_url)


    def scrollDown(self, px):
        self.driver.execute_script(f"window.scrollBy(0, {px})")

    def handleButton(self):
        self.driver.find_element(By.XPATH, "//input[@value='radio2']").click()

    def handleDropdowns(self):
        # Auto Suggesst Dropdown
        self.driver.find_element(By.ID, 'autocomplete').send_keys("pol")
        countries = self.driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item-wrapper")
        for country in countries:
            if country.text == "Poland":
                country.click()
                break
        assert len(countries) <= 10

        # Static Dropdown
        dropdown = Select(self.driver.find_element(By.ID, "dropdown-class-example"))
        dropdown.select_by_visible_text("Option2")


    def handleCheckbox(self):
        counter = 1

        while counter < 4:
            checkbox = self.driver.find_element(By.ID, f"checkBoxOption{counter}")
            checkbox.click()
            counter += 1

        assert counter == 4

    def handleWindows(self):
        self.driver.find_element(By.ID, "openwindow").click()
        opened_windows = self.driver.window_handles
        print(len(opened_windows))
        self.driver.switch_to.window(opened_windows[1])
        self.driver.switch_to.window(opened_windows[0])

    def handleTabs(self):
        self.driver.find_element(By.ID, "opentab").click()
        opened_windows = self.driver.window_handles
        self.driver.switch_to.window(opened_windows[-1])
        self.driver.switch_to.window(opened_windows[0])

    def handleAlert(self):
        # Case 1, accept alert
        self.driver.find_element(By.CSS_SELECTOR, "#name").send_keys("MJ")
        self.driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
        alert = self.driver.switch_to.alert
        alertText = alert.text
        print(alertText)
        alert.accept()

        # Case 2, cancel alert
        self.driver.find_element(By.CSS_SELECTOR, "#name").send_keys("MJ")
        self.driver.find_element(By.CSS_SELECTOR, "#confirmbtn").click()
        alert = self.driver.switch_to.alert
        alertText = alert.text
        print(alertText)
        alert.dismiss()

    def handleTable(self):
        price_list = []
        prices = self.driver.find_elements(By.XPATH, "//table[@name='courses']//tr/td[3]")
        for price in prices:
            price_list.append(int(price.text))
            print(price_list)

        total_cost = sum(price_list)
        print(total_cost)

        assert total_cost == 235

    def handleMouseHover(self):
        mouse_hover = self.driver.find_element(By.ID, "mousehover")
        self.action.move_to_element(mouse_hover).perform()
        variants = self.driver.find_elements(By.XPATH, "//div[@class='mouse-hover-content']//a")
        for variant in variants:
            if variant.text == "Top":
                variant.click()
                break

    def handleFrame(self):
        # Switch to iframe
        self.driver.switch_to.frame("courses-iframe")
        self.driver.find_element(By.LINK_TEXT, "Practice").click()
        # Switch to the default content
        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scrollTo(0, 0);")



if __name__ == "__main__":

    runner = SelWebChrome()
    runner.handleButton()
    runner.handleDropdowns()
    runner.handleCheckbox()
    runner.handleTabs()
    runner.handleWindows()
    runner.handleAlert()
    runner.scrollDown(500)
    runner.handleTable()
    runner.scrollDown(500)
    runner.handleMouseHover()
    runner.scrollDown(1500)
    runner.handleFrame()


#driver.quit()



