#!/usr/bin/env python
import sys
import requests
import json
from opentreetesting import config, summarize_json_response
DOMAIN = config('host', 'golshost')
SUBMIT_URI = DOMAIN + '/db/data/ext/GoLS/graphdb/getSyntheticTree'
payload = {
    'treeID' : 'otol.draft.22',
    'format' : 'arguson', 
    'maxDepth' : 4
}
if len(sys.argv) > 1:
    payload['subtreeNodeID'] = sys.argv[1]
headers = {
    'content-type' : 'application/json',
    'accept' : 'application/json',
}
resp = requests.post(SUBMIT_URI,
                     headers=headers,
                     data=json.dumps(payload),
                     allow_redirects=True)
summarize_json_response(resp) or sys.exit(1)