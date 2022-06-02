import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs
import scrapy

from DC_11688.items import Dc11688Item
from DC_11688.settings import SEEDS

heading = '//div[@class="col-xs-12"]//text()'
substance_name = '//div[@class="clearfix"]//p//span[child::b[contains(., "Substance name:")]]//text()'
documents_xp = '//div[contains(@class, "col-xs-12")]//li[contains(@class, "dss-card consultation")]'
urls_xp = './/h2//a/@href'
proposed_for = '//div[@class="dss-easy-reading cs-constrain-overview-column-for-readability"]//p//span[child::b[contains(., "Proposed use:")]]//text()'
status = '//div/h2[@class="cs-consultation-sidebar-primary-date"]//text()'
topic_id = 'SUBSTANCEUSAGE'

DOCUMENT_ID_RGX = r"^https?://(?:www\.)?.*?\.uk/(.+)"
DOCUMENT_ID_PREFIX = "HSE"


class A11688Spider(scrapy.Spider):

    def start_requests(self):
        for key, value in SEEDS.items():
            yield scrapy.Request(url=value,
                                 callback=self.parse,
                                 meta={'tag': key})

    name = 'DC_11688'
    allowed_domains = ['consultations.hse.gov.uk']

    def parse(self, response):
        tag = response.meta.get('tag')

        documents = response.xpath(documents_xp)
        for doc in documents:
            url = doc.xpath(urls_xp).extract_first()
            yield scrapy.Request(url=urljoin(response.url, url), callback=self.parse_document, meta={'tag': tag})

    def parse_document(self, response):
        title = prettify_text(*response.xpath(heading).extract() + response.xpath(substance_name).extract())
        abstract = prettify_text(*response.xpath(proposed_for).extract() + response.xpath(status).extract())
        tag = response.meta.get('tag')

        item = Dc11688Item()
        item["title"] = title
        item["abstract"] = abstract
        item["topic_id"] = topic_id
        item["tag"] = tag

        yield item


def prettify_text(*text):
    text = " ".join(text)
    return re.sub(r"\s+", " ", text).strip().replace("\r", "").replace("\n", "").replace("\t", "").strip()


def generate_fulltext(fulltext):
    fulltext = " ".join(fulltext)
    fulltext = bs(fulltext).prettify().replace("\r", "").replace("\n", "")
    return fulltext


def generate_document_id(url):
    document_id = re.findall(DOCUMENT_ID_RGX, url)[0].strip("/").replace("/", "-").upper()
    document_id = ":".join([DOCUMENT_ID_PREFIX, document_id]).upper().rstrip(".PDF").replace("%20", "-")
    return document_id
