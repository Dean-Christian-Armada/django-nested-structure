import datetime

_today = datetime.date.today()
today = _today.strftime("%Y-%m-%d")
now = datetime.datetime.now()
fileformat_today = str(_today).replace('-', '')