# This is a sample Python script.
import requests
from datetime import timedelta, datetime
import json
import time
import logging
import yaml
import sys


token = ""
trello_key = ""
board_id = ""
trello_url = "https://api.trello.com/1/boards/"
start_date = ""
end_date = ""
import calendar

python_trello = """\
 __                             ___               
|__)    |_ |_   _   _     _|_    |   _  _ | |  _  
|    \/ |_ | ) (_) | )     |     |  |  (- | | (_) 
     /                                                                                                                         
"""


def create_list(board_id, list_name):
    # calling Trello create list API
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    querystring = {"name": list_name, "key": trello_key, "token": token, "pos": "bottom"}
    response = requests.request("POST", url, params=querystring, verify=False)
    list_id = response.json()["id"]
    return list_id


def add_key_toke_query_string_cards(list_id, query_string):
    key_token = {"key": trello_key, "token": token, "idList": list_id, **query_string}
    return key_token


def create_card(list_id, query_string):
    # calling Trello create Card API
    url = f"https://api.trello.com/1/cards"
    querystring = add_key_toke_query_string_cards(list_id, query_string)
    response = requests.request("POST", url, params=querystring, verify=False)
    card_id = response.json()["id"]
    return card_id


def get_weekly_dates(date1, date2):
    # get dates + update Lists + cards w.r.t to dates
    for n in range(int((date2 - date1).days) + 1):
        yield date1 + timedelta(n)


def create_board_ws():
    # create boards in respective workspace
    url = trello_url

    query = {
        'key': trello_key,
        'token': token,
        'name': 'Python_automation',
        'idOrganization': '60c6138855d3314cb13dc802',
        'idBoardSource': '5f534dfc5745183ae8663382'

    }

    response = requests.request(
        "POST",
        url,
        params=query
    )

    print(response.text)


def create_calender_key_board():
    url = "https://api.trello.com/1/boards/{id}/calendarKey/generate"

    query = {
        'key': trello_key,
        'token': token
    }

    response = requests.request(
        "POST",
        url,
        params=query
    )
    print(response.text)


def get_file_data():
    # read json file
    file_obj = open('week_planner.json', )
    return json.load(file_obj)


def create_tasks():
    # get all dates between the two dates 6 months
    set_global_vars()
    planner_data = get_file_data()
    dates_array = []
    for dt in get_weekly_dates(start_date, end_date):
        date_date = dt.strftime('%Y-%m-%dT%H:%M:%S')
        dates_array.append(date_date.replace('00:00:00', '23:59:00'))
    days = 0
    counter = 0
    actual_weeks = (end_date - start_date).days // 7
    start_day = calendar.day_name[start_date.weekday()].upper()
    while counter <= actual_weeks:
        for lists in planner_data['LISTS']:
            list_name = list(lists.keys())[0]
            if start_day != list_name and days == 0:
               continue
            else:
                list_id = create_list(board_id,
                                      list_name if list_name != 'WEEK' else 'WEEK ##' + str(counter) + '## DONE')
                if list_name != 'WEEK':
                    all_cards = lists[list_name]['CARDS']
                    for card in all_cards:
                        date_tobe = (start_date + timedelta(days)).strftime('%Y-%m-%d')
                        card.update({'idList': list_id, 'due': date_tobe})
                        card_id = create_card(list_id, card)
                    days += 1
                else:
                    print('WEEK ##' + str(counter) + '## DONE')

                time.sleep(3)
            counter += 1


# setting up keys & token as global vars
def set_global_vars():
    with open('config.yaml') as cf_file:
        config = yaml.safe_load(cf_file.read())
    config = config.get('planner')
    global token
    token = config.get('trello').get('token')
    global trello_key
    trello_key = config.get('trello').get('key')
    global board_id
    board_id = config.get('trello').get('board_id')
    global start_date
    start_date = config.get('dates').get('start_date')
    global end_date
    end_date = config.get('dates').get('end_date')
    current_date = datetime.now().date()
    if start_date <= current_date:
        sys.exit("ERROR: Invalid start date, start date should greater than current date")

    if end_date < start_date and end_date < current_date:
        sys.exit("ERROR: Invalid end date, end date should greater than start date & current date")

# Entry point of the script.
if __name__ == '__main__':
    print(python_trello)
    logging.basicConfig(format='%(asctime)s - %(message)s')
    logging.info("Let the Magic Begin")
    create_tasks()
