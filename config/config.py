#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# PyMISP Instance configurations
#

import urllib3
# Cleaner logs
urllib3.disable_warnings()

MISP_URL = 'http://localhost'

MISP_TOKEN = 'VpsWeu2TsfqLQ5BTfk2BgRIw6Ca6rj3vzJlIj4TX'

MISP_EVENTS_URL = f'{MISP_URL}/events'
MISP_ATTR_URL = f'{MISP_URL}/attributes'
