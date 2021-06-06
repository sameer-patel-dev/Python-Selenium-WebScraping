from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import html
from time import sleep


driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver.exe')

for page_nb in range(1,5):
	driver.get('https://www.amazon.in/s?k=keyboard&page='+str(page_nb))

	sleep(1)

	tree = html.fromstring(driver.page_source)

	for product_tree in tree.xpath('//div[contains(@data-cel-widget,"search_result_")]'):
		title = product_tree.xpath('.//span[@class="a-size-medium a-color-base a-text-normal"]/text()')
		reviews = product_tree.xpath('.//span[@class="a-size-base"]/text()')
		price = product_tree.xpath('.//span[@class="a-offscreen"]/text()')

		try:
			print("Product: ", title[0])
			print("Reviews: ", reviews[0])
			print("Discounted Price: ", price[0])
			print("Actual Price: ", price[1])
			print("----------------------------------------------------------------")
		except:
			pass

	print("\n\n\n\n")

driver.close()