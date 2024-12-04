#!/bin/bash
#

. .config

curl -k \
    --header "Authorization: $MISP_TOKEN" \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    $MISP_URL_EVENTS

echo ""
