# -*- coding: utf-8 -*-

from traktor.lostfilm import LostFilmRSS
from traktor.base_action import AbstractAction
from traktor.save_to_folder import SaveToFolder
from traktor.base_tracker import AbstractTracker


class TrackerNotFoundError(Exception):
    def __init__(self, tracker):
        self.tracker = tracker
        super(TrackerNotFoundError, self).__init__()


class ActionNotFoundError(Exception):
    def __init__(self, tracker):
        self.tracker = tracker
        super(ActionNotFoundError, self).__init__()


def build(tracker, settings):
    tracker_cls = find_tracker_class(tracker)
    action_cls = find_action_class(tracker, settings)
    tracker = tracker_cls(settings)
    tracker.set_action(action_cls(settings))
    return tracker


def find_action_class(tracker, settings):

    try:
        action = settings['action']['kind']
    except KeyError:
        raise ActionNotFoundError(tracker)

    for cls in AbstractAction.__subclasses__():
        if cls.__name__ == action:
            return cls
    else:
        raise ActionNotFoundError(tracker)


def find_tracker_class(tracker):
    for cls in AbstractTracker.__subclasses__():
        if cls.__name__ == tracker:
            return cls
    else:
        raise TrackerNotFoundError(tracker)
