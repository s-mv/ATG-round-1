from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

# some selectors
CONTAINER = ".s-main-slot.s-result-list.s-search-results"
ITEM = '.s-result-item[data-component-type="s-search-result"]:not(.AdHolder)'

NAME_SELECTOR = '[data-cy="title-recipe"]'
PRICE_SELECTOR = ".a-price-whole"
RATING_SELECTOR = '[data-a-popover*="average-customer-review"]'
UNAVAILABLE_SELECTOR = '[aria-label="Currently unavailable."]'

MERCHANT_SELECTOR = "#merchant-info a"


# RETURNS: an array of objects with relevant information
# i.e. Product Name, Price, Rating, Seller Name (if in stock)
def scrape(link: str):
    output = []

    options = webdriver.FirefoxOptions()
    # options.add_argument("-headless")

    driver = webdriver.Firefox(options=options)

    driver.get(link)
    # since the container is dynamically loaded we have to wait
    container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, CONTAINER))
    )

    # sleep for some seconds so the container's contents are loaded
    time.sleep(3)

    inside = container.get_attribute("innerHTML")

    # bs4 takes over from here for scraping (for some time)
    soup = BeautifulSoup(inside, "html.parser")

    item_elements = soup.select(ITEM)

    for item in item_elements:
        # regex employed in finding the rating
        # this is due to rating being in the form:
        # "Rating: _ out of 5 stars"
        rating = float(
            re.search(
                "(.*) out of 5 stars", item.select_one(RATING_SELECTOR).text
            ).groups()[0]
        )
        # object that will be appended to `output`
        obj = {
            "Name": item.select_one(NAME_SELECTOR).text,
            "Price": item.select_one(PRICE_SELECTOR).text,
            "Rating": rating,
            "Seller": None,
        }

        # using selenium again here
        # in order to get the name of the seller
        # (which isn't displayed in the listing page)

        if item.select_one(UNAVAILABLE_SELECTOR) != None:
            output.append(obj)
            continue
        # ...otherwise

        next_link = item.select_one(NAME_SELECTOR).select_one("a")["href"]
        driver.get(f"https://amazon.in{next_link}")

        # same as before, for the same reasons
        merchant_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#merchant-info a"))
        )
        # this time not sleeping is okay since we aren't aiming for a container
        obj["Seller"] = merchant_element.get_attribute("innerText")
        output.append(obj)
        print(obj)

    # finally quit the driver
    driver.quit()

    return output
