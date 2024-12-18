#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from pymisp import PyMISP  # ExpandedPyMISP is deprecated
from config.config import MISP_URL, MISP_TOKEN


def get_events():
    misp = PyMISP(MISP_URL, MISP_TOKEN, False)

    events = misp.events(pythonify=True)

    for e in events:
        print(f'Event: {e.to_json(indent=4)}')


if __name__ == '__main__':
    get_events()
