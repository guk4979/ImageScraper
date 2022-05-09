from selenium import webdriver


class scraper:
    def __init__(self):

        self.driver = webdriver.Chrome("chromedriver.exe")

    def english_find(self, Url, keyword):

        # self.keyword = keyword
        self.driver.get(Url)
        
    def korean_find(self, Url, keyword):

        # self.keyword = keyword
        self.driver.get(Url)
        
