from scraper import *
   
def scraping(keyword):

    koUrl = ("https://pixabay.com/ko/", "https://www.pexels.com/ko-kr/")
    enUrl = ("https://pixabay.com/en/", "https://www.pexels.com/en/", "https://unsplash.com/")

    scraping = scraper(4)

    num = 0

    if 'a' <= keyword[0] <= "z" or 'A' <= keyword[0] <='Z':

        for Url in enUrl:
            scraping.english_find(Url, keyword,num)
            num = num+1

    else:
        
        for Url in koUrl:
            scraping.korean_find(Url, keyword,num)
            num = num+1
