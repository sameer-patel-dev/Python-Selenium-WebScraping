from selenium import webdriver 
from time import sleep

# Loading the driver and getting the URL
driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver.exe')
driver.get("https://www.flipkart.com/")


# Closing the POP UP from Flipkart
try:
	driver.find_element_by_xpath("//button[contains(text(),'✕')]").click()
except:
	pass
sleep(1)


# Pushing Samsung to the search bar
driver.find_element_by_xpath("//body/div[@id='container']/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/input[1]").send_keys("Samsung Galaxy S10")
driver.find_element_by_tag_name("button").click()
sleep(1)


# Cicking Mobile 
driver.find_element_by_xpath("//body/div[@id='container']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[3]/div[1]/a[1]").click()
sleep(1)


# Clicking Flipkart Assured
driver.find_element_by_xpath("//body/div[@id='container']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/section[3]/label[1]/div[2]/div[1]/img[1]").click();
sleep(1)

# Clickign on Brand Samsung
driver.find_element_by_xpath("//body/div[@id='container']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/section[5]/div[2]/div[1]/div[1]/div[1]/label[1]/div[2]").click();
sleep(1);


# Sorting the entries from High to Low
driver.find_element_by_xpath("//div[contains(text(),'Price -- High to Low')]").click()
sleep(1)

# Taking entire divs from the page
allMobiles = driver.find_elements_by_xpath("//body/div[@id='container']/div[1]/div[3]/div[1]/div[2]/div")


allItems = []

# looping through each div
for i in range(1,len(allMobiles)):
	try:
		linkToMobile = allMobiles[i].find_element_by_tag_name("a")

		mobileTitle = linkToMobile.find_element_by_xpath("./div[2]/div[1]/div[1]").text
		mobilePrice = linkToMobile.find_element_by_xpath("./div[2]/div[2]/div[1]/div/div").text
		mobileLink = linkToMobile.get_attribute("href")

		# Adding each mobile to the list
		item  = []
		item = [mobileTitle, mobilePrice, mobileLink]
		allItems.append(item) 

	except:
		pass

# Printing each item from the list
for item in allItems:
	print("Name: ", item[0])
	print("Price: ", item[1])
	print("Link: ", item[2])

	print("\n\n")


driver.close()

