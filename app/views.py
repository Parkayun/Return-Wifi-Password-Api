#-*-coding:utf-8-*-
from flask import abort, jsonify, request

import password

from manage import app


@app.route('/', methods=['GET'])
def return_password():
    results = {}

    ssids = request.args.get('ssid')
    ssids = ssids.split(',')

    if '' in ssids:
        raise abort(400)

    results['passwords'] = password.from_ssids(ssids)
    
    return jsonify(results)
