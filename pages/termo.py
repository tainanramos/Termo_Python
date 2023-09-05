from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unidecode import unidecode
import pandas as pd
import time


class Termo:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)
        try:
            wc_modal = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "wc-modal")))
            wc_modal.click()
        except:
            pass

    def close(self):
        self.driver.close()

    def input_word(self, word, termo_row):
        java_script = f'return document.querySelector("#board0").shadowRoot.querySelector("#hold > wc-row:nth-child({termo_row + 1})").shadowRoot.querySelector("div[lid=\'0\']") '
        wc_row = self.driver.execute_script(java_script)
        wc_row.send_keys(word + "\ue007")
        time.sleep(3)

    def output_result(self, termo_row):
        table_result = pd.DataFrame({"POSITION": [], "CLASS": [], "LETTER": []})
        count_right = 0
        for i in range(0, 5):
            java_script = f'return document.querySelector("#board0").shadowRoot.querySelector("#hold > wc-row:nth-child({termo_row + 1})").shadowRoot.querySelector("div[lid=\'{i}\']") '
            wc_row = self.driver.execute_script(java_script)
            class_termo = wc_row.get_attribute("class")
            if "wrong" in class_termo:
                table_temp = pd.DataFrame(
                    {"POSITION": [i], "CLASS": ["wrong"], "LETTER": [unidecode(str(wc_row.text)).lower()]})
                table_result = pd.concat([table_result, table_temp])
            elif "place" in class_termo:
                table_temp = pd.DataFrame(
                    {"POSITION": [i], "CLASS": ["place"], "LETTER": [unidecode(str(wc_row.text)).lower()]})
                table_result = pd.concat([table_result, table_temp])
            elif "right" in class_termo:
                table_temp = pd.DataFrame(
                    {"POSITION": [i], "CLASS": ["right"], "LETTER": [unidecode(str(wc_row.text)).lower()]})
                table_result = pd.concat([table_result, table_temp])
                count_right += 1
        return table_result, count_right
