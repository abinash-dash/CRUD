# 2.	Create an API endpoint that allows users to create new employees.


import pandas as pd
import requests
import json
from dateutil import parser
from dateutil.relativedelta import relativedelta
from datetime import datetime
from time import sleep


def create_employee(body):
    print('Creating User')
    url = "http://127.0.0.1:8000/create/"

    payload = json.dumps(body)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    status_code, resp = response.status_code, response.text
    print(f'Status Code :: {status_code}')
    print(
        f'User :: {body.get("emp_id")} ==> {body.get("emp_name")} Created successfully') if status_code == 200 else print(
        'User Creation failed')


# update existing data

def update_employee(body):
    print('Updating User')
    url = "http://127.0.0.1:8000/update/"

    payload = json.dumps(body)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    status_code, resp = response.status_code, response.text
    print(f'Status Code :: {status_code}')
    print(
        f'User :: {body.get("emp_id")} ==> {body.get("emp_name")} Updated successfully') if status_code == 200 else print(
        'User Updation failed')


def employee_exists(emp_id):
    print('Checking User')
    url = f"http://127.0.0.1:8000/id/{emp_id}/"
    response = requests.request("POST", url)
    status_code, resp = response.status_code, dict(json.loads(response.text))
    # print(f'Status Code :: {status_code}')
    query_status = resp.get('status')
    employee_existing = query_status == 200
    print(f"Status code :: {query_status}\nEmployee exists :: {employee_existing}")
    return employee_existing


def get_all_employees(per_page):
    pagewise_results = {}
    flag = True
    url = f"http://127.0.0.1:8000/pagination/?limit={per_page}&offset=0"
    page_num = 0
    while flag:
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers)
        status_code, resp = response.status_code, response.text
        output = dict(json.loads(resp))
        results = output.get('results')
        pagewise_results[page_num] = results
        if next_url := output.get('next'):
            url = next_url
            page_num += 1
        else:
            flag = False
            break
    print({k: len(v) for k, v in pagewise_results.items()})
    return pagewise_results


def employee_operations():
    file_path = "emp_data.csv"
    rows = pd.read_csv(file_path).to_dict('records')
    emp_created, emp_updated = 0, 0
    for idx, row in enumerate(rows):
        dob = row.pop('dob')
        age = relativedelta(datetime.now(), parser.parse(dob)).years
        row.update({
            'age': age
        })
        print(f"Row index :: {idx + 1}")
        if employee_exists(row.get('emp_id')):
            update_employee(row)
            emp_updated += 1
        else:
            create_employee(row)
            emp_created += 1
        print('=====' * 30)
        # sleep(3)
    print(f"New Employees Created :: {emp_created}\nOld Employees Updated :: {emp_updated}")
    get_all_employees(per_page=5)


if __name__ == '__main__':
    employee_operations()


def delete_data():
    URL = 'http://127.0.0.1:8000/pagination/?offset=310'
    data = {'emp_id' == 10312}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)


delete_data()
