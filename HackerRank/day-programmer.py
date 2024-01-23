

def dayOfProgrammer(year):
    # Write your code here
    feb = 0
    # if(year% 4 == 0 and ((year % 400 == 0) or (year%100!=0))):
    if (year < 1918 and year % 4 == 0) or (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        feb = 29
    else:
        feb = 28

    s = (31 + feb + 31 + 30 + 31 + 30 + 31 + 31)
    result = 256 - s
    return (f"{result}.09.{year}")


n = int(input("Enter the year:"))
r = dayOfProgrammer(n)
print(r)
