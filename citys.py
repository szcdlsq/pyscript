# -*- coding: utf-8 -*-
# 统计用区划代码转xml脚本


def processLevelEnd(number, name):
    result = "<_"
    result = result+str(number)+" Name="+'"'+name+'"'+" />"
    return result

def processLevelBegin(number, name):
    result = "<_"
    result = result + str(number) + " Name=" + '"' + name + '"' + ">"
    return result

def processLevelShortEnd(number):
    result = "</_"
    result = result+str(number)+">"
    return result


if __name__ == '__main__':
    url = open("E:/labdoc/区划代码/hebei.csv", encoding='utf-8')
    lines = url.readlines()
    changeFlag = "VILLAGE"
    cityInfo=[]
    countyInfo=[]
    townInfo=[]
    results = []

    xmlUrl = open("E:/a.dst", mode='w', encoding='utf-8')
    for i in range(1, len(lines)-1):
        attributes = lines[i].split("	")
        number = attributes[0]
        name = attributes[1]
        flag = attributes[3].strip()
        attributesNext = lines[i+1].split("	")
        numberNext = attributesNext[0]
        nameNext = attributesNext[1]
        flagNext = attributesNext[3].strip()

        if(flag=="CITY"):
            cityInfo.clear()
            cityInfo.append(number)
            cityInfo.append(name)
            string = processLevelBegin(number, name)
            results.append("  "+string+"\n")
        if(flag=="COUNTY"):
            countyInfo.clear()
            countyInfo.append(number)
            countyInfo.append(name)
            string = processLevelBegin(number, name)
            results.append("    "+string+"\n")
        if(flag=="TOWN"):
            townInfo.clear()
            townInfo.append(number)
            townInfo.append(name)
            string = processLevelBegin(number, name)
            results.append("      "+string + "\n")
        if(flag=="VILLAGE" and flag==flagNext):
            string = processLevelEnd(number, name)
            results.append("        "+string + "\n")
        if (flag == "VILLAGE" and flag!=flagNext):
            string = processLevelEnd(number, name)
            results.append("        "+string + "\n")
            if(flagNext=="TOWN"):
                stringTown = processLevelShortEnd(townInfo[0])
                results.append("      "+stringTown+"\n")
            if(flagNext=="COUNTY"):
                stringTown = processLevelShortEnd(townInfo[0])
                results.append("      " + stringTown + "\n")
                stringCounty = processLevelShortEnd(countyInfo[0])
                results.append("    "+stringCounty+"\n")
            if(flagNext=="CITY"):
                stringTown = processLevelShortEnd(townInfo[0])
                results.append("      " + stringTown + "\n")
                stringCounty = processLevelShortEnd(countyInfo[0])
                results.append("    " + stringCounty + "\n")
                stringCity = processLevelShortEnd(cityInfo[0])
                results.append("  "+stringCity+"\n")

    attributes = lines[-1].split("	")
    number = attributes[0]
    name = attributes[1]
    flag = attributes[3].strip()
    string = processLevelEnd(number, name)
    results.append("        " + string + "\n")
    stringTown = processLevelShortEnd(townInfo[0])
    results.append("      " + stringTown + "\n")
    stringCounty = processLevelShortEnd(countyInfo[0])
    results.append("    " + stringCounty + "\n")
    stringCity = processLevelShortEnd(cityInfo[0])
    results.append("  "+stringCity + "\n")

    xmlUrl.writelines(results)
    xmlUrl.close()
    url.close()













