from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas
#you should have geckodriver in ./ folder
main_sheets=pandas.read_excel(io="Youtube video.xlsx")
urls=main_sheets['url'].tolist()
youtube_url = []
driver = webdriver.Firefox(executable_path="geckodriver.exe")
for url in urls:

    try:
        driver.get(url)
        page=driver.page_source
        url1=page.find("https://www.youtube.com/watch?v=")
        url2=page.find("https://youtu.be/")
        url3=page.find("https://www.youtube.com/embed")
        url4=page.find("YouTube video player")

        if url4 != -1:
            index_of_seconde = (page.find('"', url4))
            char = range(index_of_seconde - url4)
            charlink = []
            for i in char:
                charlink.append(page[url4 + i])
            clink=''.join(charlink)
            youtube_url.append(clink)
        elif url3 != -1:
            index_of_seconde = (page.find('"', url3))
            char = range(index_of_seconde - url3)
            charlink = []
            for i in char:
                charlink.append(page[url3 + i])
            clink=''.join(charlink)
            youtube_url.append(clink)
        elif url2 != -1:
            index_of_seconde = (page.find('"', url2))
            char = range(index_of_seconde - url2)
            charlink = []
            for i in char:
                charlink.append(page[url2 + i])
            clink=''.join(charlink)

            youtube_url.append(clink)
        elif url1 != -1:
            index_of_seconde = (page.find('"', url1))
            char = range(index_of_seconde - url1)
            charlink = []
            for i in char:
                charlink.append(page[url1 + i])

            clink = ''.join(charlink)

            youtube_url.append(clink)
        else:
            youtube_url.append("there is no youtube links")
        print(youtube_url)

    except :
        pass



import xlrd

book = xlrd.open_workbook("Youtube video.xls")
sheet = book.sheet_by_index(0)
n=0
for i in youtube_url:

    sheet.cell(1+n, 0).value=i
    n+=1
