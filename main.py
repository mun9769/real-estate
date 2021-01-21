from selenium import webdriver
from pyvirtualdisplay import Display
import pymysql

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


sum = 0
i = 1
s = 2

conn = pymysql.connect(host="localhost",user = 'root',password=None,db='test',charset='utf8')
curs = conn.cursor()

sql = """insert into real_estate(no,사건번호,물건번호,소재지,비고,감정평가액,담당계,link)
                            value(%s,%s,%s,%s,%s,%s,%s,%s)"""

number = 1
while True:
    item0 = driver.find_elements_by_class_name("Ltbl_list_lvl0")
    item1 = driver.find_elements_by_class_name("Ltbl_list_lvl1")
    items = item0 + item1

    for item in items:
        curs.execute(sql,(str(number),
                        item.find_elements_by_css_selector("td")[1].text,
                        item.find_elements_by_css_selector("td")[2].text,
                        "none",
                        "none",
                        item.find_elements_by_css_selector("td")[5].text,
                        item.find_elements_by_css_selector("td")[6].text,
                        "none"))
    
        number += 1
        # print(item.find_elements_by_css_selector("td")[1].text)

    # sum += len(item0 + item1)
    # print(sum)

    page = driver.find_elements_by_class_name("page2")
    children = page[0].find_elements_by_tag_name("a")



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

conn.commit()
conn.close()


for i in range(5):
    print(i)