import scrapy
from dateutil import parser
import re


# playwright integration for js website  Note: Make sure to edit settings.py to include playwright

# remove all symbols from string and join together
def compareRegex(movie):
    movie = re.sub(r'[^\w]', '', movie)
    return movie

# spider for ticketnew website
class tkSpider(scrapy.Spider):
    name = 'tk'
    
    def start_requests(self):
        
        yield scrapy.Request(
            url=f'{self.link}'
            )

    async def parse(self, response):

        # values accessed from get url
        film = self.film
        date = self.date

        ## if date booking is active get the details
        
        active = response.css('li.ui-tabs-tab.ui-corner-top.ui-state-default.ui-tab.ui-tabs-active.ui-state-active').get()
        # logic to check and retrive only the needed data in json format
        if active != None:
            venuehtml =  response.css('div#divTheatreInfo')
            DT = (parser.parse(date)).strftime('%Y-%m-%d')
            for show in response.css('div.tn-entity-details')[1:]:
                showname = show.css('h5::text').get()
                if compareRegex(film) in compareRegex(showname.lower()):
                    yield {
                        'venue' : venuehtml.css('h2::text').get(),
                        'show' : showname,
                        'date' : DT,
                    }
        else: 
            yield {
                None
            }

# spider for bookmyshow website
class bmsSpider(scrapy.Spider):
    name = 'bms'

    def start_requests(self):
        yield scrapy.Request(
            url=f'https://in.bookmyshow.com/buytickets/{self.link}',
            # PageMethod('wait_for_selector', 'ul#showEvents')
           )

    async def parse(self, response):

        film = self.film
        date = self.date

        ## if date booking is active get the details
        active = response.css('li.slick-current').get()

        if active != None:
            venuehtml =  response.css('a.venue-heading')

            date_numeric = response.css('li.date-details.slick-slide.slick-current.slick-active > a > div.date-numeric::text').get()
            date_month = response.css('li.date-details.slick-slide.slick-current.slick-active > a > div.date-month::text').get()

            DT = (parser.parse(f'{date_month} {date_numeric} 2022')).strftime('%Y-%m-%d')
            if DT == date:
                for show in response.css('a.nameSpan'):
                    showname = show.css('a::text').get()
                    if compareRegex(film) in compareRegex(showname.lower()):
                        yield {
                            'venue' : venuehtml.css('a::text').get(),
                            'show' : showname,
                            'date' : DT,
                        }
            else:
                yield {
                    None
                }


# spider for sourcing ticketnew booking links and theater lists
class tkdataSpider(scrapy.Spider):
    name = 'tkdata'
    
    def start_requests(self):
        
        yield scrapy.Request(
            url=f'https://www.ticketnew.com/online-advance-booking/Theatres/C/{self.location}',
            # PageMethod('wait_for_selector', 'div.tn-entity-details')
            )

    async def parse(self, response):
   
        for elem in response.css('div.tn-entity'):
            venuename = elem.css('div.tn-entity-details')
            bookinglink = elem.css('div.tn-entity-book')
            yield {
                'value' : venuename.css('h5::text').get(),
                'bookinglink' : bookinglink.css('a').attrib['href'],
            }
