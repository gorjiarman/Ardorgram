import plotly.graph_objects as go
import json
from datetime import datetime
from datetime import timedelta
import csv
from pathlib import Path
import jdatetime

loveWords = []
graphDates = []
isJalali = False
SameTimeMessagesList = []
SameTimeMessages = ''

# loading resources -lovewords.csv-
try:
    base_path = Path(__file__).parent
    file_path = (base_path / "./res/lovewords.csv").resolve()
    with open(file_path, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                loveWords.append(row[0])

    print("Resources Loaded Successfully.")

except IOError:
    print("Could not load lovewords.csv")
# getting result.json path from user
file_path = input('Insert result.json file exported from telegram. \n')
# file_object  = open("result.json", "r",encoding="utf-8")

# opening result.json file and handling exceptions
try:
    file_object = open(file_path, 'r', encoding='utf-8')
    content = file_object.read()
    y = json.loads(content)

except IOError:
    print("Could find or read your result.json")
    y = None

# asking for calender type
calender = input('Gregorian Or Jalali? Type J or G \n')
if calender == 'J':
    isJalali = True
elif calender == 'j':
    isJalali = True
elif calender == 'G':
    isJalali = False
elif calender == 'g':
    isJalali = False
else:
    input('Try again, Gregorian Or Jalali? Type J or G \n')

print('Processing data, please wait...')
# loading json to object
messages = y["messages"]
# getting day zero time
startTimeString = messages[0]["date"].split('T')[0]
startTime = datetime.strptime(startTimeString, '%Y-%m-%d')
# reading messages one by one and searching for loveWords
for message in messages:
    currentDayString = message["date"].split('T')[0]
    currentDay = datetime.strptime(currentDayString, '%Y-%m-%d')
    # you can change time span from here
    endTime = startTime + timedelta(days=30)
    if currentDay >= endTime:
        if isJalali:
            graphDates.append(str(jdatetime.date.fromgregorian(date=startTime)) + ' --> ' + str(
                jdatetime.date.fromgregorian(date=endTime)))
        else:
            graphDates.append(str(startTime) + ' --> ' + str(endTime))

        SameTimeMessagesList.append(SameTimeMessages)
        startTime = endTime
        SameTimeMessages = ''
    else:
        SameTimeMessages += str(message["text"])

# generating graphs from raw data
data = []
counts = []
for loveWord in loveWords:
    for mSameTimeMessages in SameTimeMessagesList:
        counts.append(mSameTimeMessages.count(loveWord))
    data.append(go.Bar(name=loveWord, x=graphDates, y=counts))
    counts = []
# Showing graph
fig = go.Figure(data)
# Change the bar mode
fig.update_layout(barmode='stack')
fig.show()
