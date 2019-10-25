from keywordC import KeywordC  ##연관검색어 크롤러 import
from googleC import GoogleC     ##구글 크롤러 import
import pandas as pd

#tag데이터 csv파일 가져오기
#tagFile = pd.read_csv('tag.csv', sep=',', skiprows=1, nrows=5, header=None)     #테스트용 행 5개
tagFile = pd.read_csv('tag.csv', sep=',', skiprows=1, header=None)     #전체 데이터

keyword_results = list()        #연관검색어 csv에 저장할 값들(태그id, 태그 내용, 연관검색어1, 연관검색어2)
len_tag = len(tagFile)      #총 태그 개수

for i in range(0,len_tag):
    tag_content = tagFile[1][i]     #태그 내용
    tag_id = tagFile[0][i]      #태그 id

    #연관검색어 가져오기
    k = KeywordC(tag_content)
    words = k.getWords()
    
    if words is None:       #연관검색어 없는 경우
        keyword_results.append([tag_id, tag_content, "", ""])
    else:
        if len(words) == 1:
            keyword_results.append([tag_id, tag_content, words[0], ""])
        else:
            keyword_results.append([tag_id, tag_content, words[0],words[1]])

    #구글에서 이미지 수집하기
    g = GoogleC(tag_content)    #기존 태그
    g.getImages()

    #연관검색어
    if words is not None:
        for word in words:
            w = GoogleC(word)
            w.getImages()

#연관검색어 CSV 파일 저장
data = pd.DataFrame(keyword_results)
data.columns = ['tag_id', 'tag_content', 'word1', 'word2']
data.to_csv('tagWord.csv', encoding = 'cp949', index=False)

