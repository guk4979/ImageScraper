from selenium import webdriver


class scraper:
    def __init__(self,num):
        self.driver = []
        for i in range(0 , num):
            self.driver.append(webdriver.Chrome("chromedriver.exe"))
            

    def english_find(self, Url, keyword, num):

        # self.keyword = keyword
        self.driver[num].get(Url)
        
    def korean_find(self, Url, keyword, num):

        # self.keyword = keyword
        self.driver[num].get(Url)
        
