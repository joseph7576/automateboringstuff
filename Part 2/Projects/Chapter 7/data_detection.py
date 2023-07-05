# regext that detects DD/MM/YYYY format.
# D -> 01 - 31, M -> 01 - 12, Y -> 1000 - 2999 ( day or month in single digit have leading zero )
# can detect 31/02/2020 or 31/04/2021

# -> store it in  month, day, year
# validate ->
# April - 4, June - 6, September - 9, and November - 11 have 30 days, February - 2 has 28 days, and the rest of the months have 31 days. 
# February has 29 days in leap years. Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, 
# unless the year is also evenly divisible by 400. 

import re

dateRegex = re.compile(r'(\d{2})/(\d{2})/(\d{4})')

dateData = '31/02/2020 or 31/04/2021 ijaiwefojwe 31/09/2024 - 05/06/2023'


for groups in dateRegex.findall(dateData):
    day, month, year = groups
        
    isLeapYear = True if (int(year) % 4 == 0) or ((int(year) % 100 == 0) and (int(year) % 400 == 0)) else False
    
    # validate month
    if month in ['04', '06', '09', '11'] and int(day) > 30:
        print(f'- Invalid day:{day} for month:{month}, It should be 30!')
    elif month == '02':
        if isLeapYear and int(day) > 29:
            print(f'- Invalid day:{day} for month:{month}, It should be 29! -> LEAP YEAR')
        elif int(day) > 28:
            print(f'- Invalid day:{day} for month:{month}, It should be 28!')
    
    # validate day
    if int(day) > 31:
        print('We have only max 31 days in months!')  
        
    # validate year
    if not 1000 < int(year) < 2999:
        print('Year should be in range 1000 - 2999')
            
        