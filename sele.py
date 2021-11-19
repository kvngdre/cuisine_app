# Importing Dependencies
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

web_link = 'https://www.tred.com/'
driver_path = 'geckodriver.exe'  # Path to the geckodriver on my computer.
options = Options()
options.page_load_strategy = 'normal'
search_radius = None
zip_code = None

while search_radius is None:
    # request and validate user input for radius.
    try:
        search_radius = int(input('Please enter the search radius in miles: ').strip())
    except ValueError:
        print('Invalid!. Please enter a number for the search radius.')
    else:
        while search_radius % 5 != 0:
            search_radius += 1
        print('Perfect!')

# This is to set the search radius variable to be a multiple of 25
while search_radius % 25 != 0:
    search_radius += 1

while zip_code is None:
    # request and validate user input for zip code.
    try:
        zip_code = input('Now enter the zip code: ').strip()
        if len(zip_code) != 5:
            zip_code = None
            raise ValueError
        zip_code = int(zip_code)
    except ValueError:
        print('Sorry That is not a valid US Zip code ')
    else:
        print('Great!')

driver = webdriver.Firefox(executable_path=driver_path, options=options)
wait = WebDriverWait(driver, timeout=10)
driver.get(url=web_link)

# This is to ensure we don't try scraping the wrong webpage
assert driver.title == "TRED | The New Way To Sell Your Car | Get 30% Over Trade-In", 'Wrong Link'

# TO navigate to "Search Cars" web page.
wait.until(ec.presence_of_element_located((By.LINK_TEXT, 'SEARCH CARS')))
driver.find_element(By.LINK_TEXT, 'SEARCH CARS').click()

# Imputing the radius value in the form field.
wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'form-control')))
radius = driver.find_element(By.CLASS_NAME, 'form-control')
drop_down = Select(radius)
if search_radius <= 25:
    drop_down.select_by_value('25')
elif search_radius > 500:
    drop_down.select_by_value('500+')
else:
    drop_down.select_by_value(str(search_radius))

# Imputing the zip code in the form field
enter_zip = driver.find_element(By.XPATH, "//div[@class='form-group inline zip']/input")
enter_zip.send_keys(zip_code)

scroll_wait_time = 2  # in seconds
current_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down page for more results if any
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # Wait for images to load
    time.sleep(scroll_wait_time)

    new_height = driver.execute_script("return document.body.scrollHeight")
    time.sleep(scroll_wait_time)

    if new_height == current_height:
        # check to see if at end of page
        break
    current_height = new_height

driver.quit()
