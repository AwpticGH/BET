from src.helper.DatetimeHelper import DatetimeHelper
from datetime import datetime

class TodoModel:
  def __init__(self, id, title, description):
    self.id = id
    self.title = title
    self.description = description
    self.created_at = DatetimeHelper.get_datetime_format(datetime.now())
    self.deleted_at = None
    self.finished_at = None
    self.updated_at = None