# PROBLEM 2

# prompt each user to enter their values
print("USER 1:")
hours1 = int(input("Time in hours: "))
minutes1 = int(input("Time in minutes: "))
seconds1 = int(input("Time in seconds: "))

print("USER 2:")
hours2 = int(input("Time in hours: "))
minutes2 = int(input("Time in minutes: "))
seconds2 = int(input("Time in seconds: "))

# find out who finishes first
if hours1 > hours2:
    print("Person 2 finishes before.")
if hours1 < hours2:
    print("Person 1 finishes before.")
elif hours1 == hours2:
    if minutes1 > minutes2:
        print("Person 2 finishes before.")
    if minutes1 < minutes2:
        print("Person 1 finishes before.")
    elif minutes1 == minutes2:
        if seconds1 > seconds2:
            print("Person 2 finishes before.")
        if seconds1 < seconds2:
            print("Person 1 finishes before.")
        if seconds1 == seconds2:
            print("They finish at the same time")