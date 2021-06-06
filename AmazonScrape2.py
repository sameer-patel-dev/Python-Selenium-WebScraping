from selenium import webdriver
from selenium.webdriver.common.by import By
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


outerDiv = driver.find_elements_by_xpath('//div[contains(@data-cel-widget,"search_result_")]')

for innerDiv in outerDiv:
	try:
		product = innerDiv.find_element_by_tag_name("h2").find_element_by_tag_name("a").find_element_by_tag_name("span")
		review = innerDiv.find_element_by_class_name("a-size-base")
		rating = innerDiv.find_element_by_class_name("a-icon-alt")
	
		print("Product: ", product.text)
		print("Review: ", review.text)
		print("Rating: ", rating.text)
	except:
		pass
	print("-------------------------------------------------------------------------------------")
	

driver.close()