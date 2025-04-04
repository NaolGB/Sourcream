import uuid
from datetime import datetime
import random
from helpers import helpers
from values import values_default as values


def users(all_users=values.om_users):
    ADRP_json = {}
    USR02_json = {}
    USR21_json = {}

    for index, (k, v) in enumerate(all_users.items()):
        person_number = f'PRS{index}'
        first_name = k.split()[0]
        last_name = k.split()[1] if k != 'BATCH_JOB' else 'BATCH_JOB'
        ADRP_json[str(uuid.uuid4())] = {
            "CLIENT": values.mandt,
            "DATE_FROM": '20230101',
            "NAME_FIRST": first_name, # First name from username
            "NAME_LAST": last_name, # Last name from username
            "NATION": v['nation'],
            "PERSNUMBER": person_number 
        }
        USR02_json[str(uuid.uuid4())] = {
            "BNAME": k,
            "MANDT": values.mandt,
            "USTYP": v['type']
        }
        USR21_json[str(uuid.uuid4())] = {
            "BNAME": k,
            "MANDT": values.mandt,
            "PERSNUMBER": person_number
        }
    
    return {'ADRP_json': ADRP_json, 'USR02_json': USR02_json, 'USR21_json': USR21_json}

def plants(all_plants=values.om_plants):
    T001W_json = {}
    T005T_json = {}

    unique_countries = {}
    for k, v in all_plants.items():
        T001W_json[str(uuid.uuid4())] = {
            "LAND1": v['country_key'],
            "MANDT": values.mandt,
            "NAME1": v['name'],
            "WERKS": k,
            "BWKEY": random.choice(values.om_valuation_areas),

        }
        unique_countries[v['country_key']] = v['country_name']
    for k, v in unique_countries.items():
        T005T_json[str(uuid.uuid4())] = {
            "LAND1": k,
            "LANDX": v,
            "MANDT": values.mandt,
            "SPRAS": "E"
        }
    
    return {'T001W_json': T001W_json, 'T005T_json': T005T_json}

def company_codes(all_company_codes=values.om_company_codes):
    T001_json = {}
    T001K_json = {}

    for k, v in all_company_codes.items():
        T001_json[str(uuid.uuid4())] = {
            "BUKRS": k,
            "BUTXT": v['BUTXT'],
            "MANDT": values.mandt,
            "WAERS": 'EUR'
        }
    for va in values.om_valuation_areas: # HACK only one valuation area
        T001K_json[str(uuid.uuid4())] = { # connect comapny code with plants
            "BUKRS": k,
            "BWKEY": va, 
            "MANDT": values.mandt
        }

    return {'T001_json': T001_json, 'T001K_json': T001K_json}

