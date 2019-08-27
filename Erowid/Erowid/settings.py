# -*- coding: utf-8 -*-

BOT_NAME = 'Erowid'

SPIDER_MODULES = ['Erowid.spiders']
NEWSPIDER_MODULE = 'Erowid.spiders'
DOWNLOAD_HANDLERS = {
  's3': None,
}
ITEM_PIPELINES = {'Erowid.pipelines.ErowidPipeline': 1}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Erowid (+http://www.yourdomain.com)'
