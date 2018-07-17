#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class HtmlOutpter(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        with open('output.html', 'w') as f:
            f.write('<meta charset=UTF-8"/>')
            f.write('<html>')
            f.write('<body>')
            f.write('<table>')

            for data in self.datas:
                f.write('<tr>')
                f.write('<td>%s</td>' % data['url'])
                f.write('<td>%s</td>' % data['title'])
                f.write('<td>%s</td>' % data['summary'])
                f.write('</tr>')

            f.write('</table>')
            f.write('</body>')
            f.write('</html>')
