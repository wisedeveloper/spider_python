#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import re
import urllib

from bs4 import BeautifulSoup


class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # <a target="_blank" href="/item/%E8%87%AA%E7%94%B1%E8%BD%AF%E4%BB%B6/405190"
        links = soup.find_all('a', href=re.compile(r'/item/*'))
        for link in links:
            new_url = link['href']
            # new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_full_url = 'https://baike.baidu.com'+new_url
            new_urls.add(new_full_url)
        return new_urls


    def _get_nxew_data(self, page_url, soup):
        new_data = {}

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        new_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        new_data['summary'] = summary_node.get_text()

        new_data['url'] = page_url

        return new_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_nxew_data(page_url, soup)

        return new_urls, new_data

