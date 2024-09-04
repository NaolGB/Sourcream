import uuid

#Castlelight
# import values_Castlelight as values
#sourcream
from masterdata import values

def domain_fixed_values(dd07t_combinations=values.dd07t_combinations):
    DD07T_json = {}  

    for k, v in dd07t_combinations.items():
        for v_item in v:
            DD07T_json[str(uuid.uuid4())] = {
                "DDLANGUAGE": 'E',
                "DOMNAME": v_item['DOMNAME'],
                "DOMVALUE_L": v_item['DOMVALUE_L'],
                "DDTEXT": v_item['DDTEXT'],
                "AS4LOCAL": 'A',
                "VALPOS": 99, # TODO add custom value
                "AS4VERS": 99, # TODO add custom d
            }

    return {'DD07T_json': DD07T_json}

def sales_doc_types(doc_types=values.om_sales_doc_types):
    TVAK_json = {}
    TVAKT_json = {}

    
    for k, v in doc_types.items():
        TVAK_json[str(uuid.uuid4())] = {
            "AUART": k,
            "KLIMP": 'D',  # TODO -- must match DD07T's TVAK entry
            "MANDT": values.mandt
        }
        TVAKT_json[str(uuid.uuid4())] = {
            "AUART": k,
            "BEZEI": v,
            "MANDT": values.mandt,
            "SPRAS": 'E',
        }

    return {'TVAK_json': TVAK_json, 'TVAKT_json': TVAKT_json}

def sales_organizations(sales_orgs=values.om_sales_orgs):
    TVKBT_json = {}
    TVKOT_json = {}
    TVKOV_json = {}
    TVTWT_json = {}

    unique_distribution_channels = {}

    for org, attributes in sales_orgs.items():
        for key, name in attributes['sales_offices'].items():
            TVKBT_json[str(uuid.uuid4())] = {
                "BEZEI": name,
                "MANDT": values.mandt,
                "SPRAS": 'E',
                "VKBUR" : key
            }
        TVKOT_json[str(uuid.uuid4())] = {
            "MANDT": values.mandt,
            "SPRAS": 'E',
            "VKORG": org,
            "VTEXT": org
        }
        
        # select unique distribution channels
        for key, name in attributes['distribution_channels'].items():
            unique_distribution_channels[key] = name
            TVKOV_json[str(uuid.uuid4())] = {
                "MANDT": values.mandt,
                "VKORG": org,
                "VTWEG": key
            }
    for key, name in unique_distribution_channels.items():
        TVTWT_json[str(uuid.uuid4())] = {
            "MANDT": values.mandt,
            "SPRAS": 'E',
            "VTEXT": name,
            "VTWEG": key
        }
    
    return {'TVKBT_json': TVKBT_json, 'TVKOT_json': TVKOT_json, 'TVKOV_json': TVKOV_json, 'TVTWT_json': TVTWT_json}

def distribution(shipping_conditions=values.shipping_conditions, all_movt_types=values.goods_movement_types):
    TVSBT_json = {}
    T156_json = {}

    for k, v in shipping_conditions.items():
        TVSBT_json[str(uuid.uuid4())] = {
            "MANDT": values.mandt,
            "SPRAS": 'E',
            "VSBED": k,
            "VTEXT": v
        }

    for _, v in all_movt_types.items():
        T156_json[str(uuid.uuid4())] = {
            "BWART": v['code'],
            "MANDT": values.mandt,
            "XSTBW": v['is_reverse'],
        }

    return {'TVSBT_json': TVSBT_json, 'T156_json': T156_json}

def sales_doc_item_categories(all_categories=values.om_sales_doc_item_categories):
    TVAPT_json = {}
    for _, v in all_categories.items():
        TVAPT_json[str(uuid.uuid4())] = {
            "MANDT": values.mandt,
            "PSTYV": v['PSTYV'],
            "SPRAS": 'E',
            "VTEXT": v['VTEXT'],
        }
    
    return {'TVAPT_json': TVAPT_json}

def sales_doc_rejection_reasons(all_rejection_reasons=values.om_sales_doc_rejection_reasons):
    TVAGT_json = {}
    for _, v in all_rejection_reasons.items():
        TVAGT_json[str(uuid.uuid4())] = {
            "ABGRU": v['ABGRU'],
            "BEZEI": v['BEZEI'],
            "MANDT": values.mandt,
            "SPRAS": 'E',
        }

    return {'TVAGT_json': TVAGT_json}

def system_status(all_status=values.om_status):
    TJ02T_json = {}
    for _, v in all_status.items():
        TJ02T_json[str(uuid.uuid4())] = {
            "ISTAT": v['ISTAT'],
            "SPRAS": 'E',
        }

    return {'TJ02T_json': TJ02T_json}

def blocking_reasons(all_billing_blocks=values.om_billing_blocks, all_delivery_blocks=values.om_delivery_blocks):
    TVFST_json = {}
    TVLST_json = {}

    for _, v in all_billing_blocks.items():
        TVFST_json[str(uuid.uuid4())] = {
            "FAKSP": v['FAKSP'],
            "MANDT": values.mandt,
            "SPRAS": 'E',
            "VTEXT": v['VTEXT']
        }
    for _, v in all_delivery_blocks.items():
        TVLST_json[str(uuid.uuid4())] = {
            "LIFSP": v['LIFSP'],
            "MANDT": values.mandt,
            "SPRAS": 'E',
            "VTEXT": v['VTEXT']
        }

    return {'TVFST_json': TVFST_json, 'TVLST_json': TVLST_json}

def releases(all_release_indicators=values.release_indicators):
    T161U_json = {}
    
    for _, v in all_release_indicators.items():
        T161U_json[str(uuid.uuid4())] = {
            "FKZTX": v['FKZTX'],
            "FRGKZ": v['FRGKZ'],
            "MANDT": values.mandt,
            "SPRAS": 'E',
        }
    return {'T161U_json': T161U_json}

def purchasing_doc_types(all_doc_types=values.proc_doc_types):
    T161T_json = {}
    for k, v in all_doc_types.items():
        T161T_json[str(uuid.uuid4())] = {
            "BATXT": v,
            "BSART": 'F', # HACK similar to EKKO.BSART
            "BSTYP": k,
            "MANDT": values.mandt,
            "SPRAS": 'E'
        }
    
    return {'T161T_json': T161T_json}
    
def purchasing_organizations(proc_orgs=values.proc_purchasing_orgs):
    T024E_json = {}

    for org, attributes in proc_orgs.items():
        T024E_json[str(uuid.uuid4())] = {
            "EKORG": org,
            "EKOTX": org,
            "MANDT": values.mandt
        }
    
    return {'T024E_json': T024E_json}