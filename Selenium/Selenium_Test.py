from selenium import webdriver

#Create new instance of the web driver
driver = webdriver.Chrome()
#Open Demo Website
driver.get("http://www.seleniumeasy.com/test/basic-first-form-demo.html")
print(driver.title)

#Login to Website : Enter User Id and Password and Sign-In

strText = "This is demo script in Python"
driver.find_element_by_id("user-message").send_keys(strText)
driver.find_element_by_xpath("//*[@class='btn btn-default' and contains(text(),'Show Message')]").click()

strDisplayMessage = driver.find_element_by_id("display").text

print(strDisplayMessage)
assert strDisplayMessage == strText, "Message not displayed. Houston there is a problem"
print("Test-1 PASSED")

intVal1=5
intVal2=7
sumResult = intVal1 + intVal2

driver.find_element_by_id("sum1").send_keys(intVal1)
driver.find_element_by_id("sum2").send_keys(intVal2)
driver.find_element_by_xpath("//*[@class='btn btn-default' and contains(text(),'Get Total')]").click()

strSumResult = driver.find_element_by_id("displayvalue").text
print(strSumResult)
assert strSumResult == str(sumResult), "Incorrect Sum displayed. Houston there is a problem"
print("Test-2 PASSED")

driver.quit()
