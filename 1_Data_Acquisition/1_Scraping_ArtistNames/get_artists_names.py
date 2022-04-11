from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://chartmasters.org/most-streamed-artists-ever-on-spotify/')

try:
    # get the select tag
    select = Select(driver.find_element(By.TAG_NAME,'#table_1_length > label > div > select'))
    # select by value (select All option to get all 1000 artists)
    select.select_by_value('-1')

    all_artists = [my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "table#table_1 tbody tr[role='row'] td:nth-of-type(2)")))]

    print(all_artists)

    df = pd.DataFrame(all_artists)
    df.to_csv(r'Artists.csv', index=False)

finally:
    driver.quit()
