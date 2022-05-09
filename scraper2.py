from scraper import *
   
def scraping(keyword):

    scraping = scraper()

    koUrl = ("https://pixabay.com/ko/", "https://pixabay.com/ko/")
    enUrl = ("https://pixabay.com/en/", "https://pixabay.com/en/", "https://unsplash.com/")

    if 'a' <= keyword[0] <= "z" or 'A' <= keyword[0] <='Z':

        for Url in enUrl:
            scraping.english_find(Url, keyword)

    else:
        
        for Url in koUrl:
            scraping.korean_find(Url, keyword)
