import json
import csv
import numpy as np
import os

def model3(inputCounty, area):
    counties = []
    crop = []
    inputList = []

    area10 = ['Wheat','Oats','Barley']
    area5 = ['Wheat','Oats','Barley','Oranges','Strawberries']

    # Get the unique crops and county
    with open(os.path.dirname(__file__) + '/Data/crops_nonirr.csv') as fp:
    #with open(".\\Data\\crops.csv","rb") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            if row['areaname'] not in counties:
                counties.append(row['areaname'])
            if row['cropname'] not in crop:
                crop.append(row['cropname'])

    for county in counties:
        temp = []
        for i in crop:
            temp.append(0.0)
        with open(os.path.dirname(__file__) + '/Data/crops_nonirr.csv') as fp1:
        #with open("./Data/crops.csv","rb") as fp1:
            reader = csv.DictReader(fp1)
            for row in reader:
                if row['areaname'] == county:
                    if row['Expr1002'] == '':
                        temp[crop.index(row['cropname'])] = 0.0
                    else:
                        temp[crop.index(row['cropname'])] = float(row['Expr1002'])
        inputList.append(temp)

    corrArray = np.array(inputList)
    output = np.corrcoef(corrArray)

    print output

    inputIndex = counties.index((inputCounty))

    tempCorr = output[inputIndex]
    similarCountyIndex = 0
    try:
        similarCountyIndex = list(output[inputIndex]).index(sorted(tempCorr)[-2])
    except ValueError:
        print 'Caught Value error here'
        similarCountyIndex = list(output[inputIndex]).index(sorted(tempCorr)[-3])

    keys = crop
    values = inputList[similarCountyIndex]
    suggestedCrops = dict(zip(keys, values))

    if area == 10:
        for removal in area10:
            del  suggestedCrops[removal]
    if area == 5:
        for removal in area5:
            del suggestedCrops[removal]

    topSuggestions = sorted(suggestedCrops.iteritems(), key=lambda x:-x[1])[:5]
    print json.dumps(dict(topSuggestions))
    return json.dumps(dict(topSuggestions))
