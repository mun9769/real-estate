from selenium import webdriver
from pyvirtualdisplay import Display

display = Display(visible=1, size=(1920, 1080))
display.start()

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "/usr/bin/google-chrome"
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')

url = "https://www.courtauction.go.kr/RetrieveMainInfo.laf"
path = '/home/moon/python/chromedriver'
driver = webdriver.Chrome(executable_path = path,chrome_options= chrome_options)
driver.get(url)
driver.find_element_by_id("idJiwonNm1").click()
driver.find_element_by_xpath('//*[@id="idJiwonNm1"]/option[8]').click()
# driver.find_element_by_name("인천지방법원").click()
driver.find_element_by_xpath("//*[@id=\"main_btn\"]/a/img").click()


items = []
sum = 0
i = 1
s = 2
while True:
    item0 = driver.find_elements_by_class_name("Ltbl_list_lvl0")
    item1 = driver.find_elements_by_class_name("Ltbl_list_lvl1")
    sum += len(item0 + item1)
    print(sum)

    page = driver.find_elements_by_class_name("page2")
    children = page[0].find_elements_by_tag_name("a")
    # print(len(children))
    # print(children[0].find_element_by_tag_name("span").text)
    try:
        if i == 1:
            children[0].click()
        elif i > 1 and i < 11 :
            children[i].click()
        else :
            children[s].click()
    except:
        break
    i += 1
    s += 1 
    if s > 11 :
        s = 2



for i in range(5):
    print(i)