def customers_and_vendors(all_customers=values.om_customers, all_users=values.om_users, all_company_codes=values.om_company_codes, all_vendors=values.proc_vendors):
    KNB1_json = {}
    KNA1_json = {}
    LFA1_json = {}
    LFB1_json = {}
    KNKK_json = {}
    S067_json = {}
    KNVV_json = {}

    for index, (k, v) in enumerate (all_customers.items()):
        customer_number = f'CUST{index}'
        KNA1_json[str(uuid.uuid4())] = {
            "ERNAM": random.choice(list(all_users.keys())),
            "KUNNR": customer_number,
            "LAND1": v['country'],
            "MANDT": values.mandt,
            "NAME1": k,
            "ORT01": v['city'],
            "PSTLZ": 'PSTC', # TODO add postal code
            "REGIO": v['region'],
            "STRAS": 'ADD1', # TODO add address liner
            "VBUND": None,
            "LIFSD": None,
            "FAKSD": None
        }

        KNVV_json[str(uuid.uuid4())] = {
            "KUNNR": customer_number,
            "KUNRG": customer_number, 
            "MANDT": values.mandt, 
            "SPART": '10', # for AR starter , division of goods / services join on knvv
            "VKORG": 'EMEA', # to adjust for AR 
            "VTWEG": '10', # to  adjust for AR 
            "ZTERM": 'Z030' # payment term
        }

        KNKK_json[str(uuid.uuid4())] = {
            'AEDAT': helpers.generate_random_date(start_date=datetime(2017, 1, 1), end_date=datetime(2018, 1, 1)), #LastChangeDate
            'AENAM': random.choice(list(all_users.keys())), #LastChangedBy
            'CASHD': helpers.generate_random_date(start_date=datetime(2017, 1, 1), end_date=datetime(2018, 1, 1)), #LastPaymentDate
            'CRBLB': None, # BlockIndicator
            'CTLPC': 'C02', # RiskCategory to adjust 
            'DTREV': None, #CreditLimitLastReviewDate
            'ERDAT': helpers.generate_random_date(start_date=datetime(2015, 1, 1), end_date=datetime(2017, 1, 1)), # CreationTime
            'KKBER': values.credit_control_area, #same as S067 part of ID Credit control area
            'KLIMK': random.randint(10000, 50000), # BaseLimitAmount Customer's credit limit FLOAT to adjust
            'KNKLI': customer_number, #Customer's account number with credit limit reference
            'KUNNR': customer_number, 
            'MANDT': values.mandt,
            }
        
        S067_json[str(uuid.uuid4())]  = {
            'CMWAE': 'EUR', # OpenBillingCurrency
            'KKBER': values.credit_control_area, #part of id Credit control area
            'KNKLI': customer_number, #for join to knkk Customer's account number with credit limit reference
            'MANDT': values.mandt,
            'OFAKW': 0, # unclear Open billing document credit value
            'OLIKW': 0, # unclear Open delivery credit value
            'SPTAG': helpers.generate_random_date(start_date=datetime(2023, 1, 1), end_date=datetime(2024, 12, 31)), # used to order by Period to analyze - current date
        }

        for bukrs in list(all_company_codes.keys()):
            KNB1_json[str(uuid.uuid4())] = {
                "BUKRS": bukrs, # HACK all company codes for all customers
                "ERDAT": helpers.generate_random_date(start_date=datetime(2020, 1, 1), end_date=datetime(2021, 1, 1)),
                "ERNAM": random.choice(list(all_users.keys())),
                "KUNNR": customer_number,
                "MANDT": values.mandt,
                "ZTERM": v['payment_term']
            }

    for index, (k, v) in enumerate(all_vendors.items()):
        vendor_number = f'VND{index}'
        LFA1_json[str(uuid.uuid4())] = {
            "ERNAM": random.choice(list(all_users.keys())),
            "LAND1": v['country'],
            "LIFNR": vendor_number,
            "MANDT": values.mandt,
            "NAME1": k,
            "ORT01": v['city'],
            "VBUND": None,
        }
        for bukrs in list(all_company_codes.keys()):
            LFB1_json[str(uuid.uuid4())] = {
                "BUKRS": bukrs, # HACK all company codes for all vendors
                "ERDAT": helpers.generate_random_date(start_date=datetime(2017, 1, 1), end_date=datetime(2018, 1, 1)),
                "ERNAM": random.choice(list(all_users.keys())),
                "LIFNR": vendor_number,
                "MANDT": values.mandt,
                "ZTERM": v['payment_term']
            }
    
    return {'KNB1_json': KNB1_json, 'KNA1_json': KNA1_json, 'LFA1_json': LFA1_json, 'LFB1_json': LFB1_json, 'KNKK_json': KNKK_json, 'S067_json': S067_json, 'KNVV_json': KNVV_json}

def materials(
        all_material_groups={**values.om_material_groups,**values.proc_material_groups}, # merge both dicts 
        all_users=values.om_users, 
        all_mat_types=values.om_material_types, 
        all_industries=values.om_industries, 
        all_units=values.om_units,
        all_dimensions=values.om_dimensions, 
        all_plants=values.om_plants
    ):
    MAKT_json = {}
    MARA_json = {}
    MARM_json = {}
    MARC_json = {}
    MBEW_json = {}

    for index_0, (_, mat_grps) in enumerate(all_material_groups.items()):
        for index_1, (grp_code, v) in enumerate(mat_grps.items()):
            for index_2, (name, attributes) in enumerate(v['materials'].items()):
                matnr = f'MAT{index_0}{index_1}{index_2}'
                material = name
                price = attributes['price']
                quantity = random.randint(500, 10_000)
                creation_time = helpers.generate_random_date(start_date=datetime(2020, 1, 1), end_date=datetime(2021, 1, 1))

                MAKT_json[str(uuid.uuid4())] = {
                    "MAKTX": material,
                    "MANDT": values.mandt,
                    "MATNR": matnr,
                    "SPRAS": "E"
                }
                MARA_json[str(uuid.uuid4())] = { # MARA is the base Material Master Data - for all plants
                    "ERNAM": random.choice(list(all_users.keys())),
                    "ERSDA": creation_time,
                    "MANDT": values.mandt,
                    "MATKL": grp_code,
                    "MATNR": matnr,
                    "MBRSH": all_industries[random.choice(list(all_industries.keys()))]['MBRSH'],
                    "MEINS": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                    "MTART": all_mat_types[random.choice(list(all_mat_types.keys()))]['MTART'],
                    "PRDHA": 'DEFAULT', # TODO add product heirarchy here
                }
                MARM_json[str(uuid.uuid4())] = {
                    "MANDT": values.mandt,
                    "MATNR": matnr,
                    "MEINH": all_dimensions[random.choice(list(all_dimensions.keys()))]['MSSIE'],
                    "UMREN": 1.0,
                    "UMREZ": 1.0
                }
                # Handling all plants with special logic for certain plants
                for plant in list(all_plants.keys()):
                    MARC_json[str(uuid.uuid4())] = {
                        "AUSDT": helpers.generate_random_date(start_date=datetime(2026, 12, 1), end_date=datetime(2029, 1, 1)), # HACK after all SO and procurement have passed
                        "BESKZ": 'X',
                        "BSTMI": 99,
                        "DISGR": 'D', # TODO add custom value
                        "DISMM": 'D', # TODO add custom value
                        "DISPO": 'D', # TODO add custom value
                        "DZEIT": 99, # TODO add custom value
                        "EISBE": 99, # TODO add custom value
                        "LGRAD": 99, # TODO add custom value
                        "MANDT": values.mandt,
                        "MATNR": matnr,
                        "MMSTD": creation_time,
                        "NFMAT": matnr,
                        "PLIFZ": random.randint(1, 2) if plant in ('PL10','PL07','PL05') else random.randint(2, 7),
                        "STRGR": 'D', # TODO add custom value
                        "WEBAZ": random.randint(1, 2) if plant in ('PL10','PL07','PL05') else random.randint(2, 6),
                        "WERKS": plant
                    }
                MBEW_json[str(uuid.uuid4())] = {
                    "BWKEY": random.choice(values.om_valuation_areas),
                    "BWTAR": None,
                    "LBKUM": quantity,
                    "MANDT": values.mandt,
                    "MATNR": matnr,
                    "PEINH": 99, # TODO add custom value
                    "SALK3": round(quantity*price, 4),
                    "STPRS": price,
                    "VERPR": price,
                    "VPRSV": 'D', # TODO add custom value
                }

    return {'MAKT_json': MAKT_json,'MARA_json': MARA_json,'MARM_json': MARM_json,'MARC_json': MARC_json,'MBEW_json': MBEW_json}

