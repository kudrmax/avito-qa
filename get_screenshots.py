from playwright.sync_api import sync_playwright
import os


def get_screenshots(test_case_id):
    """
    Функция, которая делает скриншоты для тесткейсов из файла TESTCASES.md

    Parameters:
    test_case_id: номер тексткейса из файла TESTCASES.md
    """
    url = 'https://www.avito.ru/avito-care/eco-impact'
    output_dir = 'output'
    test_case_selector = {
        # словарь для получения индеска элемента нужного тесткейса в селекторе '.desktop-impact-items-F7T6E'
        1: 1,
        2: 3,
        3: 5,
    }

    os.makedirs(output_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        page.wait_for_selector('.desktop-impact-items-F7T6E')
        elements = page.query_selector_all('.desktop-impact-item-eeQO3')

        elements[test_case_selector[test_case_id]].screenshot(path=f'{output_dir}/{test_case_id}.png')

        browser.close()
