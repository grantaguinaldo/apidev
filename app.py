from flask import Flask, jsonify
import json
import random
from random import randint
import uuid
import requests as r

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome'

@app.route('/baidcheck/<baid>', methods=['GET'])
def baidcheck(baid):
    
    eligibility_check_payload = {
    
    'BA_ID': baid,
    'GNN_ID': randint(10000, 99999),
    'IS ELIGIBLE': int(round(random.uniform(0, 1))),
    'BA_OPEN_DT': '2019-01-01',
    'QUERY_ID': str(uuid.uuid4())}
    
    return jsonify(eligibility_check_payload)


@app.route('/billingdata/<baid>', methods=['GET'])
def billingdata(baid):
    
    payload_customer = {
    
    'GNN_ID': randint(10000, 99999),
    'BA_ID': baid,
    'SVC_ZIP': randint(10000, 99999),
    'CEC_ZONE': randint(10, 99),
    '2018_BASELOAD_THMS_WINTER_2018_THMS': randint(1, 99999),
    'WINTER_2018_2019_THMS': randint(1, 99999),
    'TOTAL_THMS': randint(1, 99999),
    '2018_ANNUAL_WINTER_2018_BASE_RATIO': random.uniform(0, 1),
    'WINTER_2018_2019_TOTAL_RATIO': random.uniform(0, 1),
    'IS_WINTER_2018_THMS_BETWEEN_50_70_PCT': int(round(random.uniform(0, 1))),
    'IS_WINTER_2018_THMS_ABOVE_70_PCT': int(round(random.uniform(0, 1))),
    'IS_2018_BASELOAD_THMS_50_70_PCT': int(round(random.uniform(0, 1))),
    'IS_2018_BASELOAD_THMS_ABOVE_70_PCT': int(round(random.uniform(0, 1))),
    'IS_WINTER_2018_BASE_RATIO_50_70_PCT': int(round(random.uniform(0, 1))),
    'IS_WINTER_2018_BASE_RATIO_ABOVE_70_PCT': int(round(random.uniform(0, 1))),
    'BA_OPEN_DT': '2019-01-01',
    'QUERY_ID': str(uuid.uuid4())}
    
    return jsonify(payload_customer)

if __name__ == '__main__':
    app.run()