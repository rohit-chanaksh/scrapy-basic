import scrapy


class AllAuthorsSpider(scrapy.Spider):
    name = "all_authors"
    allowed_domains = ["book.org"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):

        # authors = response.css('small.author::text').get()
        # print()
        # print()
        # print('Author :-' , authors)
        # print()
        # print()
        

        auth_data = response.css('small.author::text')
        # print()
        # print()
        # print(auth_data)
        # print()
        # print()    

        for auth in auth_data :
            authors = auth.get()
            print()
            print()
            print('Author :-' , authors)
            print()
            print()

        pass
