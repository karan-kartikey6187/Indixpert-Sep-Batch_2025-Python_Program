import datetime

now=datetime.datetime.now()
expected=now+datetime.timedelta(30)
print("30 Days From Now:",expected)

now=datetime.datetime.now()
expected=now+datetime.timedelta(-30)
print("30 Days Back From Now:",expected)

now=datetime.datetime.now()
print("Date Time:",now.strftime("%y/%m/%d,%H:%M:%S"))
