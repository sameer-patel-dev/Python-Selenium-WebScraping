from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver.exe')
driver.get("https://www.imdb.com/search/title/")

element = driver.find_element_by_id("groups-1")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element.click()
sleep(1)

driver.find_element_by_xpath("//button[contains(text(),'Search')]").click()

allDiv = driver.find_elements_by_xpath("//body/div[@id='wrapper']/div[@id='root']/div[@id='pagecontent']/div[@id='content-2-wide']/div[@id='main']/div[1]/div[3]/div[1]/div")

for i in range(len(allDiv)):
	print("Movie: ", allDiv[i].find_element_by_tag_name("h3").find_element_by_tag_name("a").text)
	print("Year: ", allDiv[i].find_element_by_tag_name("h3").text.split()[-1])
	print("Genre: ", allDiv[i].find_element_by_xpath(".//p//span[@class='genre']").text)
	print("Rating: ", allDiv[i].find_element_by_xpath(".//div[@class='ratings-bar']//div").get_attribute("data-value"))
	lst =  allDiv[i].find_elements_by_xpath(".//p[3]//a")
	for i in range(len(lst)):
		print("Crew No "+str(i+1)+": ", lst[i].text)

	print()



driver.close()


