from serial import Serial
import json
import requests
import time
import datetime

data = {}

urls = {
    'table1':{
        'startsit': 'http://127.0.0.1/api/table/1/startsit',
        'ordered': 'http://127.0.0.1/api/table/1/ordered',
        'arrived': 'http://127.0.0.1/api/table/1/arrived',
        'finished': 'http://127.0.0.1/api/table/1/finished',
        'endSit': 'http://127.0.0.1/api/table/1/endSit',
    },
    'table2':{
        'startsit': 'http://127.0.0.1/api/table/2/startsit',
        'ordered': 'http://127.0.0.1/api/table/2/ordered',
        'arrived': 'http://127.0.0.1/api/table/2/arrived',
        'finished': 'http://127.0.0.1/api/table/2/finished',
        'endSit': 'http://127.0.0.1/api/table/2/endSit',
    },
    'table3':{
        'startsit': 'http://127.0.0.1/api/table/3/startsit',
        'ordered': 'http://127.0.0.1/api/table/3/ordered',
        'arrived': 'http://127.0.0.1/api/table/3/arrived',
        'finished': 'http://127.0.0.1/api/table/3/finished',
        'endSit': 'http://127.0.0.1/api/table/3/endSit',
    },
    'table4':{
        'startsit': 'http://127.0.0.1/api/table/4/startsit',
        'ordered': 'http://127.0.0.1/api/table/4/ordered',
        'arrived': 'http://127.0.0.1/api/table/4/arrived',
        'finished': 'http://127.0.0.1/api/table/4/finished',
        'endSit': 'http://127.0.0.1/api/table/4/endSit',
    },
    'table5':{
        'startsit': 'http://127.0.0.1/api/table/5/startsit',
        'ordered': 'http://127.0.0.1/api/table/5/ordered',
        'arrived': 'http://127.0.0.1/api/table/6/arrived',
        'finished': 'http://127.0.0.1/api/table/6/finished',
        'endSit': 'http://127.0.0.1/api/table/6/endSit',
    },
    'table7':{
        'startsit': 'http://127.0.0.1/api/table/7/startsit',
        'ordered': 'http://127.0.0.1/api/table/7/ordered',
        'arrived': 'http://127.0.0.1/api/table/7/arrived',
        'finished': 'http://127.0.0.1/api/table/7/finished',
        'endSit': 'http://127.0.0.1/api/table/7/endSit',
    },
    'table8':{
        'startsit': 'http://127.0.0.1/api/table/8/startsit',
        'ordered': 'http://127.0.0.1/api/table/8/ordered',
        'arrived': 'http://127.0.0.1/api/table/8/arrived',
        'finished': 'http://127.0.0.1/api/table/8/finished',
        'endSit': 'http://127.0.0.1/api/table/8/endSit',
    },
    'table9':{
        'startsit': 'http://127.0.0.1/api/table/9/startsit',
        'ordered': 'http://127.0.0.1/api/table/9/ordered',
        'arrived': 'http://127.0.0.1/api/table/9/arrived',
        'finished': 'http://127.0.0.1/api/table/9/finished',
        'endSit': 'http://127.0.0.1/api/table/9/endSit',
    },
    'table10':{
        'startsit': 'http://127.0.0.1/api/table/10/startsit',
        'ordered': 'http://127.0.0.1/api/table/10/ordered',
        'arrived': 'http://127.0.0.1/api/table/10/arrived',
        'finished': 'http://127.0.0.1/api/table/10/finished',
        'endSit': 'http://127.0.0.1/api/table/10/endSit',
    },
    'table11':{
        'startsit': 'http://127.0.0.1/api/table/11/startsit',
        'ordered': 'http://127.0.0.1/api/table/11/ordered',
        'arrived': 'http://127.0.0.1/api/table/11/arrived',
        'finished': 'http://127.0.0.1/api/table/11/finished',
        'endSit': 'http://127.0.0.1/api/table/11/endSit',
    },
    'table12':{
        'startsit': 'http://127.0.0.1/api/table/12/startsit',
        'ordered': 'http://127.0.0.1/api/table/12/ordered',
        'arrived': 'http://127.0.0.1/api/table/12/arrived',
        'finished': 'http://127.0.0.1/api/table/12/finished',
        'endSit': 'http://127.0.0.1/api/table/12/endSit',
    },
    'table13':{
        'startsit': 'http://127.0.0.1/api/table/13/startsit',
        'ordered': 'http://127.0.0.1/api/table/13/ordered',
        'arrived': 'http://127.0.0.1/api/table/13/arrived',
        'finished': 'http://127.0.0.1/api/table/13/finished',
        'endSit': 'http://127.0.0.1/api/table/13/endSit',
    },
    'table14':{
        'startsit': 'http://127.0.0.1/api/table/14/startsit',
        'ordered': 'http://127.0.0.1/api/table/14/ordered',
        'arrived': 'http://127.0.0.1/api/table/14/arrived',
        'finished': 'http://127.0.0.1/api/table/14/finished',
        'endSit': 'http://127.0.0.1/api/table/14/endSit',
    },
    'table15':{
        'startsit': 'http://127.0.0.1/api/table/15/startsit',
        'ordered': 'http://127.0.0.1/api/table/15/ordered',
        'arrived': 'http://127.0.0.1/api/table/15/arrived',
        'finished': 'http://127.0.0.1/api/table/15/finished',
        'endSit': 'http://127.0.0.1/api/table/15/endSit',
    },
    'table16':{
        'startsit': 'http://127.0.0.1/api/table/16/startsit',
        'ordered': 'http://127.0.0.1/api/table/16/ordered',
        'arrived': 'http://127.0.0.1/api/table/16/arrived',
        'finished': 'http://127.0.0.1/api/table/16/finished',
        'endSit': 'http://127.0.0.1/api/table/16/endSit',
    },
    'table17':{
        'startsit': 'http://127.0.0.1/api/table/17/startsit',
        'ordered': 'http://127.0.0.1/api/table/17/ordered',
        'arrived': 'http://127.0.0.1/api/table/17/arrived',
        'finished': 'http://127.0.0.1/api/table/17/finished',
        'endSit': 'http://127.0.0.1/api/table/17/endSit',
    },
    'table18':{
        'startsit': 'http://127.0.0.1/api/table/1/startsit',
        'ordered': 'http://127.0.0.1/api/table/18/ordered',
        'arrived': 'http://127.0.0.1/api/table/18/arrived',
        'finished': 'http://127.0.0.1/api/table/18/finished',
        'endSit': 'http://127.0.0.1/api/table/18/endSit',
    },
    'table19':{
        'startsit': 'http://127.0.0.1/api/table/19/startsit',
        'ordered': 'http://127.0.0.1/api/table/19/ordered',
        'arrived': 'http://127.0.0.1/api/table/19/arrived',
        'finished': 'http://127.0.0.1/api/table/19/finished',
        'endSit': 'http://127.0.0.1/api/table/19/endSit',
    },
    'table20':{
        'startsit': 'http://127.0.0.1/api/table/20/startsit',
        'ordered': 'http://127.0.0.1/api/table/20/ordered',
        'arrived': 'http://127.0.0.1/api/table/20/arrived',
        'finished': 'http://127.0.0.1/api/table/20/finished',
        'endSit': 'http://127.0.0.1/api/table/20/endSit',
    },
    'entered': 'http://127.0.0.1/api/entered',
    'sit': 'http://127.0.0.1/api/sit'

}

arduino = Serial('/dev/ttyUSB0', 9600, timeout=.1)

def segregate(config, second):
    if config == 'sit' and second == 'sit':
        urlneeded = urls[config]
        return urlneeded
    elif config == 'entered' and second == 'entered':
        urlneeded = urls[config]
        return urlneeded
    else:
        return urls[config][second]
while 1:
    if arduino.readline():
        inputData = arduino.readline()[:-2]
        ArrayData = inputData.split(' ')
        print(len(ArrayData))
        print(str(ArrayData))
        Datapayload = {
            "Timestep": str(datetime.datetime.now()),
            "Data": ArrayData[2],


        }
        payload = json.dumps(Datapayload)

        r = requests.post(segregate(ArrayData[0],ArrayData[1]), data=payload)
