import requests
from lxml.html import parse
from bs4 import BeautifulSoup

class KeywordC:
    
    def __init__(self, keyword, maxCount = 2):
        self.keyword = keyword
        self.maxCount = maxCount    #연관검색어 개수, default값은 2

    def getWords(self):
        count = 0
        word_list = list()  # 연관검색어 리스트
        url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query='+self.keyword

        response = requests.get(url)
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')

        ul = soup.find('ul', {'class':'_related_keyword_ul'})
        try:
            li_list = ul.find_all('li')
        except AttributeError:   #연관검색어가 없는 경우
            return None

        for li in li_list:
            if count > self.maxCount-1:
                break
            a = li.find('a')
            word = a.get_text()
            word_list.append(word)
            count += 1

        return word_list
