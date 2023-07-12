from datetime import datetime
from pytz import timezone

d = datetime(2012, 12, 21, 9, 30, 0)
print(d)

# localize the date for Chicago
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

shanghai = timezone('Asia/Shanghai')
shanghai_d = shanghai.localize(d)
print(shanghai_d)