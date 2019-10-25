import requests
from lxml.html import parse
from io import StringIO
import os, sys
from PIL import Image
from bs4 import BeautifulSoup
import urllib.request
import random
from unidecode import unidecode         #폴더명 영어로 변환

class GoogleC:
    
    def __init__(self, word):
        self.keyword = word         # 검색할 이미지의 키워드

    def getImages(self):   
        url = 'https://www.google.co.kr/search?q='+self.keyword+'&source=lnms&tbm=isch&sa=X&ved=0ahUKEwic-taB9IXVAhWDHpQKHXOjC14Q_AUIBigB&biw=1842&bih=990'
        imgDir = './imgData/' + (unidecode(self.keyword)).strip()        #이미지 저장할 폴더, 각 태그 별로 폴더 생성
        if not os.path.isdir(imgDir):       #폴더 없으면 생성
            os.mkdir(imgDir)
        
        # html 소스 가져오기
        text = requests.get(url, headers={'user-agent': ':Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}).text

        # html 문서로 파싱
        text_source = StringIO(text)
        parsed = parse(text_source)

        # root node 
        doc = parsed.getroot()

        # img 경로는 img 태그안에 src에 있음
        imgs = doc.findall('.//img')

        img_list = []   # 이미지 경로가 담길 list
        for a in imgs:

            if a.get('data-src') is None:       
                continue
            
            else:
                img_list.append(a.get('data-src'))      #이미지 url을 리스트에 저장

        for img in img_list:
            print(img)
            try:
                name = random.randrange(1,1001)  #저장할 이미지 이름 랜덤숫자 붙여서 생성
                full_name = imgDir + "/" + str(name) + ".jpg"
                urllib.request.urlretrieve(str(img),full_name)  #url이용해서 각 태그폴더에 저장
            except ValueError:
                print("None!")
            except urllib.error.HTTPError:
                print("HTTPError 404 not found")
