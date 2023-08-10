import cdsapi
import datetime
import pathlib
import calendar,os
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
    var_list = ['10m_u_component_of_wind', '10m_v_component_of_wind', '2m_dewpoint_temperature',
            '2m_temperature', 'convective_available_potential_energy', 'convective_inhibition',
            'convective_precipitation', 'high_cloud_cover', 'instantaneous_10m_wind_gust',
            'instantaneous_moisture_flux', 'k_index', 'large_scale_precipitation',
            'low_cloud_cover', 'mean_sea_level_pressure', 'mean_top_net_long_wave_radiation_flux',
            'mean_top_net_short_wave_radiation_flux', 'sea_surface_temperature', 'surface_latent_heat_flux',
            'surface_net_solar_radiation', 'surface_net_solar_radiation_clear_sky', 'surface_pressure',
            'surface_sensible_heat_flux', 'total_cloud_cover', 'total_column_water', 'medium_cloud_cover',
            'total_column_water_vapour', 'total_precipitation', 'vertical_integral_of_divergence_of_kinetic_energy_flux',
            'vertical_integral_of_divergence_of_moisture_flux', 'vertically_integrated_moisture_divergence', 'zero_degree_level',]
    for var_i in range(len(var_list)):
        savepath = 'V:\\d\\era5\\' + var_list[var_i]
        pathlib.Path(savepath).mkdir(parents=True,exist_ok=True)
        for i in range(longers1):
            begin_all = pre_begin + datetime.timedelta(days = i)
            path = 'V:\\d\\era5\\' + var_list[var_i]
            filename = 'era5.' + var_list[var_i] + '.' + str(begin_all.strftime('%Y')) + str(begin_all.strftime('%m')) + str(begin_all.strftime('%d')) + r'.nc'
            if not os.path.exists(path + "\\" + filename):
                print(path + "\\" + filename)
                r = c.retrieve('reanalysis-era5-single-levels',
                        {'product_type': 'reanalysis', 'grid': '0.25/0.25', 'area': [70, 40, 0, 140,], 'format': 'netcdf', 'variable':var_list[var_i],
                        'year': str(begin_all.strftime('%Y')), 'month': str(begin_all.strftime('%m')), 'day': str(begin_all.strftime('%d')),
                        'time': [ '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']},)
                url = r.location
                idmDownloader(url, path, filename)
            print(filename)