# Run a test to check SABGOM output
#
# Joseph B. Zambon
# 30-March 2017

sabgom_url='http://omgsrv1.meas.ncsu.edu:8080/thredds/dodsC/fmrc/sabgom/SABGOM_Forecast_Model_Run_Collection_best.ncd'

import pandas as pd
from pydap.client import open_url
import numpy as np
import datetime

sabgom = open_url(sabgom_url)
roms_origin_date = datetime.datetime(2017,1,29,0,0,0)
ocean_time = (np.array(sabgom['time'][:])/24)+datetime.date.toordinal(roms_origin_date)
ocean_time_readable = np.array([ocean_time.size])
for t in range(0,ocean_time.size):
    print(datetime.datetime.fromordinal(int(ocean_time[t]))+datetime.timedelta(hours=(ocean_time[t]-np.floor(ocean_time[t]))*24))


