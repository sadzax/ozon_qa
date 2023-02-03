from datetime import datetime
a = '02:46:00'

b = datetime.strptime(a, '%H:%M:%S').time()