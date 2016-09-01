# -*- coding: utf-8 -*-

import logging
from yaml import safe_load as load_yaml
from traktor.factory import build, TrackerNotFoundError, ActionNotFoundError


logging.basicConfig(
    level=logging.DEBUG,
    datefmt='%d.%m.%Y %H:%M:%S',
    format='[%(asctime)s][%(name)-8s][%(levelname)-5s] %(message)s'
)

logger = logging.getLogger()

SETTINGS_FILE_PATH = '/home/sns/devel/traktor/src/traktor.yml'


def run():
    try:
        logger.info('Traktor started')

        logger.debug('Trying to read settings from "%s"', SETTINGS_FILE_PATH)
        with open(SETTINGS_FILE_PATH, 'r') as f:
            tasks = [build(tracker, settings) for tracker, settings in load_yaml(f).items()]
        logger.debug('Setting read completed successfuly')

        for task in tasks:
            task.process()

        logger.info('Traktor finished')

    except TrackerNotFoundError as e:
        logger.error('Processor for tracker "%s" not found', e.tracker)

    except ActionNotFoundError as e:
        logger.error('Action for tracker "%s" not found', e.tracker)

    except Exception as e:
        logger.exception(e)
