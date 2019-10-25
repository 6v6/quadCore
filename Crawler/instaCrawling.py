import time
from konlpy.tag import Okt # 해시태그를 분석하기 위한 Twitter 모듈 
from selenium import webdriver # 크롬 브라우저 조작을 위한 모듈
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys # 페이지 스크롤링을 위한 모듈
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import urllib.request
import regex


keyword = input("검색할 계정을 입력하세요 : ")
# 크롤링할 url 주소
url = "https://www.instagram.com/" + keyword + "/"
# 다운로드 받은 driver 주소
DRIVER_DIR = 'C:Users/DS/Desktop/data'
# 크롬 드라이버를 이용해 임의로 크롬 브라우저를 실행시켜 조작한다.
driver = webdriver.Chrome(ChromeDriverManager().install())
# 암묵적으로 웹 자원을 (최대) 5초 기다리기
driver.implicitly_wait(5)
# 크롬 브라우저가 실행되며 해당 url로 이동한다.
driver.get(url)

url_list = []  #url list
count = 0



##앵커 태그 href 가져와서 list에 저장
def get_href():
    global url_list
    for i in range(8):
        for j in range(3):
            xpath = """//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[""" + str(i+1) + """]/div["""+ str(j+1) +"""]/a"""
            anchor = driver.find_element_by_xpath(xpath)
            url_list.append(anchor.get_attribute('href'))

            # 값의 중복을 방지를 리스트 set으로 변환후 리스트로 재할당
            url_list = list(set(url_list))




##url접근해서 tag/img 크롤링
def get_tags(url, desdir, textFile):
    global url_list
    global count
    count += 1
    webpage = urlopen(url).read()
    soup = BeautifulSoup(webpage, "lxml")

    ##이미지 저장
    image = soup.find("meta", property="og:image") # image: 이미지 url
    rand = random.randrange(1,1001)  # 이미지 이름(랜덤숫자)
    imgName = desdir + "/" + str(rand) + ".jpg"
    try:
        urllib.request.urlretrieve(image.get("content"),imgName)  #url이용해서 img폴더에 저장
        print(str(count) + "<Image: Success>")

    except ValueError:
        print("Error")


    ##게시글 타입 별 property값 가져오기
    tags = ""  #태그 저장할 변수
    prop = ""  #property 값
    ogType = soup.find("meta", property = "og:type")  #게시글 타입
    if ogType.get("content") == "instapp:photo":  #타입이 photo이면
        prop = "instapp:hashtags"
    else:  #타입이 video이면
        prop = "video:tag"


    ##한자 아니면 tag
    for title in soup.find_all("meta", property=prop):
        #print (title["content"] if title else "No meta title given")
        if regex.findall('[\p{Han}]+',title["content"]):  #한자인지 확인
            print("한자입니다.")
        else:  #한자가 아니면 tag로 추가
            tags += "#" + title["content"] 


    ##textFile 쓰기
    #print(tags)
    textFile.write("%s, %s\n"%(imgName, tags))


def main():
    
    desdir = "Data"    #이미지 저장 폴더
    textFile = open(desdir + "\\tag.txt", 'a')  #태그 csv파일


    elem = driver.find_element_by_tag_name("body")

    # 페이지 스크롤을 위해 임시 변수 선언
    pagedowns = 1

    # 스크롤을 20번 진행한다.
    while pagedowns < 5:
        # PAGE_DOWN(스크롤)에 따라서 결과 값이 달라진다. 
        # 기본적으로 브라우저 조작을 통해 값을 얻어올 때는 실제 브라우저에 보이는 부분이어야 요소를 찾거나 특정 이벤트를 발생시킬 수 있다.
        elem.send_keys(Keys.PAGE_DOWN)
        # 페이지 스크롤 타이밍을 맞추기 위해 sleep
        time.sleep(1)
        get_href()   #함수 호출
        pagedowns += 1

    for url in url_list:
        print(url)
        get_tags(url, desdir, textFile)

    textFile.close()

    
if __name__ == "__main__":
    main()


# 드라이버를 종료한다.
#driver.close()     
