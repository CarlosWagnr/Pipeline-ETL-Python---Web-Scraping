import scrapy


class NotebookSpider(scrapy.Spider):
    name = "notebook"
    allowed_domains = ["LISTA.MERCADOLIVRE.COM.BR"]
    start_urls = ["https://LISTA.MERCADOLIVRE.COM.BR/NOTEBOOK#D[A:NOTEBOOK]"]


    def parse(self, response):

        products = response.css('div.ui-search-result__wrapper')

        for product in products:

            # Variável para pegar todos os preços
            prices = product.css('span.andes-money-amount__fraction::text').getall()

            # Yield retorna valores e não um único objeto
            yield{
                'brand': product.css('span.poly-component__brand::text').get(),
                'name': product.css('a.poly-component__title::text').get(),
                'seller': product.css('span.poly-reviews__rating::text').get(),
                'reviews_amount': product.css('span.poly-reviews__total::text').get(),
                'old_price': prices[0] if len(prices) > 0 else None,
                'new_price': prices[1] if len(prices) > 1 else None
            }
            