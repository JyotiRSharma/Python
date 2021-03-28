year = int(input("Enter a year: "))

#
# Write your code here.
#

res = "Leap year"

if year%4 != 0:
    res = "Common year"
    
elif year%100 != 0:
    res = "Leap year"
        
elif year%400 != 0:
    res = "Common year"
        
else:
    res = "Leap year"
    
if year <= 1582:
    res = "Not within the Gregorian calendar period"
    
print(res)
