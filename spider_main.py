# coding:utf-8

import url_manager, html_outputer, html_parser, html_downloader


# 目标:百度百科Python词条相关的词条网页-标题和简介
# 入口页:https://baike.baidu.com/item/Python/407313
# URL格式:
#	词条页面URL格式:/item/%E8%87%AA%E7%94%B1%E8%BD%AF%E4%BB%B6/405190
# 数据格式:
#	标题:<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1></dd>
#	简介:<div class="lemma-summary" label-module="lemmaSummary"></div>
# 网页编码:utf-8

class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutpter()

    def craw(self, url):
        count = 1
        self.urls.add_new_url(url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                # 爬取前10条数据
                if count == 10:
                    break
                count = count + 1

            except Exception as e:
                print('%d:craw failed --- %s' % (count, e))

        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
