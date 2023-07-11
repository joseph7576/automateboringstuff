import csv

exampleFile = open('Data/absfiles/example.csv')

exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)
print(exampleData[0][1])

# outputFile = open('output.csv', 'w', newline='') #? if you forget the newline, rows will be double spaced
# csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n') #? separate cells with a tab char, rows to be double spaced

#? defaults
# delimiter -> comma
# line terminator -> newline 

exampleFile = open('Data/absfiles/exampleWithHeader.csv')
exampleDictReader = csv.DictReader(exampleFile) # 
for row in exampleDictReader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])
    
# exampleDictReader = csv.DictReader(exampleFile, ['time', 'name', 'amount']) #? made up header name for csv that do not have headers

#? json can hold -> strings, integers, floats, Booleans, lists, dictionaries, and NoneType.

#? json.loads() -> The name means “load string,” not “loads.” :D
# Note that JSON strings always use double quotes. 

#? The json.dumps() function (which means “dump string,” not “dumps”)  :DD

