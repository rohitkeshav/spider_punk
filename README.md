# Spider Punk
A Scrapy based webspider for jobs at Federal Reserve - https://www.federalreserve.gov/start-job-search.htm


### Setup (Requires python 3.6 env) - 

  * git clone https://github.com/rohitkeshav/spider_punk.git`
  * pip install requirements


### Run - 

```scrapy crawl job_search -a keyword=*insert keyword* -a category=*category of jobs*```

Arguements are optional

#### Example - 

```scrapy crawl job_search -a keyword=analyst -a category=Accounting```


###### Saves Scraped Data into a csv in the root folder - jobs.csv
