from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from typing import NamedTuple


class Locator(NamedTuple):
    """ Locator object """
    by: str
    selector: str


class TextInput:
    """ TextInput object """

    def __init__(self, root_selector, driver):
        self.root_selector = f'input{root_selector}'
        self._driver = driver
        self._locator = Locator(By.CSS_SELECTOR, self.root_selector)

    @property
    def value(self) -> str:
        """
        returns the current value in input
        :return: str
        """
        element = self._driver.find_element(self._locator)
        return self._driver.execute_script(f"return arguments[0].value", element)

    def enter_text(self, text: str) -> None:
        """ enters text to element """
        element = self._driver.find_element(self._locator)
        element.clear()
        element.send_keys(text)

    def clear_text(self) -> None:
        """
        clears text
        :return:None
        """
        element = self._driver.find_element(self._locator)
        element.clear()


class Button:
    """ Button object """

    def __init__(self, root_selector, driver):
        self.root_selector = f'{root_selector}'
        self._driver = driver
        self._locator = Locator(By.CSS_SELECTOR, self.root_selector)

    @property
    def text(self) -> str:
        return self._driver.get_text(self._locator)

    def click(self) -> None:
        self._driver.click(self._locator)


class DropDown:
    """ DropDown Object """

    def __init__(self, root_selector, driver):
        self.root_selector = f'.select_container {root_selector}'
        self._driver = driver
        self._locator = Locator(By.CSS_SELECTOR, self.root_selector)

    @property
    def options(self) -> list:
        element = self._driver.find_element(self._locator)
        return Select(element).options

    def select_by_value(self, value: str) -> None:
        element = self._driver.find_element(self._locator)
        Select(element).select_by_value(value)

    def select_by_index(self, index: int) -> None:
        element = self._driver.find_element(self._locator)
        Select(element).select_by_index(index)
