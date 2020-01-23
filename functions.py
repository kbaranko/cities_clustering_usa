#function used to get desired data from NREL API
def get_energy_info(city, state):
    """input city w/ associated state and return three dictionaries w/ residential, commercial, and industrial energy data"""
    api_key = config.api_key
    city = city.replace(" ", "%20")
    url = f'https://developer.nrel.gov/api/cleap/v1/energy_expenditures_and_ghg_by_sector?city={city}&state_abbr={state}&api_key={api_key}'
    response = requests.get(url)
    print(response)
    info = response.json()
    city = city.replace("%20", " ")
    print(city)
    try: 
        result = info['result']
        city_data = result[city]
        residential = city_data['residential'] 
        commercial = city_data['commercial']
        industrial = city_data['industrial']
        data_res = {}
        data_com = {}
        data_ind = {}
        for (key, value) in residential.items():
            if key == 'housing_units':
                    data_res[key] = value
            elif key == 'elec_mwh':
                    data_res[key] = value
            elif key == 'gas_mcf': 
                    data_res[key] = value
            elif key == 'elec_lb_ghg':
                    data_res[key] = value
            elif key == 'gas_lb_ghg':
                    data_res[key] = value
        for (key, value) in commercial.items():
            if key == 'num_establishments':
                    data_com[key] = value
            elif key == 'elec_mwh':
                    data_com[key] = value
            elif key == 'gas_mcf': 
                    data_com[key] = value
            elif key == 'elec_lb_ghg':
                    data_com[key] = value
            elif key == 'gas_lb_ghg':
                    data_com[key] = value        
        for (key, value) in industrial.items():
            if key == 'num_establishments':
                    data_ind[key] = value
            elif key == 'elec_mwh':
                    data_ind[key] = value
            elif key == 'gas_mcf': 
                    data_ind[key] = value
            elif key == 'elec_lb_ghg':
                    data_ind[key] = value
            elif key == 'gas_lb_ghg':                
                    data_ind[key] = value
        data_res.update( {'city' : city, 'state' : state} )
        data_com.update({'city' : city, 'state' : state} )
        data_ind.update({'city' : city, 'state' : state} )
    except:
        data_res = {'city': city, 'state' : state, 'elec_mwh': 'no_info'} 
        data_com = {'city': city, 'state' : state, 'elec_mwh': 'no_info'}
        data_ind = {'city': city, 'state' : state, 'elec_mwh': 'no_info'}
    return data_res, data_com, data_ind 

#Set of functions to calculate electricity consumption per person and ghg emissions per person 
def elec_person(population, elec_mwh):
    elec_person = None 
    try:
        elec_person = elec_mwh / population
    except:
        elec_mwh == 0 or population == 0
    return elec_person

def ghg_person(population, lb_ghg):
    ghg_person = None
    try:
        ghg_person = lb_ghg / population
    except:
        lb_ghg == 0 or population == 0
    return ghg_person
 
    