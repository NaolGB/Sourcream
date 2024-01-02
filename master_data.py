import uuid
from datetime import datetime
import random

import values, helpers


def users(all_users=values.om_users):
    ADRP_json = {}
    USR02_json = {}
    USR21_json = {}

    for k, v in all_users.items():
        person_number = str(uuid.uuid4())
        ADRP_json[str(uuid.uuid4())] = {
            "CLIENT": values.mandt,
            "DATE_FROM": '00010101',
            "NAME_FIRST": k, # TODO split bname
            "NAME_LAST": k, # TODO split bname
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

def customers_and_vendors(all_customers=values.om_customers, all_users=values.om_users):
    KNB1_json = {}
    KNA1_json = {}
    T001_json = {}
    T001K_json = {}

    for k, v in all_customers.items():
        customer_number = v['id']
        KNB1_json[str(uuid.uuid4())] = {
            "BUKRS": v['company_code'],
            "ERDAT": helpers.generate_random_date(start_date=datetime(2021, 1, 1), end_date=datetime(2022, 1, 1)),
            "ERNAM": random.choice(list(all_users.keys())),
            "KUNNR": customer_number,
            "MANDT": values.mandt,
            "ZTERM": v['payment_term']
        }
        KNA1_json[str(uuid.uuid4())] = {
            "ERNAM": random.choice(list(all_users.keys())),
            "KUNNR": customer_number,
            "LAND1": v['country'],
            "MANDT": values.mandt,
            "NAME1": k,
            "ORT01": v['city'],
            "PSTLZ": 'PSTC', # TODO add postal code
            "REGIO": v['region'],
            "STRAS": 'ADD1', # TODO add address liner
            "VBUND": None
        }
        T001_json[str(uuid.uuid4())] = {
            "BUKRS": v['company_code'],
            "BUTXT": f"{k}-{v['company_code']}",
            "MANDT": values.mandt,
            "WAERS": 'EUR'
        }
        T001K_json[str(uuid.uuid4())] = {
            "BUKRS": v['company_code'],
            "BWKEY": 'D', # TODO add custom value - must match T100W.BWKEY
            "MANDT": values.mandt
        }
    
    return {'KNB1_json': KNB1_json, 'KNA1_json': KNA1_json, 'T001_json': T001_json, 'T001K_json': T001K_json}

def plants(all_plants=values.om_plants):
    T001W_json = {}
    T005T_json = {}
    for k, v in all_plants.items():
        T001W_json[str(uuid.uuid4())] = {
            "LAND1": v['country_key'],
            "MANDT": values.mandt,
            "NAME1": k,
            "WERKS": v['plant_number'],
            "BWKEY": 'D' # TODO add valuation area

        }
        T005T_json[str(uuid.uuid4())] = {
            "LAND1": v['country_key'],
            "LANDX": v['country_name'],
            "MANDT": values.mandt,
            "SPRAS": "E"
        }
    
    return {'T001W_json': T001W_json, 'T005T_json': T005T_json}

def materials(all_materials=values.om_materials, all_users=values.om_users):
    MAKT_json = {}
    MARA_json = {}
    MARM_json = {}
    T006_json = {}
    T006D_json = {}
    T023T_json = {}
    T134T_json = {}
    T137T_json = {}
    MARC_json = {}
    MBEW_json = {}

    for k, v in all_materials.items():
        matnr = v['id']
        quantity = random.randint(500, 1500)
        creation_time = helpers.generate_random_date(start_date=datetime(2021, 1, 1), end_date=datetime(2022, 1, 1)),
        MAKT_json[str(uuid.uuid4())] = {
            "MAKTX": k,
            "MANDT": values.mandt,
            "MATNR": matnr,
            "SPRAS": "E"
        }
        MARA_json[str(uuid.uuid4())] = { # MARA is the base Material Master Data - for all plants
            "ERNAM": random.choice(list(all_users.keys())),
            "ERSDA": creation_time,
            "MANDT": values.mandt,
            "MATKL": 'DEFAULT', # TODO add material group
            "MATNR": matnr,
            "MBRSH": 'D', # TODO add industry sector
            "MEINS": 'UNT', 
            "MTART": 'DEFT', # TODO add material type here
            "PRDHA": 'DEFAULT', # TODO add product heirarchy here
        }
        MARM_json[str(uuid.uuid4())] = {
            "MANDT": values.mandt,
            "MATNR": matnr,
            "MEINH": 'ST'
        }
        T006_json[str(uuid.uuid4())] = {
            "DIMID": 'AAAADL',
            "MANDT": values.mandt,
            "MSEHI": 'UNT'
        }
        T006D_json[str(uuid.uuid4())] = {
            "DIMID": 'AAAADL',
            "MANDT": values.mandt,
            "MSSIE": 'ST'
        }
        T023T_json[str(uuid.uuid4())] = {
            "MANDT": values.mandt,
            "MATKL": 'DEFAULT', # TODO add material group - must match MARA.MATKL
            "SPRAS": "E",
            "WGBEZ": 'DEFAULT', # TODO add group decriptin
        }
        T134T_json[str(uuid.uuid4())] = {
            "MANDT": values.mandt,
            "MTART": 'DEFT', # TODO add material type here - must match MARA.MTART
            "SPRAS": "E"
        }
        T137T_json[str(uuid.uuid4())] = {
            "MANDT": values.mandt,
            "MBRSH": 'D', # TODO add industry sector - must match MARA.MBRSH
            "SPRAS": "E"
        }
        MARC_json[str(uuid.uuid4())] = {
            "AUSDT": helpers.generate_random_date(start_date=datetime(2024, 1, 1), end_date=datetime(2025, 1, 1)), # HACK after all SO and procurement have passed
            "BESKZ": v['type'],
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
            "PLIFZ": v['delivery_takes_days'],
            "STRGR": 'D', # TODO add custom value
            "WEBAZ": v['goods_receipt_processing_days'],
            "WERKS": 'PL01', # TODO make this material dependent than just UK-1 (check values.om_plants)
        }
        MBEW_json[str(uuid.uuid4())] = {
            "BWKEY": 'D', # TODO add custom value - must match T100W.BWKEY
            "BWTAR": None,
            "LBKUM": quantity,
            "MANDT": values.mandt,
            "MATNR": matnr,
            "PEINH": 99, # TODO add custom value
            "SALK3": quantity*v['price'],
            "STPRS": v['price'],
            "VERPR": v['price'],
            "VPRSV": 'D', # TODO add custom value
        }

    return {'MAKT_json': MAKT_json,'MARA_json': MARA_json,'MARM_json': MARM_json,'T006_json': T006_json,'T006D_json': T006D_json,'T023T_json': T023T_json,'T134T_json': T134T_json,'T137T_json': T137T_json,'MARC_json': MARC_json,'MBEW_json': MBEW_json}