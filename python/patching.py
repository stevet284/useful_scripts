#!/usr/bin/env python

from time import gmtime , strptime

daysdict={ 1 : 'Monday' , 2 : 'Tuesday' , 3 : 'Wednesday' , 4 : 'Thursday ' , 5 : 'Friday' , 6 : 'Saturday' , 7 : 'Sunday' }

time_struct=gmtime()
today_num=time_struct.tm_wday +1
today=daysdict[today_num]


while True:
	patch_time = raw_input("patching Time [01:00] ? ")
	if not patch_time :
		patch_time = "01:00"
	try:
		x=strptime('Sat Jun 06 %s:11 1998'%patch_time)
	except:
		continue
	break

	print "today_num %s today %s" % (today_num , today)
while True:
	patch_day = raw_input("Patch Day [%s] ?"%today).capitalize()
	if not patch_day:
		patch_day = today
	if patch_day in daysdict.values():
		break

print "will patch %s @ %s" % (patch_day , patch_time)



