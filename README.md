# Spider Punk
Scrapy spider for jobs at Federal Reserve - https://www.federalreserve.gov/start-job-search.htm


### SETUP (Requires python 3.6 env) - 

1. git clone <url>
2. pip install requirements


### RUN - 

scrapy crawl job_search -a keyword=<insert keyword> -a category=<category of jobs>

Arguements are optional

#### Example - 

scrapy crawl job_search -a keyword=analyst -a category=Accounting


###### Saves Scraped Data into a csv in the root folder - jobs.csv
