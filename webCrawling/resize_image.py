import os
import io
from PIL import Image

MAX_SIZE = 400

def resize(file):
    img = Image.open(file)
    new_img = img.resize((MAX_SIZE,MAX_SIZE))
    new_img.save(str(file))

def getfiles(srcdir):  ##폴더에서 파일 읽어와 리스트로 반환
    files = []
    for f in os.listdir(srcdir):
        if os.path.isfile(os.path.join(srcdir,f)):
            if not f.startswith('.'):
                files.append(os.path.join(srcdir,f))

    return files

def main():
    #srcdir = input("원본 이미지 폴더: ")
    srcdir = "C:/Users/kimsk/Documents/cns/webCrawling/Data"

    files = getfiles(srcdir)
    for f in files:
        if 'jpg' in f:
            resize(f)
            
main()
