#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from pymisp import PyMISP, MISPAttribute
from config.config import MISP_URL, MISP_TOKEN


def create_attribute(value, category, type, comment, to_ids, first_seen, last_seen, tags):
    attribute = MISPAttribute()
    attribute.value = value
    attribute.category = category
    attribute.type = type
    attribute.comment = comment
    attribute.to_ids = to_ids
    attribute.first_seen = first_seen
    attribute.last_seen = last_seen

    for tag in tags:
        attribute.add_tag(tag)

    return attribute


def add_attribute():
    event_id = '4df8e7dc-49a3-4a08-a586-5c5b3616982a'

    if not event_id:
        print('Event id is empty!')
        return

    attribute = create_attribute(
        'test.pdf',
        'Payload delivery',
        'filename',
        'Email attachment',
        '0',
        '2024-01-01',
        '2024-08-31',
        ['tlp:green', 'ransomware'])

    misp = PyMISP(MISP_URL, MISP_TOKEN, False)

    try:
        added = misp.add_attribute(event_id, attribute, pythonify=True)

        print(f'Created: {added.to_json()}')

    except Exception as e:
        print(f'Attribute: {attribute.to_json()}')
        print(f'Exception: {repr(e)}')


if __name__ == '__main__':
    add_attribute()
