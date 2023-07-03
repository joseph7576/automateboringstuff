
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

#   apples Alice  dogs
#  oranges   Bob  cats
# cherries Carol moose
#   banana David goose


def printTable(tableData:list):
    colWidths = [0] * len(tableData)
    
    for col in tableData:
        colWidths[tableData.index(col)] = len(max(col, key=len))
    
    for x in range(len(tableData[0])):
        for y in tableData:
            print(str(tableData[tableData.index(y)][x]).rjust(colWidths[tableData.index(y)]) + ' ', end='')
        print()
        
    
printTable(tableData)