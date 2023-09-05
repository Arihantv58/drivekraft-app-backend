import logging
from datetime import date


#to to build a cron which runs at 12 and creates a new file basically which calls this logFileCongig fun
def logFileCongig():
    dte = date.today()
    logging.basicConfig(filename='drivekraft-app-backend/log/record' + str(dte) + '.log', level=logging.DEBUG,
                         format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
    # logging.basicConfig(filename='log/record' + '.log', level=logging.DEBUG,
    #                      format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
    return



