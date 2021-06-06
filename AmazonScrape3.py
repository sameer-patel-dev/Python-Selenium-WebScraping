from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import html
from time import sleep

#Open Chrome and navigate to Amazon
driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver.exe')
driver.get("https://www.amazon.in/")
sleep(1)

#Enter what you have to search in the search box
searchBox = driver.find_element_by_id('twotabsearchtextbox')
searchBox.send_keys("keyboard")

#Press Go to search
driver.find_element_by_id('nav-search-submit-button').click()
sleep(1)

#Select a specific brand
driver.find_element_by_xpath('//*[@id="p_89/ZEBRONICS"]/span/a/span').click()
sleep(1)

tree = html.fromstring(driver.page_source)

for product_tree in tree.xpath('//div[contains(@data-cel-widget,"search_result_")]'):
	title = product_tree.xpath('.//span[@class="a-size-medium a-color-base a-text-normal"]/text()')
	reviews = product_tree.xpath('.//span[@class="a-size-base"]/text()')
	rating = product_tree.xpath('.//span[@class="a-icon-alt"]/text()')
	price = product_tree.xpath('.//span[@class="a-offscreen"]/text()')
	try:
		print("Product: ", title)
		print("Reviews: ", reviews)
		print("Rating: ", rating)
		print("Discounted Price: ", price[0])
		print("Actual Price: ", price[1])
		print("----------------------------------------------------------------")
	except:
		pass

	print("\n\n\n\n")

driver.close()