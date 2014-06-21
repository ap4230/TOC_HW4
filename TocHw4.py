# -*- coding: utf-8 -*-
import sys
import urllib2
import json

road = list()
year = list()
roadName = ""
argument = u"土地區段位置或建物區門牌"

response = urllib2.urlopen(sys.argv[1])
text = json.load(response)

#---------------------------------------------------
for i in range(len(text)):
    if text[i][argument].find(u"大道") != -1:
        split = text[i][argument].find(u"大道")
        if split != 0:
            roadName = text[i][argument][0:split+1]

    elif text[i][argument].find(u"路") != -1:
        split = text[i][argument].find(u"路")
        if split != 0:
            roadName = text[i][argument][0:split+1]

    elif text[i][argument].find(u"街") != -1:
        split = text[i][argument].find(u"街")
        if split != 0:
            roadName = text[i][argument][0:split+1]

    elif text[i][argument].find(u"巷") != -1:
        split = text[i][argument].find(u"巷")
        if split != 0:
            roadName = text[i][argument][0:split+1]
    else:
        roadName = ""

    if roadName != "":
        if road.count(roadName) == 0:
            road.append(roadName)
#---------------------------------------------------

argumentYear = u"交易年月"
finalRoad = list()
yearcount = 0

for i in range(0,len(road)):
    for j in range(len(text)):
        if text[j][argument].find(road[i]) != -1:
            if year.count(text[j][argumentYear]) == 0:
                year.append(text[j][argumentYear])

    if len(year) > yearcount:
        del finalRoad[0:len(finalRoad)]
        finalRoad.append(road[i])
        yearcount = len(year)
    elif len(year) == yearcount:
        finalRoad.append(road[i])

    del year[0:len(year)]

#---------------------------------------------------

price = list()

for i in range(0, len(finalRoad)):
    for j in range(0, len(text)):
        if text[j][argument].find(finalRoad[i]) != -1:
            price.append(text[j][u"總價元"])
    string = finalRoad[i].encode('utf-8') + ", 最高成交價: "
    string += str(max(price)) + ", 最低成交價: " + str(min(price))
    print string
    string = ""

    del price[0:len(price)]