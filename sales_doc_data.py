import uuid
import random
from datetime import datetime, timedelta
import values, helpers

def sales_order(
    sales_org,
    sales_office,
    distribution_channel,
    shipping_condition,
    erdat,
    days_till_delivery,
    ernam,
    customer,
    materials,
    quantities,
):
    vbeln = uuid.uuid4()
    VBAK_json = {}
    VBKD_json = {}
    VBUK_json = {}

    vdatu = erdat + timedelta(days=days_till_delivery)
    if sales_office == None:
        sales_office = random.choice(list(values.sales_orgs[sales_org]['sales_offices'].keys()))
    if distribution_channel == None:
        distribution_channel = random.choice(list(values.sales_orgs[sales_org]['distribution_channels'].keys()))

    VBAK_json[str(uuid.uuid4())] = {
        "AUART": 'OR',
        "BSTDK": erdat,
        "BSTNK": vbeln,
        "BUKRS_VF": customer['company_code'],
        "ERDAT": erdat,
        "ERNAM": ernam,
        "ERZET": helpers.generate_random_time(),
        "KKBER": 'D', # TODO add custom value
        "KUNNR": customer['id'],
        "MANDT": values.mandt,
        "NETWR": sum([values.om_materials[materials[i]]['price']*quantities[i] for i, _ in enumerate(materials)]),
        "OBJNR": uuid.uuid4(),
        "VBELN": vbeln,
        "VBTYP": 'C',
        "VDATU": vdatu,
        "VKBUR": sales_office,
        "VKORG": sales_org,
        "VSBED": shipping_condition,
        "VTWEG": distribution_channel,
        "WAERK": 'EUR'
    }
    VBKD_json[str(uuid.uuid4())] = {
        "INCO1": 'D', # TODO add custom value
        "INCO2": 'D', # TODO add custom value
        "MANDT": values.mandt,
        "POSNR": '000000',
        "VBELN": vbeln,
        "ZTERM": customer['payment_term'],
    }
    VBUK_json[str(uuid.uuid4())] = {
        "BESTK": 'A',
        "GBSTK": 'A',
        "MANDT": values.mandt,
        "VBELN": vbeln,
    }

    return {'VBAK_json': VBAK_json, 'VBKD_json': VBKD_json, 'VBUK_json': VBUK_json}
