from flask import Flask, jsonify
import json
import random
from random import randint
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Dev API!'

@app.route('/baidcheck/<baid>', methods=['GET'])
def baidcheck(baid):
    
    eligibility_check_payload = {
    
    'BA_ID': baid,
    'GNN_ID': randint(10000, 99999),
    'IS_ELIGIBLE': int(round(random.uniform(0, 1))),
    'BA_OPEN_DT': '2019-01-01',
    'QUERY_ID': str(uuid.uuid4())}
    
    return jsonify(eligibility_check_payload)


@app.route('/billingdata/<baid>', methods=['GET'])
def billingdata(baid):
    
    payload_customer = {
    
    'GNN_ID': randint(10000, 99999),
    'BA_ID': baid,
    'AS_USED_YR_MO': '2020-05',
    'AS_BILLED_YR_MO': '2020-06',
    'TOT_THMS_BILLED': randint(10, 99999),
    'BILLING_ST_DT': '2020-04-01',
    'BILLING_END_DT': '2020-05-01',
    'QUERY_ID': str(uuid.uuid4())}
    
    return jsonify(payload_customer)

if __name__ == '__main__':
    app.run()
