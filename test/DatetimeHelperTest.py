from src.helper.DatetimeHelper import DatetimeHelper
from datetime import datetime

def test_datetime_formatting():
  my_dt = datetime(year=2024, month=11, day=7, hour=22, minute=8, second=21)
  formatted_dt = DatetimeHelper.get_datetime_format(my_dt)
  
  assert formatted_dt == "07-11-2024 22:08:21"