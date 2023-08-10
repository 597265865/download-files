import cdsapi
import datetime
import pathlib
import calendar
import os
from subprocess import call
c = cdsapi.Client()
def idmDownloader(task_url, folder_path, file_name):
    idm_engine = "C:\\Program Files (x86)\\Internet Download Manager\\IDMan.exe"
    call([idm_engine, "/d", task_url, "/p", folder_path, "/f", file_name, "/a"])
    call([idm_engine, "/s"])
if __name__ == '__main__':
    pre_begin = datetime.datetime.strptime('20220101', '%Y%m%d')
    end = datetime.datetime.strptime('20230610', '%Y%m%d')
    longers1 = int((end - pre_begin).days) + 1
    var_list = ['divergence', 'fraction_of_cloud_cover', 'geopotential', 'ozone_mass_mixing_ratio',
                'potential_vorticity', 'relative_humidity', 'specific_cloud_ice_water_content',
                'specific_cloud_liquid_water_content', 'specific_humidity', 'specific_rain_water_content',
                'specific_snow_water_content', 'temperature', 'u_component_of_wind', 'v_component_of_wind',
                'vertical_velocity','vorticity']
    for var_i in range(len(var_list)):
        savepath = 'V:\\d\\era5\\' + var_list[var_i]
        pathlib.Path(savepath).mkdir(parents=True,exist_ok=True)
        for i in range(longers1):
            begin_all = pre_begin + datetime.timedelta(days = i)
            path = 'V:\\d\\era5\\' + var_list[var_i]
            filename = 'era5.' + var_list[var_i] + '.' + str(begin_all.strftime('%Y')) + str(begin_all.strftime('%m')) + str(begin_all.strftime('%d')) + r'.nc'
            if not os.path.exists(path + "\\" + filename):
                print(path + "\\" + filename)
                r = c.retrieve('reanalysis-era5-pressure-levels',
                    {'product_type': 'reanalysis', 'grid': '0.25/0.25', 'area': [70, 40, 0, 140,], 'format': 'netcdf',
                     'variable':var_list[var_i],
                    'pressure_level':['1', '50', '100', '125', '150', '175', '200', '225', '250','300', '350', '400',
                                      '450', '500', '550','600', '650', '700', '750', '775', '800','825', '850', '875',
                                      '900', '925', '950', '975', '1000',],
                    'year': str(begin_all.strftime('%Y')), 'month': str(begin_all.strftime('%m')), 'day': str(begin_all.strftime('%d')),
                    'time': [ '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00',
                              '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00',
                              '20:00', '21:00', '22:00', '23:00']},)
                url = r.location
                idmDownloader(url, path, filename)
            print(filename)