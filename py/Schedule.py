__author__ = 'BHS-programing'
import string
def scheduleDefine(input):
    if input == 1:
        return 1,2,3,4,5,6
    elif input == 2:
        return 2,0,4,3,6,5
    elif input == 3:
        return 0,1,3,4,5,6
    elif input == 4:
        return 1,0,2,4,6,5
    elif input == 5:
        return 2,0,1,3,5,6
    elif input == 6:
        return 0,1,2,3,4,6
    else:
        return 1,0,2,3,4,5

masterSchedule = ["APUSH", "STAT", "Calc", "AP Lit", "Python", "Gym/Study","Spanish"]
day = int(input("Enter the schedule day: "))
numbers = scheduleDefine(day)
scheduleNumbers = numbers

for number in scheduleNumbers:
    print(masterSchedule[number])