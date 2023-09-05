from screens.driver import setup_webdriver
from pages.termo import Termo
from utils.words import Words
import time


def main():
    words = Words(r"data\Palavras.xlsx")
    words.filter_by_size(5)

    driver = setup_webdriver()
    termo = Termo(driver)
    termo.open("https://term.ooo/")

    for i in range(0, 6):
        termo.input_word(words.new_word(), i)
        table_result, count_right = termo.output_result(i)
        if count_right == 5:
            break
        words.filter_by_class(table_result)

    time.sleep(5)
    driver.close()


if __name__ == "__main__":
    main()
