import scrapy
import redis
from scrapy_redis.spiders import RedisSpider

from ..items import PositionSpiderItem
from .. import settings


class ZLSpider(RedisSpider):
    name = "zhi_lian"

    def __init__(self, **kwargs):
        self.redis_cli = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
        super().__init__(**kwargs)

    def parse(self, response, **kwargs):
        positions = response.css('div.joblist-box__item')
        if not len(positions):
            return
        next_url = []
        flag = False
        for s in response.url.split('&'):
            if s.startswith('p='):
                flag = True
                s = s.split('=')
                s[1] = str(int(s[1]) + 1)
                s = '='.join(s)
            next_url.append(s)
        if not flag:
            next_url.append('p=2')
        next_url = '&'.join(next_url)
        print("++++++++++++++++++++++++++++")
        print(next_url)
        self.redis_cli.lpush("zhi_lian:start_urls", next_url)
        print("++++++++++++++++++++++++++++")
        for position in positions:
            url = position.css('a::attr(href)').get()
            item = PositionSpiderItem()
            item['position_name'] = position.css('span.iteminfo__line1__jobname__name::attr(title)').get()
            item['company_name'] = position.css('span.iteminfo__line1__compname__name::text').get()
            comdesc = position.css('span.iteminfo__line2__compdesc__item::text').getall()
            item['company_class'] = comdesc[0].strip()
            item["company_scale"] = comdesc[1].strip()
            item["detail_url"] = url.split('?')[0]
            jobdesc = position.css('ul.iteminfo__line2__jobdesc__demand li::text').getall()
            item["position_base"] = jobdesc[0].strip()
            item["position_experience"] = jobdesc[1].strip()
            item["position_degree"] = jobdesc[2].strip()
            print(item.__dict__)
            yield item
