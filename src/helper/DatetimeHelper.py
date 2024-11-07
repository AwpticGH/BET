from datetime import datetime

class DatetimeHelper:
  @classmethod
  def get_datetime_format(cls, dt: datetime):
    return dt.strftime("%d-%m-%Y %H:%M:%S")