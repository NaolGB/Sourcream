import uuid
import random
from datetime import datetime, timedelta
import values, helpers

class SalesAndDistribution:
    def __init__(self, vbeln) -> None:
        self.vbeln = vbeln
        self.tables = {
            'VBAK_json': {},
            'VBKD_json': {},
            'VBUK_json': {},
            'VBAP_json': {},
            'VBEP_json': {},
            'LIKP_json': {},
            'LIPS_json': {}
        }

    def create_sales_order(
        self,
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
        all_rejection_reasons=values.om_sales_doc_rejection_reasons,
        all_units=values.om_units,
        all_categories=values.om_sales_doc_item_categories,
        all_routes=values.om_routes,
        all_plants=values.om_plants
    ):
        vdatu = erdat + timedelta(days=days_till_delivery)
        if sales_office == None:
            sales_office = random.choice(list(values.sales_orgs[sales_org]['sales_offices'].keys()))
        if distribution_channel == None:
            distribution_channel = random.choice(list(values.sales_orgs[sales_org]['distribution_channels'].keys()))

        self.tables['VBAK_json'][str(uuid.uuid4())] = {
            "AUART": 'OR',
            "BSTDK": erdat,
            "BSTNK": self.vbeln,
            "BUKRS_VF": customer['company_codes'][0], # TODO make company code dynamic
            "ERDAT": erdat,
            "ERNAM": ernam,
            "ERZET": helpers.generate_random_time(),
            "KKBER": 'D', # TODO add custom value
            "KUNNR": customer['id'],
            "MANDT": values.mandt,
            "NETWR": sum([values.om_materials[materials[i]]['price']*quantities[i] for i, _ in enumerate(materials)]),
            "OBJNR": uuid.uuid4(),
            "VBELN": self.vbeln,
            "VBTYP": 'C',
            "VDATU": vdatu,
            "VKBUR": sales_office,
            "VKORG": sales_org,
            "VSBED": shipping_condition,
            "VTWEG": distribution_channel,
            "WAERK": 'EUR'
        }
        self.tables['VBKD_json'][str(uuid.uuid4())] = {
            "INCO1": 'D', # TODO add custom value
            "INCO2": 'D', # TODO add custom value
            "MANDT": values.mandt,
            "POSNR": '000000',
            "VBELN": self.vbeln,
            "ZTERM": customer['payment_term'],
        }
        self.tables['VBUK_json'][str(uuid.uuid4())] = {
            "BESTK": 'A',
            "GBSTK": 'A',
            "MANDT": values.mandt,
            "VBELN": self.vbeln,
        }

        for i, _ in enumerate(materials):
            x = str(uuid.uuid4())
            self.tables['VBAP_json'][x] = {
                "ABGRU": all_rejection_reasons[random.choice(list(all_rejection_reasons.keys()))]['ABGRU'],
                "BRGEW": 99, # TODO add custom value
                "ERDAT": erdat,
                "ERNAM": ernam,
                "ERZET": helpers.generate_random_time(),
                "FKREL": 'A',
                "GEWEI": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "KDMAT": values.om_materials[materials[i]]['id'],
                "KPEIN": 1,
                "KWMENG": quantities[i],
                "MANDT": values.mandt,
                "MATNR": values.om_materials[materials[i]]['id'],
                "NETPR": values.om_materials[materials[i]]['price'],
                "NETWR": values.om_materials[materials[i]]['price']*quantities[i],
                "NTGEW": 99, # TODO add custom value
                "OBJNR": f'{self.vbeln}{i}',
                "POSNR": i,
                "PSTYV": all_categories[random.choice(list(all_categories.keys()))]['PSTYV'],
                "ROUTE": all_routes[random.choice(list(all_routes.keys()))]['ROUTE'],
                "VBELN": self.vbeln,
                "VGBEL": self.vbeln, # same value as VBUK.VBELN
                "VGPOS": i, # same value as VBUP.VGPOS where VBUP.VBELN is vbeln
                "VGTYP": 'C',
                "VRKME": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "WAERK": 'EUR',
                "WERKS": all_plants[random.choice(list(all_plants.keys()))]['plant_number'],
            }
            self.tables['VBEP_json'][x] = {
                "BMENG": quantities[i], # HACK all qauntities are the same as their confirmed queantities
                "EDATU": erdat,
                "ETENR": i,
                "MANDT": values.mandt,
                "MBDAT": None, # TODO MaterialAvailabilityDate edit later on shipping
                "MEINS": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "POSNR": i,
                "VBELN": self.vbeln,
                "WADAT": None, # TODO MaterialAvailabilityDate edit later on shipping,
            }

    def generate_delivery_document(
            self, 
            ernam, 
            erdat,
            planned_delivery_date,
            picking_date,
            delivery_date,
            confirmation_date,
            materials,
            quantities,
            all_units=values.om_units,
            all_plants=values.om_plants
        ):
        likp_vbeln = str(uuid.uuid4())
        self.tables['LIKP_json'][str(uuid.uuid4())] = {
            "BTGEW": 99, # TODO add custom value
            "ERDAT": erdat,
            "ERNAM": ernam,
            "ERZET": helpers.generate_random_time(),
            "GEWEI": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
            "KODAT": picking_date,
            "KOUHR": helpers.generate_random_time(),
            "KUNNR": self.tables['VBAK_json'][list(self.tables['VBAK_json'].keys())[0]]['KUNNR'], # HACK the 0'th key is the only key in VBAK
            "LFART": 'D', # TODO add custom value
            "LFDAT": delivery_date,
            "MANDT": values.mandt,
            "NTGEW": len(materials)*99, # TODO add custom weight and assign accordingly to VBAP
            "PODAT": confirmation_date,
            "POTIM": helpers.generate_random_time(),
            "VBELN": likp_vbeln,
            "VBTYP": 'J',
            "VOLEH": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
            "VOLUM": 99, # TODO add custom value
            "WADAT": planned_delivery_date,
        }

        for i, _ in enumerate(materials):
            self.tables['LIPS_json'][str(uuid.uuid4())] = {
                "ERDAT": erdat,
                "ERNAM": ernam,
                "ERZET": helpers.generate_random_time(),
                "GEWEI": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "LFIMG": quantities[i],
                "LGORT": 'D',#TODO add custom value
                "MANDT": values.mandt,
                "MATNR": values.om_materials[materials[i]]['id'],
                "NTGEW": 99, # TODO add custom value
                "POSNR": i,
                "VBELN": likp_vbeln,
                "VGBEL": self.vbeln,
                "VGPOS": i,
                "VGTYP": 'C',
                "VOLEH": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "VOLUM": 99, # TODO add custom value
                "VRKME": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "WERKS": all_plants[random.choice(list(all_plants.keys()))]['plant_number'],
            }