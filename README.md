# scrapyreq

A scrapy code with scrapyRT for scrapping info from TicketNew

Uses: [Scrapy](https://scrapy.org/) and [ScrapyRT](https://github.com/scrapinghub/scrapyrt)

Clone the git repo and run

```
cd scrapsense && scrapyrt
```

For getting the list & url of all theaters based on location

```
http://127.0.0.1:9080/crawl.json?spider_name=tkdata&start_requests=true&crawl_args={"location":"Bangalore"}
```

For getting details of shows from a theater on TicketNew

```
http://127.0.0.1:9080/crawl.json?spider_name=tk&start_requests=true&crawl_args={"link":"theater_link","film":"filmtitle","date":"date_in_YY-MM-DD"}
```

Result out as json
