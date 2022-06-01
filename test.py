from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import tkinter
from tkinter import filedialog
import os

class function():
    def download_img(self):
        images = driver.find_elements_by_css_selector(".link--h3bPW")
        count = 0
        for image in images:
            if count == self.limit:
                break
            try:
                image.click()
                time.sleep(2)
                imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
                opener=urllib.request.build_opener()
                opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
                urllib.request.install_opener(opener)
                urllib.request.urlretrieve(imgUrl,self.path + "/" + self.keyWords + str(count+1) + ".jpg")
                count = count + 1
            except:
                pass


class scraper(function):
    def __init__(self,num):
        options = webdriver.ChromeOptions()
        # options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36')
        # options.add_argument('--ignore-certificate-errors')
        # options.add_argument('--ignore-ssl-errors')
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # options.add_experimental_option("prefs", {"download.default_directory": self.path})
        # options.add_argument('headless')
        options.add_argument('disable-gpu') 
        self.driver = []
        for i in range(0 , num):
            self.driver.append(webdriver.Chrome("chromedriver.exe", options=options))


    def english_find(self, Url, keyword, num):
        self.num = num
        self.keyword = keyword
        self.driver[self.num].get(Url)
        try:
            elem1 = self.driver[self.num].find_element_by_id("search")
            elem1.send_keys(self.keyword)
            elem1.send_keys(Keys.RETURN)
        except:
            pass
        try:
            elem2 = self.driver[self.num].find_element_by_name("q")
            elem2.send_keys(self.keyword)
            elem2.send_keys(Keys.RETURN)
        except:
            pass
        try:
            elem3 = self.driver[self.num].find_element_by_name("searchKeyword")
            elem3.send_keys(self.keyword)
            elem3.send_keys(Keys.RETURN)
        except:
            pass
        
    def korean_find(self, Url, keyword, num):
        self.num = num
        # self.keyword = keyword
        self.driver[self.num].get(Url)

    
    


        
class scraper2(scraper):
    def __init__(self):
        self.koUrl = ("https://pixabay.com/ko/", "https://www.pexels.com/ko-kr/")
        self.enUrl = ("https://pixabay.com/en/", "https://www.pexels.com/en/", "https://unsplash.com/")

    def scraping(self,keyword):
        
        self.keyword = keyword
        num = 0

        if 'a' <= keyword[0] <= "z" or 'A' <= keyword[0] <='Z':

            scraping = scraper(len(self.enUrl))

            for Url in self.enUrl:
                scraping.english_find(Url, self.keyword,num)
                num = num+1

        else:

            scraping = scraper(len(self.koUrl))
            
            for Url in self.koUrl:
                scraping.korean_find(Url, self.keyword,num)
                num = num+1


    

def test():
    hello = scraper2()
    hello.scraping("cheese")

test()


"""
imrawling = tkinter.Tk()

imrawling.withdraw
imrawling.title("사진 줍줍")
imrawling.geometry("1200x800+300+100")
imrawling.resizable(False,False)

#실행 버튼
def active_btn():
    start_scraping = scraper2() #(keyword_entry.get(), int(limit_entry.get()),select_folder.get())
    start_scraping.scraping(keyword_entry.get())

    compelet = sel.active()


#저장 경로 설정
def select_fold():
    global select_fold
    select_fold = filedialog.askdirectory()
    if select_fold == "":
        return
    select_folder.delete(0, 'end')
    select_folder.insert(0, select_fold)

title = tkinter.Label(imrawling, text="사진 줍줍",font='Helvetica 20 bold')
title.place(x=95, y=50)

keyword_entry = tkinter.Entry(imrawling)
keyword_entry.insert(0, "키워드를 입력하세요")
keyword_entry.bind("<Return>", active_btn)
keyword_entry.place(x=95, y=200, height=30, width=500)

limit_text = tkinter.Label(imrawling, text="다운로드할 사진 개수 :", font= "Helvetica 13")
limit_text.place(x=95, y=250)

limit_entry = tkinter.Entry(imrawling)
limit_entry.insert(0, 0)
limit_entry.bind("<Return>", active_btn)
limit_entry.place(x=275, y=250, height=30, width=320)

# start_img = PhotoImage(".\시작 버튼.png")
start_btn = tkinter.Button(imrawling, overrelief="solid", command=active_btn, repeatdelay=1000, repeatinterval=10)
start_btn.place(x=930, y=625, height=80, width=80) 

select_folder = tkinter.Entry(imrawling)
select_folder.place(x=95, y=550, height=30, width=320)

select_btn = tkinter.Button(imrawling,text="찾아보기", command=select_fold, repeatdelay=1000, repeatinterval=10)
select_btn.place(x=420, y=550, height=30,width=60)


#마우스 커서 좌표

# def motion(event):
#     x, y = event.x, event.y
#     print('{}, {}'.format(x, y))
# imrawling.bind('<Motion>', motion)


imrawling.mainloop()

"""