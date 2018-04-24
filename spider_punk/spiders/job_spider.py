import time
from csv import DictWriter
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from scrapy import Spider, Request


class JobsSpider(Spider):
    name = "job_search"

    def __init__(self, keyword=None, category=None, **kwargs):

        self.keyword = keyword
        self.category = category

        super().__init__(**kwargs)

    @staticmethod
    def save_as_csv(lod, headers, fname):
        with open(fname + '.csv', 'w') as f:
            fobj = DictWriter(f, fieldnames=headers)
            fobj.writeheader()
            fobj.writerows(lod)

    def start_requests(self):

        yield Request(url='https://www.federalreserve.gov/start-job-search.htm', callback=self.parse)

    def parse(self, response):

        driver = self.job_search_help('https://www.federalreserve.gov/start-job-search.htm')

        with open("jobs.html", "w+") as h_blob:
            h_blob.write(driver.page_source)

        soup = BeautifulSoup(driver.page_source, "lxml")
        per_job_data = soup.find(id='requisitionListInterface.listRequisition').tbody.find_all('div', attrs={'class': 'iconcontentpanel'})

        retval = []
        headers = ['role', 'location', 'posting_date']

        for j_obj in per_job_data:
            retval.append(dict(zip(headers, [data.get_text() for data in j_obj.find_all('div', attrs={'class': 'contentlinepanel'})])))

        save_as_csv(retval, headers, 'jobs')

    def job_search_help(self, base_url):
        driver = webdriver.Chrome(executable_path='../../chromedriver')

        driver.get(base_url)

        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

        if self.category is not None:
            select = Select(driver.find_element_by_xpath('//*[@id="advancedSearchInterface.jobfield1L1"]'))
            select.select_by_visible_text(self.category)

        if self.keyword is not None:
            driver.find_element_by_xpath('//*[@id="advancedSearchInterface.keywordInput"]').send_keys(self.keyword)

        if self.keyword is not None or self.category is not None:
            driver.find_element_by_xpath('//*[@id="advancedSearchFooterInterface.searchAction"]').click()
            time.sleep(5)

        return driver