def material_support(
        all_units=values.om_units, 
        all_dimensions=values.om_dimensions, 
        all_material_groups={**values.om_material_groups,**values.proc_material_groups}, # merge both dicts
        all_mat_types=values.om_material_types,
        all_industries=values.om_industries
    ):
    T006_json = {}
    T006D_json = {}
    T023T_json = {}
    T134T_json = {}
    T137T_json = {}

    for _, v in all_units.items():
        T006_json[str(uuid.uuid4())] = {
            "DIMID": v['DIMID'],
            "MANDT": values.mandt,
            "MSEHI": v['MSEHI'], 
            "EXP10": None,
            "NENNR": None,
            "ZAEHL": None,
        }
    for _, v in all_dimensions.items():
        T006D_json[str(uuid.uuid4())] = {
            "DIMID": v['DIMID'],
            "MANDT": values.mandt,
            "MSSIE": v['MSSIE']
        }

    for _, mat_grps in all_material_groups.items():
        for k in list(mat_grps.keys()):
            T023T_json[str(uuid.uuid4())] = {
                "MANDT": values.mandt,
                "MATKL": k,
                "SPRAS": "E",
                "WGBEZ": mat_grps[k]['name'],
            }
    for _, v in all_mat_types.items():
        T134T_json[str(uuid.uuid4())] = {
            "MANDT": values.mandt,
            "MTART": v['MTART'],
            "SPRAS": "E"
        }
    for _, v in all_industries.items():
        T137T_json[str(uuid.uuid4())] = {
            "MANDT": values.mandt,
            "MBRSH": v['MBRSH'],
            "SPRAS": "E"
        }

    return {'T006_json': T006_json,'T006D_json': T006D_json,'T023T_json': T023T_json,'T134T_json': T134T_json,'T137T_json': T137T_json}

def routes(all_routes=values.om_routes):
    TVRO_json = {}
    for _, v in all_routes.items():
        TVRO_json[str(uuid.uuid4())] = {
            "MANDT": values.mandt,
            "ROUTE": v['ROUTE'],
            "TRAZTD": v['TRAZTD'],
        }
    
    return {'TVRO_json': TVRO_json}

def currencyexchanges():
    TCURR_json = {}
    TCURF_json = {}
    TCURX_json = {}

    validityperiods = ['79759898','79769898']  # 20240101 and 20230101

    for i in validityperiods:
        TCURR_json[str(uuid.uuid4())] = {
            "FCURR": 'EUR',
            "FFACT": 1,
            "GDATU": i,
            "KURST": 'EURX',
            "MANDT": values.mandt,
            "TCURR": 'EUR',
            "TFACT": 1,
            "UKURS": 1
        }

        TCURF_json[str(uuid.uuid4())] = {
        "FCURR":'EUR',
        "FFACT": 1,
        "GDATU": i,
        "KURST": 'EURX',
        "MANDT": values.mandt,
        "TCURR": 'EUR',
        "TFACT": 1,
        }
    
    TCURX_json[str(uuid.uuid4())] = {
	"CURRDEC": 2,
	"CURRKEY": 'EUR'
    }

    return {'TCURR_json': TCURR_json, 'TCURF_json': TCURF_json, 'TCURX_json': TCURX_json}

def cust_mastercreditmgnt():
    T014_json = {}
    T014_json[str(uuid.uuid4())] = {
          "WAERS": 'EUR',
          "MANDT": values.mandt,
          "KKBER": values.credit_control_area # used for join to knkk
    }

    return {'T014_json': T014_json}