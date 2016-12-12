import json
import csv
import numpy as nm
import os


# This fucntion calculates the irrigatin needs foe the plants
def calculateIrrigation( moistData, runoffData, typeOfPlant):
    #Gallon water per day
    irrigationPattern = {}
    plantFactor = 0.5;
    if typeOfPlant == "lawn":
       plantFactor = 1.0
    elif typeOfPlant == "shrubs":
        plantFactor = 0.5

    for key in moistData:
        irrigationPattern[key] = ((moistData[key]/100) * plantFactor * 0.62)/ runoffData[key]
    irrigationJson = json.dumps(irrigationPattern, ensure_ascii=False)
    return irrigationJson


# This fucntion calculates the means for each month
def calculateMeanRunoff(monthName, monthData, runoffMonthData, moistData, runoffData):
    #Calculate the mean data for each month here
    npArray = nm.array(monthData)
    moistData[monthName] = npArray.mean()

    # Calculaate the runoff data for each month  here
    predictedRunoff = max(runoffMonthData.iterkeys(), key=(lambda key: runoffMonthData[key]))
    if predictedRunoff == "Negligible":
        runoffData[monthName] = 0.95
    elif predictedRunoff == "Very low":
        runoffData[monthName] = 0.90
    elif predictedRunoff == "Low":
        runoffData[monthName] = 0.85
    elif predictedRunoff == "Medium":
        runoffData[monthName] = 0.8
    elif predictedRunoff == "High":
        runoffData[monthName] = 0.65
    elif predictedRunoff == "Very high":
        runoffData[monthName] = 0.5
    else:
        runoffData[monthName] = 0.95

