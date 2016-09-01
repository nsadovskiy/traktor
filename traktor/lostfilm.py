# -*- coding: utf-8 -*-

from traktor.base_tracker import AbstractTracker


class LostFilmRSS(AbstractTracker):

    RSS_URL = 'https://www.lostfilm.tv/rssdd.xml'

    def __init__(self, settings):
        super(LostFilmRSS, self).__init__(settings)
        self.rss_url = settings.get('rss') or LostFilmRSS.RSS_URL

    def process_torrent(self, torrent):
        pass
