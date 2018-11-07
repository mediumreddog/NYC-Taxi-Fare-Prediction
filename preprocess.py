import requests
import csv
import json
import pprint

with open('data/train.csv') as training_data:
    data_reader = csv.DictReader(training_data)

    with open('data/train_preprocessed.csv', 'a+') as training_data_out:
        data_writer = csv.writer(training_data_out)
        data_writer.writerow(['key', 'pickup_datetime', 'pickup_longitude', 'pickup_latitude',
                              'dropoff_longitude', 'dropoff_latitude', 'passenger_count', 'distance', 'travel_time', 'fare_amount'])

        for row in data_reader:
            r = requests.get('http://127.0.0.1:5000/route/v1/driving/' +
                             row['pickup_longitude'] + ',' + row['pickup_latitude'] + ';' + row['dropoff_longitude'] + ',' + row['dropoff_latitude'] + '?steps=false')

            response = r.json()

            try:
                data_writer.writerow([row['key'], row['pickup_datetime'], row['pickup_longitude'], row['pickup_latitude'], row['dropoff_longitude'],
                                      row['dropoff_latitude'], row['passenger_count'], response['routes'][0]['distance'], response['routes'][0]['duration'], row['fare_amount']])
            except:
                print "Error on Row Key: " + row['key']


print 'Completed Successfully'
