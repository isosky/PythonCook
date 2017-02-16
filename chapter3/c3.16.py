# 处理涉及到时区的日期问题
from datetime import datetime

from pytz import timezone

d = datetime(2012, 12, 21, 9, 30, 0)
print(d)

central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

