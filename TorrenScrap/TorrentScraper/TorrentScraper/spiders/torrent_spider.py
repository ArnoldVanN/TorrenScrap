import scrapy

from scrapy.selector.unified import Selector

from TorrentScraper.items import TorrentItem

from TorrentScraper.pipelines import TorrentscraperPipeline

class TorrentSpider(scrapy.Spider):

    name = 'torrents'

    def __init__(self, *args, **kwargs): 
        super(TorrentSpider, self).__init__(*args, **kwargs)
        self.title = kwargs['title']
        self.start_urls = [
        'https://thepiratebay.party/search/' 
        + self.title 
        ]

    def parse(self, response):
        torrent = TorrentItem()
        sel = Selector(response)
        items = []
        url = sel.xpath(f'/html[1]/body[1]/div[3]/table[1]/tbody[1]/tr[1]/td[2]').get()


        # for i in range(2, 5):
        #     torrent['url'] = sel.xpath(f'//*[@id="wrapperInner"]/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/div/table/tbody/tr[{i}]/td[1]/div[2]/div/a').extract_first()
        #     torrent['size'] = sel.xpath(f'//*[@id="wrapperInner"]/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/div/table/tbody/tr[{i}]/td[2]').get()
        #     torrent['seed'] = sel.xpath(f'//*[@id="wrapperInner"]/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/div/table/tbody/tr[{i}]/td[5]').get()
        #     torrent['leech'] = sel.xpath(f'//*[@id="wrapperInner"]/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/div/table/tbody/tr[{i}]/td[6]').get()
        #     items.append(torrent)
        
        filename = 'test.html'
        with open(filename, 'w') as f: 
            #f.write(str(response.body))
            f.write(str(response.body))
        return items

    def parse_magnet_uri(self, response):
        pass
