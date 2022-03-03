from typing import *
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import traceback

DOMAIN_MAP = {
    'SG': '.sg',
    'MY': '.com.my',
    'TH': '.co.th',
    'TW': '.co.tw',
    'ID': '.co.id',
    'VN': '.vn',
    'PH': '.ph',
    'BR': '.com.br',
    'MX': '.com.mx',
    'CO': '.com.co',
    'CL': '.cl',
    'PL': '.pl',
    'ES': '.es',
    'IN': '.in',
    'AR': '.com.ar'
}

class ShopeeCrawler:
    driver: WebDriver = None

    def __init__(self, driver: WebDriver = None) -> None:
        if driver is None:
            driver = webdriver.Chrome()
        self.driver = driver
        pass
    
    def close(self) -> None:
        self.driver.close()
    
    def _get_next_page_button(self) -> WebElement:
        return self.driver.find_element(By.CLASS_NAME,'shopee-icon-button--right')
    
    def search(self, region: str, search_txt: str) -> None:
        assert region in DOMAIN_MAP
        domain = DOMAIN_MAP.get(region)
        search_txt_URLfied = urllib.parse.quote(search_txt)
        url = f'https://shopee{domain}/search?keyword={search_txt_URLfied}'
        self.driver.get(url)
    
    def next_page(self) -> None:
        next_page_btn = self._get_next_page_button()
        next_page_btn.click()
    
    def get_search_results(self) -> List[str]:
        search_result: List[WebElement] = self.driver.find_element(By.CLASS_NAME, 'shopee-search-item-result__items').find_elements(By.CLASS_NAME, 'shopee-search-item-result__item')
        links: List[str] = []
        print(search_result)
        for element in search_result:
            try:
                self.driver.execute_script('arguments[0].scrollIntoView(true)', element)
                link_element: WebElement = element.find_element(By.TAG_NAME, 'a')
                link = link_element.get_attribute('href')
                links.append(link)
            except Exception as e:
                print('Error occured when trying to get link')
                traceback.print_exc()
        
        return links
