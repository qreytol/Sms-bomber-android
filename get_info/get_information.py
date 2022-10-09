import phonenumbers
from phonenumbers.carrier import name_for_number
from phonenumbers.geocoder import country_name_for_number
from phonenumbers.timezone import time_zones_for_number

full_information = []
def get_information(phone):
    pars = phonenumbers.parse(f'+{phone}', 'UK')
    operator = name_for_number(pars, 'uk')
    full_information.append(operator)
    country = country_name_for_number(pars, 'uk')
    full_information.append(country)
    geo = time_zones_for_number(pars)
    full_information.append(geo)
    return full_information

    
    
