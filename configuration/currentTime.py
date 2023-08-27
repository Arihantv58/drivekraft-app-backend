from datetime import datetime, timedelta
from  configuration import getTimedelta

def getCurrentTimeInIst():
    return datetime.now() + timedelta( minutes=getTimedelta.getMinDelta(), hours=getTimedelta.getHrDelta())