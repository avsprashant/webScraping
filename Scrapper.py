import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

chromedriver="C:\\Users\\raghu\\Desktop\\Chromedriver\\chromedriver.exe"
url="http://court.mah.nic.in/courtweb/index_eng.php"

# opens url
driver=webdriver.Chrome(chromedriver)
driver.get(url)
driver.maximize_window()

#selecting Pune from dropdown
obj=Select(driver.find_element_by_class_name("selectdistrict"))
obj.select_by_value("25")
#obj.select_by_visible_text("Pune-पुणे ")

#navigate to 'Court Orders' link
driver.find_element_by_xpath("""//*[@id="fourlinks"]/ul/li[2]/div[1]/a""").click()

time.sleep(3)

#further navigate to 'Order Date' link.
driver.find_element_by_xpath("""//*[@id="fourlinks"]/ul/li[2]/div[2]/ul/li[4]/a""").click()

time.sleep(5)

#switching to frame data
driver.switch_to.frame('data')

#clicking court complex radio button
driver.find_element_by_xpath("//*[@id='radCourtComplex']").click()

#selecting District from dropdown
obj1=Select(driver.find_element_by_xpath("""//*[@id="court_complex_code"]"""))
obj1.select_by_visible_text("District and Sessions Court, Shivajinagar, Pune - 411 005")

#selecting from date
driver.find_element_by_xpath("//*[@id='from_date']").click()
obj=Select(driver.find_element_by_class_name("datepick-month-year"))
obj.select_by_value("1/2019")
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[3]/a").click()

time.sleep(2)

#selecting to date
driver.find_element_by_xpath("//*[@id='to_date']").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/select[1]/option[1]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[4]/a").click()

###################################################

print(" ENTER CAPTCHA AND WAIT for 10sec \n")

time.sleep(20)

driver.find_element_by_xpath("""//*[@id="caseNoDet"]/div[7]/span[3]/input[1]""").click()

time.sleep(10)

#start from tr2 tag
start=2

#assuming we get results for 4 district courts at specified locations always at '//*[@id="showList2"]/div['
for i in [3,4,5,6]:

    x='//*[@id="showList2"]/div[';
    y="]/a";
    a=driver.find_element_by_xpath(x+str(i)+y).text
    #capturing filename
    filename=a.split(':')[0]
    #capturing no.of rows in each district court
    rows=int(a.split(':')[1][1:])
    #creating files
    f=open(filename+".txt","w")
    headers="(Sr No, Case Type/Case Number/Case Year, Order Date, Order No.)\n"
    f.write(headers)

    #looping through all records
    for start in range(start, rows + start):
        #looping thru all columns
        for k in [1,2,3,4]:
            x='//*[@id="showList1"]/tr['
            y=']/td['
            z=']'
            a=driver.find_element_by_xpath(x+str(start)+y+str(k)+z).text
            f.write(a+'\t')
        f.write('\n')

    #skipping the district court names which comes in between results
    start = start + 2
    #closing each file
    f.close()
