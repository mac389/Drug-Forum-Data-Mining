# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import codecs
class ErowidPipeline(object):
    def process_item(self, item, spider):
    	cargo =  {'title': item['Title'],
    			'author': item['Author'],
    			 'text': item['Text'],
    			 'substance': item['Substance']}

    	directory = os.path.join('Erowid/archive/',cargo['substance'][0].strip().lower())
    	filename = os.path.join(directory,cargo['title']+'.txt')

    	if not os.path.exists(directory):
    		os.makedirs(directory)

    	with codecs.open(filename, encoding = 'utf-8', mode= 'wb') as fid:
    		for symbols in cargo['text']:
    			print>>fid,symbols 
