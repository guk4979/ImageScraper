from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys

import tkinter

from tkinter import filedialog
import time

import urllib.request



# 실행 코드




class download():

    def download_img(self, image):
        self.image = image
        self.limit = limit


        for num in range(0, self.limit):


            try:

                imgUrl = self.image[num]

                opener=urllib.request.build_opener()

                opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36')]

                urllib.request.install_opener(opener)

                urllib.request.urlretrieve(imgUrl,selected_folder + "/" + keyword + str(num+1) + ".jpg")

                # urllib.request.urlretrieve(imgUrl, str(num) + ".jpg")

            except:
                pass



class scraper(download):

    def __init__(self,num):

        options = webdriver.ChromeOptions()

        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36")

        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        options.add_experimental_option("prefs", {"download.default_directory": selected_folder})

        options.add_argument('headless')

        options.add_argument('disable-gpu') 

        self.driver = []

        for i in range(0 , num):

            self.driver.append(webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options))



    def imageUrlFind(self, Url, keyword, num):
        self.num = num

        keyword = keyword

        self.driver[self.num].get(Url)


        SCROLL_PAUSE_TIME = 1

        # Get scroll height

        last_height = self.driver[self.num].execute_script("return document.body.scrollHeight")

        t = 0


        while t <= 2:

            # Scroll down to bottom

            self.driver[self.num].execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page

            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height

            new_height = self.driver[self.num].execute_script("return document.body.scrollHeight")

            last_height = new_height

            t += 1


        try:

            image1 = self.driver[self.num].find_elements_by_css_selector("a.link--h3bPW > img")


            if image1 == []:

                raise Exception()


            for num in range(0 , limit):

                img.append(image1[num].get_attribute("src"))

            self.driver[self.num].close()
            return

        except:
            pass

        try:

            image3 = self.driver[self.num].find_elements_by_css_selector("div.VQW0y > img")


            if image3 == []:

                raise Exception()


            for num in range(0 , limit):

                img.append(image3[num].get_attribute("src"))

            self.driver[self.num].close()
            return

        except:
            pass


        try:

            image2 = self.driver[self.num].find_elements_by_css_selector("a.Link_link__mTUkz > img")


            if image2 == []:

                raise Exception()


            for num in range(0 , limit):

                img.append(image2[num].get_attribute("src"))

            self.driver[self.num].close()
            return

        except:
            pass
        


        
class textReader():


    def textReader(self,keywords):

        global keyword

        keyword = keywords

        self.koUrl = ("https://pixabay.com/ko/images/search/{0}".format(keyword), "https://www.pexels.com/ko-kr/search/{0}".format(keyword))

        self.enUrl = ("https://pixabay.com/images/search/{0}".format(keyword), "https://www.pexels.com/search/{0}".format(keyword), "https://unsplash.com/s/photos/{0}".format(keyword))

        num = 0

        if 'a' <= keyword[0] <= "z" or 'A' <= keyword[0] <='Z':

            
            URL = self.enUrl

        else:
            
            URL = self.koUrl

        textReader = scraper(len(URL))                
        for Url in URL:

            textReader.imageUrlFind(Url, keyword,num)

            num = num+1
            
        download().download_img(img)

        print("finish")

        endTime = time.time() - startTime

        print(endTime)


    


def test(): #테스트 함수

    hello = textReader()

    hello.textReader("cheese")


imrawling = tkinter.Tk()


imrawling.withdraw

imrawling.title("사진 줍줍")

imrawling.geometry("1200x800+300+100")

imrawling.resizable(False,False)


#실행 버튼

def active_btn():

    global limit
    global img
    global startTime

    limit =  int(limit_entry.get())

    img = []
    img.clear()

    startTime = time.time()
    textReader().textReader(str(keyword_entry.get()))


#저장 경로 설정

def select_fold():

    global select_fold

    select_fold = filedialog.askdirectory()

    if select_fold == "":
        return

    select_folder.delete(0, 'end')

    select_folder.insert(0, select_fold)

    global selected_folder
    selected_folder = select_folder.get()


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

