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


def run(settings_file, library_file):
    try:
        logger.info('Traktor started')

        logger.debug('Trying to read settings from "%s"', settings_file)
        with open(settings_file, 'r') as f:
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
