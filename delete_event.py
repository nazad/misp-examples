#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from pymisp import PyMISP, MISPEvent
from config.config import MISP_URL, MISP_TOKEN


def delete_event():
    uuid = 'b1d863c3-da15-4a42-a1ee-c756c2d78a75'
    misp = PyMISP(MISP_URL, MISP_TOKEN, False)

    try:
        misp.delete_event(uuid)
        print(f'Event deleted: {uuid}')

    except Exception as e:
        print(f'Event: {uuid}')
        print(f'Exception: {repr(e)}')


if __name__ == '__main__':
    delete_event()
