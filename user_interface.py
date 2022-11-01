import imp

import data_provider as prov
import logger as log


def temperature_view(sens):
    data = prov.get_temperature(sens)
    log.temperature_logger(data)
    return data


def pressure_view(sens):
    data = prov.get_preassure(sens)
    log.pressure_logger(data)
    return data


def wind_speed_view(sens):
    data = prov.get_wind_speed(sens)
    log.wind_speed_logger(data)
    return data

