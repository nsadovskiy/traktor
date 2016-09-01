# -*- coding: utf-8 -*-


class AbstractTracker(object):

    def __init__(self, settings):
        self.action = None
        self.torrents = settings['torrents']

    def set_action(self, action):
        self.action = action

    def process(self):
        for torrent in self.torrents:
            self.process_torrent(torrent)

    def process_torrent(self, torrent):
        pass
