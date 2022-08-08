from datetime import datetime
ts = 1660089600000 / 1000

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d'))
print(datetime.utcfromtimestamp(1659897000).strftime('%Y-%m-%d'))