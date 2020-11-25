# welltory_test

Скрипт находит ошибки структуры и данных в JSON файлах в папке *event*

## Запуск

Установить зависимости
```
pip install -r requirements.txt
```
Запустить
```
python3 validate.py
```

Результат работы скрипта записывается в файл log.txt:

```
Total:17 Fails:15 Passed:2

Validate 'c72d21cf-1152-4d8e-b649-e198149d5bbb.json'
No such schema with name 'meditation_created', check the key 'event' value

================================

Validate '6b1984e5-4092-4279-9dce-bdaa831c7932.json'
No such schema with name 'meditation_created', check the key 'event' value

================================

Validate '2e8ffd3c-dbda-42df-9901-b7a30869511a.json'
No such schema with name 'meditation_created', check the key 'event' value

================================

Validate '29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json'
File '29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json' is not JSON-file

================================

Validate '3ade063d-d1b9-453f-85b4-dda7bfda4711.json'
No such schema with name 'cmarker_calculated', check the key 'event' value

================================

Validate 'ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json'
ERRORS:
---------------
None is not of type 'integer'
Invalid data type in key 'user_id', data type expected 'integer'
---------------
'suprt marker' is not of type 'array'
Instanse: suprt marker
Invalid data type in key 'cmarkers', data type expected 'array'

================================

Validate 'cc07e442-7986-4714-8fc2-ac2256690a90.json'
Required key 'data' is missing, check the key in the JSON file

================================

Validate 'f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json'
Validate successful!

================================

Validate '1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json'
ERRORS:
---------------
'unique_id' is a required property
Instanse: {'id': None, 'rr_id': None, 'labels': [{'slug': 'flu', 'type': 2, 'color': {'color': '#e83e35', 'lab
Required key 'unique_id' is missing, the required keys are: 
['id', 'labels', 'rr_id', 'timestamp', 'unique_id', 'user', 'user_id']
---------------
'user' is a required property
Instanse: {'id': None, 'rr_id': None, 'labels': [{'slug': 'flu', 'type': 2, 'color': {'color': '#e83e35', 'lab
Required key 'user' is missing, the required keys are: 
['id', 'labels', 'rr_id', 'timestamp', 'unique_id', 'user', 'user_id']
---------------
'user_id' is a required property
Instanse: {'id': None, 'rr_id': None, 'labels': [{'slug': 'flu', 'type': 2, 'color': {'color': '#e83e35', 'lab
Required key 'user_id' is missing, the required keys are: 
['id', 'labels', 'rr_id', 'timestamp', 'unique_id', 'user', 'user_id']

================================

Validate 'ba25151c-914f-4f47-909a-7a65a6339f34.json'
No such schema with name 'label_       selected', check the key 'event' value

================================

Validate 'a95d845c-8d9e-4e07-8948-275167643a40.json'
File 'a95d845c-8d9e-4e07-8948-275167643a40.json' is empty

================================

Validate 'fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json'
ERRORS:
---------------
{'id': 8, 'date': '2020-06-27', 'name': 'Сегодня тренировался', 'slug': 'workout_today'} is not of type 'array'
Instanse: {'id': 8, 'date': '2020-06-27', 'name': 'Сегодня тренировался', 'slug': 'workout_today'}
Invalid data type in key 'cmarkers', data type expected 'array'

================================

Validate 'bb998113-bc02-4cd1-9410-d9ae94f53eb0.json'
ERRORS:
---------------
'unique_id' is a required property
Instanse: {'info': [{'type': 'in_bed_time', 'value': 32880000.0}, {'type': 'sleep_time', 'value': 31320000.0},
Required key 'unique_id' is missing, the required keys are: 
['source', 'timestamp', 'finish_time', 'activity_type', 'time_start', 'unique_id']

================================

Validate 'test.json'
Invalid JSON, needs to be corrected:
 Expecting property name enclosed in double quotes: line 1 column 29 (char 28)

================================

Validate '3b4088ef-7521-4114-ac56-57c68632d431.json'
Validate successful!

================================

Validate '297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json'
ERRORS:
---------------
'type' is a required property
Instanse: {'date': '2020-08-27T08:34:00-04:00'}
Required key 'type' is missing, the required keys are: 
['date', 'type']
---------------
'type' is a required property
Instanse: {'date': '2020-08-27T09:34:00-04:00'}
Required key 'type' is missing, the required keys are: 
['date', 'type']
---------------
'type' is a required property
Instanse: {'date': '2020-08-27T09:40:00-04:00'}
Required key 'type' is missing, the required keys are: 
['date', 'type']

================================

Validate 'e2d760c3-7e10-4464-ab22-7fda6b5e2562.json'
ERRORS:
---------------
'bad user id' is not of type 'integer'
Instanse: bad user id
Invalid data type in key 'user_id', data type expected 'integer'

================================

```