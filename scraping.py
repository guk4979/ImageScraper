from selenium import webdriver




def english_find(Url, keyword):


    (webdriver.Chrome("chromedriver.exe")).get(Url)
    

def korean_find(Url, keyword):


    (webdriver.Chrome("chromedriver.exe")).get(Url)

    
def start(keyword, path):

    

    koUrl = ("https://pixabay.com/ko/", "https://pixabay.com/ko/")
    enUrl = ("https://pixabay.com/en/", "https://pixabay.com/en/", "https://unsplash.com/")



    if 'a' <= keyword[0] <= "z" or 'A' <= keyword[0] <='Z':

        for Url in enUrl:


            english_find(Url, keyword)

    else:
        
        for Url in koUrl:


            korean_find(Url, keyword)



