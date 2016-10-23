def createEntryList(filename, delim=","):
    results =[]
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            results.append(line.split(delim))
    return results

def tfToInt(trueVal, falseVal, data):
    if data == []:
        return -1
    for entry in data:
        for i in range(len(entry)):
            if entry[i] == trueVal:
                entry[i] = 1
            elif entry[i] == falseVal:
                entry[i] = 0