# Model for determining the irrigation needs
def model1(countyname="", typeOfPlant=""):

    print 'In irrigation'
    moistdata = {};
    runoffdata = {};
    # Variables to store the moistures
    Jan = []
    Feb = []
    Mar = []
    Apr = []
    May = []
    Jun = []
    Jul = []
    Aug = []
    Sep = []
    Oct = []
    Nov = []
    Dec = []

    # Variables to store the runoffdata
    janrunoff = {"Negligible": 0, "Very low": 0, "Low": 0, "Medium": 0, "High": 0, "Very high": 0}
    februnoff = {"Negligible": 0, "Very low": 0, "Low": 0, "Medium": 0, "High": 0, "Very high": 0}
    marrunoff = {"Negligible": 0, "Very low": 0, "Low": 0, "Medium": 0, "High": 0, "Very high": 0}
    aprrunoff = {"Negligible": 0, "Very low": 0, "Low": 0, "Medium": 0, "High": 0, "Very high": 0}
    mayrunoff = {"Negligible": 0, "Very low": 0, "Low": 0, "Medium": 0, "High": 0, "Very high": 0}
    junrunoff = {"Negligible": 0, "Very low": 0, "Low": 0, "Medium": 0, "High": 0, "Very high": 0}
    julrunoff = {"Negligible": 0, "Very low": 0, "Low": 0, "Medium": 0, "High": 0, "Very high": 0}
    augrunoff = {"Negligible": 0, "Very low": 0, "Low": 0, "Medium": 0, "High": 0, "Very high": 0}
    seprunoff = {"Negligible": 0, "Very low": 0, "Low": 0, "Medium": 0, "High": 0, "Very high": 0}
    octrunoff = {"Negligible": 0, "Very low": 0, "Low": 0, "Medium": 0, "High": 0, "Very high": 0}
    novrunoff = {"Negligible": 0, "Very low": 0, "Low": 0, "Medium": 0, "High": 0, "Very high": 0}
    decrunoff = {"Negligible": 0, "Very low": 0, "Low": 0, "Medium": 0, "High": 0, "Very high": 0}

    with open(os.path.dirname( __file__) + '/Data/irrigation.csv') as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            if countyname == "":
                countyname = row['areaname']
            if row['areaname'] == countyname:
                if row['month'] == "January":
                    if row['soimoistdepb_l'] != "" and row['runoff'] != '':
                        Jan.append(float(row['soimoistdepb_l']))
                        janrunoff[row['runoff']] = janrunoff[row['runoff']]+ 1;
                if row['month'] == "February":
                    if row['soimoistdepb_l'] != "" and row['runoff'] != '':
                        Feb.append(float(row['soimoistdepb_l']))
                        februnoff[row['runoff']] = janrunoff[row['runoff']] + 1;
                if row['month'] == "March":
                    if row['soimoistdepb_l'] != "" and row['runoff'] != '':
                        Mar.append(float(row['soimoistdepb_l']))
                        marrunoff[row['runoff']] = janrunoff[row['runoff']] + 1;
                if row['month'] == "April":
                    if row['soimoistdepb_l'] != "" and row['runoff'] != '':
                        Apr.append(float(row['soimoistdepb_l']))
                        aprrunoff[row['runoff']] = janrunoff[row['runoff']] + 1;
                if row['month'] == "May":
                    if row['soimoistdepb_l'] != "" and row['runoff'] != '':
                        May.append(float(row['soimoistdepb_l']))
                        mayrunoff[row['runoff']] = janrunoff[row['runoff']] + 1;
                if row['month'] == "June":
                    if row['soimoistdepb_l'] != "" and row['runoff'] != '':
                        Jun.append(float(row['soimoistdepb_l']))
                        junrunoff[row['runoff']] = janrunoff[row['runoff']] + 1;
                if row['month'] == "July":
                    if row['soimoistdepb_l'] != "" and row['runoff'] != '':
                        Jul.append(float(row['soimoistdepb_l']))
                        julrunoff[row['runoff']] = janrunoff[row['runoff']] + 1;
                if row['month'] == "August":
                    if row['soimoistdepb_l'] != "" and row['runoff'] != '':
                        Aug.append(float(row['soimoistdepb_l']))
                        augrunoff[row['runoff']] = janrunoff[row['runoff']] + 1;
                if row['month'] == "September":
                    if row['soimoistdepb_l'] != "" and row['runoff'] != '':
                        Sep.append(float(row['soimoistdepb_l']))
                        seprunoff[row['runoff']] = janrunoff[row['runoff']] + 1;
                if row['month'] == "October":
                    if row['soimoistdepb_l'] != "" and row['runoff'] != '':
                        Oct.append(float(row['soimoistdepb_l']))
                        octrunoff[row['runoff']] = janrunoff[row['runoff']] + 1;
                if row['month'] == "November":
                    if row['soimoistdepb_l'] != "" and row['runoff'] != '':
                        Nov.append(float(row['soimoistdepb_l']))
                        novrunoff[row['runoff']] = janrunoff[row['runoff']] + 1;
                if row['month'] == "December":
                    if row['soimoistdepb_l'] != "" and row['runoff'] != '':
                        Dec.append(float(row['soimoistdepb_l']))
                        decrunoff[row['runoff']] = janrunoff[row['runoff']] + 1;
                countyname = ""

    # calculate the mean of the month data
    calculateMeanRunoff("Jan", Jan, janrunoff, moistdata, runoffdata)
    calculateMeanRunoff("Feb", Feb, februnoff, moistdata, runoffdata)
    calculateMeanRunoff("Mar", Mar, marrunoff, moistdata, runoffdata)
    calculateMeanRunoff("Apr", Apr, aprrunoff, moistdata, runoffdata)
    calculateMeanRunoff("May", May, mayrunoff, moistdata, runoffdata)
    calculateMeanRunoff("Jun", Jun, junrunoff, moistdata, runoffdata)
    calculateMeanRunoff("Jul", Jul, julrunoff, moistdata, runoffdata)
    calculateMeanRunoff("Aug", Aug, augrunoff, moistdata, runoffdata)
    calculateMeanRunoff("Sep", Sep, seprunoff, moistdata, runoffdata)
    calculateMeanRunoff("Oct", Oct, octrunoff, moistdata, runoffdata)
    calculateMeanRunoff("Nov", Nov, novrunoff, moistdata, runoffdata)
    calculateMeanRunoff("Dec", Dec, decrunoff, moistdata, runoffdata)

    irrigation_suggestion = calculateIrrigation(moistdata, runoffdata, typeOfPlant=typeOfPlant)
    return irrigation_suggestion
