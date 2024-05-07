## Split raw data date

import dateutil

# Raw Data Structure: 
# datetime,season,holiday,workingday,weather,temp,atemp,humidity,windspeed,casual,registered,count
# Model expects data in this format (it was trained with these features):
# season,holiday,workingday,weather,temp,atemp,humidity,windspeed,year,month,day,dayofweek,hour

def transform_data(data):
    try:
        features = data.copy()
        dt=dateutil.parser.parse(features[0])

        features.append(dt.year)
        features.append(dt.month)
        features.append(dt.day)
        features.append(dt.weekday())
        features.append(dt.hour)

        return ','.join([str(feature) for feature in features[1:]])

    except:
        print('Error when transforming: {0},{1}'.format(data,err))
        raise Exception('Error when transforming: {0},{1}'.format(data,err))
        