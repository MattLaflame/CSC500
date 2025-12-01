#Ask for the current hour (24 hour clock)
current_hour = int(input('Enter the current hour (24 hour format): '))

#Ask how many hours to wait for the alarm
time_to_alarm = int(input('Enter the number of hours until the alarm goes off: '))

#Calculate what the time will be when the alarm goes off
alarm_time = ((current_hour + time_to_alarm) % 24)

#Output the alarm time
print('The alarm will sound at:', alarm_time)
