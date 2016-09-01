# -*- coding: utf-8 -*-

import logging
from re import compile
from urllib.request import urlopen, Request
from traktor.base_tracker import AbstractTracker


logger = logging.getLogger('LostFilm')


class RssHolder(object):

    ENCODING = '1251'
    DEFAULT_RSS_URL = 'https://www.lostfilm.tv/rssdd.xml'
    RE = compile(r'<link>(.+)</link>')

    def __init__(self, rss_url):
        self.rss_url = rss_url or RssHolder.DEFAULT_RSS_URL
        self.elements = None

    def get_elements(self):
        if self.elements is None:
            self.elements = self.load_rss()
        return self.elements

    def load_rss(self):
        logger.debug('Downloading %s', self.rss_url)
        request = Request(self.rss_url, None, {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'})
        rss = urlopen(request).read().decode(RssHolder.ENCODING)
        logger.debug('RSS Content:\n %s', rss)
        links = RssHolder.RE.findall(rss)
        logger.info('Found links: %s', ', '.join(links))
        return links


class LostFilmRSS(AbstractTracker):

    def __init__(self, settings):
        super(LostFilmRSS, self).__init__(settings)
        self.rss = RssHolder(settings.get('rss'))

    def process_torrent(self, torrent):
        logger.info('Check "%s"', torrent)
        self.rss.get_elements()
