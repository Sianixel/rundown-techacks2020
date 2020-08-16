import scrapy

class ScholarScraper(scrapy.Spider):
    name = "scholar-scraper"
    tracker = 'root'
    
    def __init__(self, **kwargs):
        super(ScholarScraper, self).__init__(**kwargs)
        self.start_urls = ['https://scholar.google.ca/scholar?hl=en&as_sdt=0%2C5&q=' + self.keywords + '&btnG=']
      
    def parse(self, response):
        yield {
            'root_article_title': response.selector.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "gs_rt", " " ))]//a')[0].get(),
            'root_article_citedby': response.selector.xpath('//*+[contains(concat( " ", @class, " " ), concat( " ", "gs_nph", " " ))]//a')[0].get(),
            'root_article_related': response.selector.xpath('//a[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]')[0].get(),
            'root_article_description': response.selector.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "gs_rs", " " ))]')[0].get()
        }
        citedby_url = response.urljoin(response.selector.xpath('//*+[contains(concat( " ", @class, " " ), concat( " ", "gs_nph", " " ))]//a')[0].get())
        related_url = response.urljoin(response.selector.xpath('//a[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]')[0].get())
            
        print(citedby_url)
        print(related_url)
            
        yield scrapy.Request(citedby_url, callback = self.parse_citedby)
        yield scrapy.Request(related_url, callback = self.parse_related)


    def parse_citedby(self, response):
        yield{
            'citedby_article_title': response.selector.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "gs_rt", " " ))]//a').get(),
            #'citedby_article_citedby': response.selector.xpath('//*+[contains(concat( " ", @class, " " ), concat( " ", "gs_nph", " " ))]//a').get(),
            #'citedby_article_related': response.selector.xpath('//a[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]').get(),
            'citedby_article_description': response.selector.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "gs_rs", " " ))]').get()
        }

    def parse_related(self, response):
        yield{
            'related_article_title': response.selector.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "gs_rt", " " ))]//a').get(),
            #'related_article_citedby': response.selector.xpath('//*+[contains(concat( " ", @class, " " ), concat( " ", "gs_nph", " " ))]//a').get(),
            #'related_article_related': response.selector.xpath('//a[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]').get(),
            'related_article_description': response.selector.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "gs_rs", " " ))]').get()
        }