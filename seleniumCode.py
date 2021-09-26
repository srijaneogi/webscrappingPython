from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

# Github credentials
username = "tatacliqmonitoring@tataunistore.com"
passkey = "Omniture@2020"
print(passkey)
# initialize the Chrome driver
#C:\Users\Rahul\PycharmProjects
driver = webdriver.Chrome(executable_path="C:\\Users\\Rahul\\PycharmProjects\\chromedriver_win32\\chromedriver.exe")
# head to github login page
#driver.get("https://experience.adobe.com/#/@tataunistore/home")
driver.get("https://experience.adobe.com/login")
# find username/email field and send the username itself to the input field
#driver.get("https://sc5.omniture.com/spa/index.html?IMS=1&company=tata%20unistore%20limited&current_org=E9174ABF55BA76BA7F000101@AdobeOrg#/reports")
driver.maximize_window()
#driver.find_element_by_class_name("login-sign-in").click()
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID,"EmailPage-EmailField")))
#print(driver.page_source)
driver.find_element_by_id("EmailPage-EmailField").send_keys(username)
driver.find_element_by_class_name("ta-right").click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID,"PasswordPage-PasswordField")))
print(driver.page_source)
driver.find_element_by_id("PasswordPage-PasswordField").send_keys(passkey)

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"spectrum-ToggleSwitch-label")))
driver.find_element_by_class_name("spectrum-ToggleSwitch-label").is_enabled()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"spectrum-Button-label")))
driver.find_element_by_class_name("spectrum-Button-label").click()
#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"quick-access-section")))
#driver.find_element_by_id("password").send_keys(password)

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#print(driver.page_source)

nowUrl=driver.current_url

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(nowUrl)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#driver.get(nowUrl)
#WebDriverWait(driver,30).until(EC.presence_of_element_located((By.ID,"root")))
#print(driver.page_source)
#driver.find_element_by_id("root")
#/html/body/div[1]/div/div/main/div[3]/div[2]/div[2]/div[1]/div[1]/a
#driver.find_element_by_xpath("//*[@id="root"]/div/div/main/div[3]/div[2]/div[2]/div[1]/div[1]")

elems = driver.find_elements_by_xpath("//a[@href]")
c=1
for elem in elems:
    print("no ",c," href")
    c+=1
    print(elem.get_attribute("href"))

#driver.find_element_by_partial_link_text("Dashboard For Web").click()
#print(driver.page_source)

driver.get("http://exc-unifiedcontent.experience.adobe.net")

print("bye bye .. going to subelement....! ! !")
print(driver.page_source)
WebDriverWait(driver, 120).until(EC.frame_to_be_available_and_switch_to_it("Main Content"))
#driver._switch_to.frame("Main Content")
print("Printing IFRAME contents ...................")
print(driver.page_source)
WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.LINK_TEXT,"Reports")))
driver.find_element_by_link_text("Reports").send_keys(Keys.COMMAND + 'w')
print("1234566 - - - - You are my life !!!!")
#WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"report-link-container")))
#driver.get("http://www4.omniture.com/spa")
#print(driver.current_url)
#print(driver.session_id)
#WebDriverWait(driver, 30).
#
window_after = driver.window_handles[0]
driver.switch_to.window(window_after)
print(driver.current_url)
window_after = driver.window_handles[0]
driver.switch_to.window(window_after)

print("Test current URL")
print(driver.current_url)
#print(driver.page_source)
#WebDriverWait(driver, 30).until(EC.url_matches("https://www4.omniture.com"))
#WebDriverWait(driver, 30).until(EC.url_matches("https://experience.adobe.com"))
print("at www 4 onmitue dot com page ")
#print(driver.page_source)
print(driver.current_url)
print("going to second iframe")
#print(driver.page_source)
print("switch")
#WebDriverWait(driver, 60).until(EC.frame_to_be_available_and_switch_to_it("Main Content"))

#driver.get("http://exc-unifiedcontent.experience.adobe.net")

WebDriverWait(driver, 60).until(EC.url_contains("https://experience.adobe.com"))
WebDriverWait(driver, 60).until(EC.url_contains("ssSession="))
#print(driver.page_source)

ssSessionurl=driver.current_url
driver.get(ssSessionurl)
#print(driver.page_source)
print("Jhal Muri . . . ")



print("xxx")
#driver.get("https://www4.an.adobe.com")
WebDriverWait(driver, 120).until(EC.title_contains("Reports"))
WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME,"exc-core-sandbox")))
driver.find_element_by_class_name("exc-core-sandbox")
WebDriverWait(driver, 120).until(EC.frame_to_be_available_and_switch_to_it("Main Content"))

print("Dashboards urls check")
print(driver.page_source)
WebDriverWait(driver, 120).until(EC.visibility_of_element_located((By.XPATH, "//a[@data-test-id=\"report-link-recent-dashboard-for-app-imran-tcs\"]")))

driver.find_element_by_xpath("//a[@data-test-id=\"report-link-recent-dashboard-for-app-imran-tcs\"]").click()

#driver.find_element_by_link_text("Dashboard For App (Imran_TCS)").click()
#driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/iframe')
#WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.LINK_TEXT,"Reports")))
#driver.find_element_by_link_text("Reports").send_keys(Keys.COMMAND + 'w')
#WebDriverWait(driver, 60).until(EC.frame_to_be_available_and_switch_to_it('//*[@id="exc-app-sandbox*"]'))
#WebDriverWait(driver, 120).until(EC.frame_to_be_available_and_switch_to_it("/html/body/div[1]/div/div/div/div[1]/iframe"))
#driver._switch_to.frame("/html/body/div[1]/div/div/div/div[1]/iframe")

print("Going inside Dashboard for APP (Imran TCS)")
print(driver.page_source)

#driver.find_element(By._ti =)

#WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME("report-link"))))
#driver.find_element_by_class_name()
#print(driver.page_source)
#driver._switch_to.frame("Main Content")
#driver.find_element_by_id("root")
#driver.close()
#window_after = driver.window_handles[0]
#driver.switch_to.window(window_after)
#driver.get("https://www4.an.adobe.com")

#print(driver.current_url)
#WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME,"coral--light spectrum spectrum--light spectrum--medium is-unified-shell light-theme")))
#print(driver.page_source)

#window_after = driver.window_handles[0]
#driver.switch_to.window(window_after)
print("Going to check visits for APp")
#WebDriverWait(driver, 120).until(EC.visibility_of_element_located((By.XPATH, "//a[@data-test-id=\"report-link-frequent-dashboard-for-app-imran-tcs\"]")))
#driver.find_element_by_xpath("//a[@data-test-id=\"report-link-frequent-dashboard-for-app-imran-tcs\"]").click()
#driver.refresh()
print("\n\n\n\n\n\n\n\n\n\n")
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME,"an-ViewLayout-contents")))
driver.find_element_by_class_name("an-ViewLayout-contents")
print("Found")
WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//a[@data-test-id=\"report-link-recent-visits-for-app\"]")))
driver.find_element_by_xpath("//a[@data-test-id=\"report-link-recent-visits-for-app\"]").click()
#WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME,"an-ViewLayout-componentContent")))
#driver.find_element_by_class_name("an-ViewLayout-componentContent")

print(driver.page_source)
print("Trying to find table")
print(driver.current_url)
#WebDriverWait(driver, 120).until(EC.url_contains(""))
#WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME,"exc-core-sandbox")))
#driver.find_element_by_class_name("exc-core-sandbox")
#WebDriverWait(driver, 120).until(EC.frame_to_be_available_and_switch_to_it("Main Content"))
#print(driver.page_source)


#print(driver.page_source)
