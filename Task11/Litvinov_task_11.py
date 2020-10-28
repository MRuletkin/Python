import json
import csv
import requests
import re
################# 1)
def read_json(filename_with_path):
    with open(filename_with_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data
################# 2)
def sort_name(tmp_dict):
    return tmp_dict['name'].split()[::-1]

sort_dict = sorted(read_json('Task11/data.json'), key=sort_name)
for i in sort_dict:
    print(i['name'])
################# 3)
def sort_years(dict_):
    years = dict_['years']
    reg_ex = r'[0-9]+'
    reg_years = re.findall(reg_ex, years)
    if 'BC' in years:
        return -int(reg_years[1])
    else:
        return int(reg_years[1])

sort_dict = sorted(read_json('Task11/data.json'), key=sort_years)
for i in sort_dict:
     print(i['years'])
#################### 4)
def sort_text(tmp_dict):
    return len(tmp_dict['text'])

sort_dict = sorted(read_json('Task11/data.json'), key=sort_text)
for i in sort_dict:
     print(i['text'])

###################### 5)
url = 'https://api.forismatic.com/api/1.0/'

def get_response(url):
    response = requests.get(url, params={'method': 'getQuote', 'lang': "ru", 'format': "json"})
    return response.json()

def get_data(url):
    data = []
    while len(data) < 20:
        if get_response(url) not in data:
            data.append(get_response(url))
    return data

def sort_key(tmp_dict):
    return tmp_dict['quoteAuthor']

def get_sorted_data():
    return sorted(get_data(url), key=sort_key)

def get_csv_data():
    csv_data = []
    for line in get_sorted_data():
        if line['quoteAuthor'] != '':
            s_list = []
            s_list.append(line['quoteAuthor'])
            s_list.append(line['quoteText'])
            s_list.append(line['quoteLink'])
            csv_data.append(s_list)
    return csv_data

def write_csv():
    header = ['Автор', 'Цитата', 'Ссылка на ресурс']
    with open('Task11/11_task.csv', 'w', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        csvwriter.writerows(get_csv_data())

write_csv()




