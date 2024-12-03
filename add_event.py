#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from pymisp import PyMISP, MISPEvent
from config.config import MISP_URL, MISP_TOKEN


def create_event(distrib, threat, analysis, info):
    event = MISPEvent()
    event.distribution = distrib
    event.threat_level_id = threat
    event.analysis = analysis
    event.info = info
    event.attributes = []

    return event


def add_event():
    event = create_event('0', '1', '0', 'Test Event')

    misp = PyMISP(MISP_URL, MISP_TOKEN, False)

    try:
        added = misp.add_event(event, pythonify=True)
        print(f'Created: {added.to_json()}')

    except Exception as e:
        print(f'Event: {event.to_json()}')
        print(f'Exception: {repr(e)}')


if __name__ == '__main__':
    add_event()
