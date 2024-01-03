import uuid
import values

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
                "AS4VERS": 99, # TODO add custom value
            }

    return {'DD07T_json': DD07T_json}

def doc_types(doc_types=values.sales_doc_types):
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

def organization(sales_orgs=values.sales_orgs):
    TVKBT_json = {}
    TVKOT_json = {}
    TVKOV_json = {}
    TVTWT_json = {}

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
        for key, name in attributes['distribution_channels'].items():
            TVKOV_json[str(uuid.uuid4())] = {
                "MANDT": values.mandt,
                "VKORG": org,
                "VTWEG": key
            }
            
            TVTWT_json[str(uuid.uuid4())] = {
                "MANDT": values.mandt,
                "SPRAS": 'E',
                "VTEXT": name,
                "VTWEG": key
            }
    
    return {'TVKBT_json': TVKBT_json, 'TVKOT_json': TVKOT_json, 'TVKOV_json': TVKOV_json, 'TVTWT_json': TVTWT_json}

def distribution(shipping_conditions=values.shipping_conditions):
    TVSBT_json = {}

    for k, v in shipping_conditions.items():
        TVSBT_json[str(uuid.uuid4())] = {
            "MANDT": values.mandt,
            "SPRAS": 'E',
            "VSBED": k,
            "VTEXT": v
        }

    return {'TVSBT_json': TVSBT_json}

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
