from zipline.utils.calendars import get_calendar,register_calendar
from .exchange_calendar_shsz import SHSZExchangeCalendar
register_calendar("SHSZ", SHSZExchangeCalendar(), force=True)



#singleton in python
shsz_calendar =get_calendar("SHSZ")