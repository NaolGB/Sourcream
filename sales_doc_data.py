import uuid
import random
from datetime import datetime, timedelta
import values, helpers

class SalesAndDistribution:
    def __init__(self, vbeln, materials, quantities, customer) -> None:
        self.vbeln = vbeln
        self.materials = materials
        self.quantities = quantities
        self.likp_vbeln = f'{str(uuid.uuid4())[:random.randint(1, 5)]}{str(uuid.uuid4())[:random.randint(1, 5)]}' # HACK avoid reaching VARCHAR(255) when joining multiple table ids
        self.vbrk_vbeln = f'{str(uuid.uuid4())[:random.randint(1, 5)]}{str(uuid.uuid4())[:random.randint(1, 5)]}'
        self.bkpf_belnr = f'{str(uuid.uuid4())[:random.randint(1, 5)]}{str(uuid.uuid4())[:random.randint(1, 5)]}'

        all_plants=values.om_plants
        self.mblnr = f'{str(uuid.uuid4())[:random.randint(1, 5)]}{str(uuid.uuid4())[:random.randint(1, 5)]}'
        self.mjahr = 2023 # TODO add custom value
        self.customer = customer
        self.plant = all_plants[random.choice(list(all_plants.keys()))]['plant_number'],

        self.tables = {
            'VBAK_json': {},
            'VBKD_json': {},
            'VBUK_json': {},
            'VBAP_json': {},
            'VBEP_json': {},
            'LIKP_json': {},
            'LIPS_json': {},
            'EKBE_json': {}, 
            'MSEG_json': {},
            'VBRK_json': {},
            'VBRP_json': {},
            'BKPF_json': {},
            'BSEG_json': {},
            'CDHDR_json': {},
            'CDPOS_json': {},
            'VBFA_json': {}
        }

    def changes(self, objid, objclas, udate, uname, chngid, fname, tabkey, tabname, valold, valnew, tcode='DEFAULT'):
        changenr = f'{str(uuid.uuid4())[:random.randint(1, 5)]}{str(uuid.uuid4())[:random.randint(1, 5)]}'

        self.tables['CDHDR_json'][str(uuid.uuid4())] = {
            "CHANGENR": changenr,
            "MANDANT": values.mandt,
            "OBJECTCLAS": objclas,
            "OBJECTID": objid,
            "TCODE": tcode,
            "UDATE": udate,
            "USERNAME": uname,
            "UTIME": helpers.generate_random_time(),
        }

        self.tables['CDPOS_json'][str(uuid.uuid4())] = {
            "CHANGENR": changenr,
            "CHNGIND": chngid,
            "FNAME": fname,
            "MANDANT": values.mandt,
            "OBJECTCLAS": objclas,
            "OBJECTID": objid,
            "TABKEY": tabkey,
            "TABNAME": tabname,
            "VALUE_NEW": valnew,
            "VALUE_OLD": valold,
        }

    def record_flow(self, erdat, prev_vbeln, next_vbeln, prev_type, next_type):
        for i, _ in enumerate(self.materials):
            self.tables['VBFA_json'][str(uuid.uuid4())] = {
                    "MANDT": values.mandt,
                    "VBELV": prev_vbeln,
                    "POSNV": i,
                    "VBTYP_V": prev_type,
                    "VBELN": next_vbeln,
                    "POSNN": i,
                    "VBTYP_N": next_type,
                    "ERDAT": erdat,
                    "ERZET": helpers.generate_random_time(),
                    "MATNR": values.om_materials[self.materials[i]]['id']
                }

    def create_sales_order(
        self,
        sales_org,
        sales_office,
        distribution_channel,
        shipping_condition,
        erdat,
        days_till_delivery,
        reqested_delivery_date,
        ernam,
        
        all_rejection_reasons=values.om_sales_doc_rejection_reasons,
        all_units=values.om_units,
        all_categories=values.om_sales_doc_item_categories,
        all_routes=values.om_routes,
    ):
        vdatu = reqested_delivery_date
        if sales_office == None:
            sales_office = random.choice(list(values.sales_orgs[sales_org]['sales_offices'].keys()))
        if distribution_channel == None:
            distribution_channel = random.choice(list(values.sales_orgs[sales_org]['distribution_channels'].keys()))

        self.tables['VBAK_json'][str(uuid.uuid4())] = {
            "AUART": 'OR',
            "BSTDK": erdat,
            "BSTNK": self.vbeln,
            "BUKRS_VF": 'CC01', # TODO make thie comapny code the same as used in KNB1
            "ERDAT": erdat,
            "ERNAM": ernam,
            "ERZET": helpers.generate_random_time(),
            "KKBER": 'D', # TODO add custom value
            "KUNNR": self.customer['id'],
            "MANDT": values.mandt,
            "NETWR": round(sum([values.om_materials[self.materials[i]]['price']*self.quantities[i] for i, _ in enumerate(self.materials)]), 4),
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
            "ZTERM": self.customer['payment_term'],
        }
        self.tables['VBUK_json'][str(uuid.uuid4())] = {
            "BESTK": 'A',
            "GBSTK": 'A',
            "MANDT": values.mandt,
            "VBELN": self.vbeln,
            "KOSTK": 'A' # Not yet processed
        }

        for i, _ in enumerate(self.materials):
            temp_vbeln = f'{str(uuid.uuid4())[:random.randint(1, 5)]}{str(uuid.uuid4())[:random.randint(1, 5)]}'
            self.tables['VBAP_json'][temp_vbeln] = {
                "ABGRU": all_rejection_reasons[random.choice(list(all_rejection_reasons.keys()))]['ABGRU'],
                "BRGEW": 99, # TODO add custom value
                "ERDAT": erdat,
                "ERNAM": ernam,
                "ERZET": helpers.generate_random_time(),
                "FKREL": 'A',
                "GEWEI": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "KDMAT": values.om_materials[self.materials[i]]['id'],
                "KPEIN": 1,
                "KWMENG": self.quantities[i],
                "MANDT": values.mandt,
                "MATNR": values.om_materials[self.materials[i]]['id'],
                "NETPR": values.om_materials[self.materials[i]]['price'],
                "NETWR": round(values.om_materials[self.materials[i]]['price']*self.quantities[i], 4),
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
                "WERKS": self.plant
            }
            self.tables['VBEP_json'][temp_vbeln] = {
                "BMENG": self.quantities[i], # HACK all qauntities are the same as their confirmed queantities
                "EDATU": erdat,
                "ETENR": i,
                "MANDT": values.mandt,
                "MBDAT": None, # TODO MaterialAvailabilityDate edit later on shipping
                "MEINS": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "POSNR": i,
                "VBELN": self.vbeln,
                "WADAT": None, # TODO MaterialAvailabilityDate edit later on shipping,
            }

        self.record_flow( # HACK no quotation before
            erdat=erdat, 
            prev_vbeln=None, 
            prev_type=None, 
            next_vbeln=self.vbeln, 
            next_type='C'
        )
            
    def generate_delivery_document(
            self, 
            ernam, 
            erdat,
            planned_delivery_date,
            picking_date,
            delivery_date,
            confirmation_date,
            all_units=values.om_units,
        ):
        self.tables['LIKP_json'][str(uuid.uuid4())] = {
            "BTGEW": 99, # TODO add custom value
            "ERDAT": erdat,
            "ERNAM": ernam,
            "ERZET": helpers.generate_random_time(),
            "GEWEI": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
            "KODAT": picking_date,
            "KOUHR": None if picking_date == None else helpers.generate_random_time(),
            "KUNNR": self.tables['VBAK_json'][list(self.tables['VBAK_json'].keys())[0]]['KUNNR'], # HACK the 0'th key is the only key in VBAK
            "LFART": 'D', # TODO add custom value
            "LFDAT": delivery_date,
            "MANDT": values.mandt,
            "NTGEW": len(self.materials)*99, # TODO add custom weight and assign accordingly to VBAP
            "PODAT": confirmation_date,
            "POTIM": None if confirmation_date == None else helpers.generate_random_time(),
            "VBELN": self.likp_vbeln,
            "VBTYP": 'J',
            "VOLEH": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
            "VOLUM": 99, # TODO add custom value
            "WADAT": planned_delivery_date,
        }

        for i, _ in enumerate(self.materials):
            self.tables['LIPS_json'][str(uuid.uuid4())] = {
                "ERDAT": erdat,
                "ERNAM": ernam,
                "ERZET": helpers.generate_random_time(),
                "GEWEI": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "LFIMG": self.quantities[i],
                "LGORT": 'D',#TODO add custom value
                "MANDT": values.mandt,
                "MATNR": values.om_materials[self.materials[i]]['id'],
                "NTGEW": 99, # TODO add custom value
                "POSNR": i,
                "VBELN": self.likp_vbeln,
                "VGBEL": self.vbeln,
                "VGPOS": i,
                "VGTYP": 'C',
                "VOLEH": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "VOLUM": 99, # TODO add custom value
                "VRKME": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "WERKS": self.plant
            }
        self.record_flow( 
            erdat=erdat, 
            prev_vbeln=self.vbeln, 
            prev_type='C', 
            next_vbeln=self.likp_vbeln, 
            next_type='J'
        )

    def pick_items(self, usnam, udate):
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas=str(uuid.uuid4()), 
            udate=udate, 
            uname=usnam, 
            chngid='U', 
            fname='KOSTK', 
            tabkey=f'{values.mandt}{self.likp_vbeln}', 
            tabname='VBUK', 
            valold='A',
            valnew='C'
        )
        for k, v in self.tables['VBUK_json'].items():
            if v['VBELN'] == self.vbeln:
                self.tables['VBUK_json'][k]['KOSTK'] = 'C'
        for k, v in self.tables['LIKP_json'].items():
            if v['VBELN'] == self.likp_vbeln:
                self.tables['LIKP_json'][k]['KODAT'] = udate
                self.tables['LIKP_json'][k]['KOUHR'] = helpers.generate_random_time()

    def post_goods_issue(self, cpudt, usnam, all_units=values.om_units):
        for i, _ in enumerate(self.materials): 
            self.tables['MSEG_json'][str(uuid.uuid4())] = {
                "BWART": '601',
                "CPUDT_MKPF": cpudt,
                "CPUTM_MKPF": helpers.generate_random_time(),
                "ERFME": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "KDAUF": self.vbeln,
                "KDPOS": i,
                "LBKUM": round(values.om_materials[self.materials[i]]['price']*self.quantities[i], 4),
                "LGORT": 'D', # TODO add custom value
                "LIFNR": None, # HACK only cosidering OM not Procurement
                "MANDT": values.mandt,
                "MATNR": values.om_materials[self.materials[i]]['id'],
                "MBLNR": self.mblnr,
                "MEINS": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "MENGE": self.quantities[i],
                "MJAHR": self.mjahr,
                "SHKZG": 'H', # Credit
                "SJAHR": self.mjahr,
                "SMBLN": self.mblnr,
                "SMBLP": i,
                "USNAM_MKPF": usnam,
                "VBELN_IM": self.likp_vbeln,
                "VBELP_IM": i,
                "WERKS": self.plant,
                "ZEILE": i,
            }
            self.tables['EKBE_json'][str(uuid.uuid4())] = { # HACK every SO has 1:1 mapping form PO
                "BELNR": self.mblnr,
                "BUZEI": i,
                "GJAHR": self.mjahr,
                "MANDT": values.mandt,
                "MENGE": self.quantities[i],
                "VGABE": 1, # Good Receipt
                "WAERS": 'EUR',
                "WRBTR": round(values.om_materials[self.materials[i]]['price']*self.quantities[i], 4),
            }
        
        self.record_flow( 
            erdat=cpudt, 
            prev_vbeln=self.likp_vbeln, 
            prev_type='J', 
            next_vbeln=self.mblnr, 
            next_type='R'
        )
  
    def create_invoice(self, ernam, erdat):
        self.tables['VBRK_json'][str(uuid.uuid4())] = {
            "ERDAT": erdat,
            "ERNAM": ernam,
            "ERZET": helpers.generate_random_time(),
            "KUNAG": self.customer['id'],
            "MANDT": values.mandt,
            "VBELN": self.vbrk_vbeln,
            "VBTYP": 'M', # M: Invoice
        }

        for i, _ in enumerate(self.materials):
            self.tables['VBRP_json'][str(uuid.uuid4())] = {
                "AUBEL": self.vbeln,
                "AUPOS": i,
                "ERDAT": erdat,
                "ERNAM": ernam,
                "ERZET": helpers.generate_random_time(),
                "MANDT": values.mandt,
                "MATNR": values.om_materials[self.materials[i]]['id'],
                "POSNR": i,
                "VBELN": self.vbrk_vbeln,
                "WERKS": self.plant,
            }
        
        self.tables['BKPF_json'][str(uuid.uuid4())] = {
            "AWKEY": self.vbrk_vbeln,
            "AWTYP": 'VBRK',
            "BELNR": self.bkpf_belnr,
            "BLART": 'D', # TODO add custom value
            "BLDAT": erdat, # FIXME use document creation date
            "BUKRS": 'CC01', # TODO make thie comapny code the same as used in KNB1
            "CPUDT": erdat,
            "CPUTM": helpers.generate_random_time(),
            "GJAHR": self.mjahr,
            "MANDT": values.mandt,
            "USNAM": ernam,
            "WAERS": 'EUR',
            "XREVERSAL": None, # NOTE might need change if P2P or AR is involved
        }

        for i, _ in enumerate(self.materials):
            self.tables['BSEG_json'][str(uuid.uuid4())] = {
                "AUGDT": None,
                "AUGBL": None,
                "AUGGJ": None,
                "BELNR": self.bkpf_belnr,
                "BSCHL": '01',
                "BUKRS": 'CC01', # TODO make thie comapny code the same as used in KNB1
                "BUZEI": i,
                "GJAHR": self.mjahr,
                "KOART": 'D',
                "KUNNR": self.customer['id'],
                "MANDT": values.mandt,
                "MANSP": None,
                "MANST": None,
                "SGTXT": 'D', # TODO add custom value
                "SHKZG": 'S', # Debit Indicator
                "SKFBT": 0,
                "WRBTR": round(sum([values.om_materials[self.materials[i]]['price']*self.quantities[i] for i, _ in enumerate(self.materials)]), 4),
                "WSKTO": 0,
                "ZBD1P": 0, # TODO add custom value
                "ZBD1T": 0, # TODO add custom value
                "ZBD2P": 0, # TODO add custom value
                "ZBD2T": 0, # TODO add custom value
                "ZBD3T": 0, # TODO add custom value
                "ZFBDT": erdat, # TODO add custom value
                "ZTERM": self.customer['payment_term'],
            }


        self.record_flow( 
            erdat=erdat, 
            prev_vbeln=self.mblnr, 
            prev_type='J', 
            next_vbeln=self.vbrk_vbeln, 
            next_type='M'
        )

    def delivery_confirmation(self, usnam, udate):
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas=str(uuid.uuid4()), 
            udate=udate, 
            uname=usnam, 
            chngid='U', 
            fname='PODAT', 
            tabkey=f'{values.mandt}{self.likp_vbeln}', 
            tabname='LIKP', 
            valold=None,
            valnew=udate
        )
        for k, v in self.tables['LIKP_json'].items():
            if v['VBELN'] == self.likp_vbeln:
                self.tables['LIKP_json'][k]['PODAT'] = udate
                self.tables['LIKP_json'][k]['POTIM'] = helpers.generate_random_time()
        
    def clear_debit_invoice(self, cpudt, usnam, cleared_date):
        cleared_bkpf_belnr = f'{str(uuid.uuid4())[:random.randint(1, 5)]}{str(uuid.uuid4())[:random.randint(1, 5)]}'
        self.tables['BKPF_json'][str(uuid.uuid4())] = {
            "AWKEY": self.vbrk_vbeln,
            "AWTYP": 'VBRK',
            "BELNR": cleared_bkpf_belnr,
            "BLART": 'D', # TODO add custom value
            "BLDAT": cpudt, # FIXME use document creation date
            "BUKRS": 'CC01', # TODO make thie comapny code the same as used in KNB1
            "CPUDT": cpudt,
            "CPUTM": helpers.generate_random_time(),
            "GJAHR": self.mjahr,
            "MANDT": values.mandt,
            "USNAM": usnam,
            "WAERS": 'EUR',
            "XREVERSAL": None, # NOTE might need change if P2P or AR is involved
        }

        for i, _ in enumerate(self.materials):
            self.tables['BSEG_json'][str(uuid.uuid4())] = {
                "AUGDT": cleared_date,
                "BELNR": cleared_bkpf_belnr,
                "AUGBL": cleared_bkpf_belnr, # TODO add custom value
                "AUGGJ": self.mjahr,
                "BSCHL": '01',
                "BUKRS": 'CC01', # TODO make thie comapny code the same as used in KNB1
                "BUZEI": i,
                "GJAHR": self.mjahr,
                "KOART": 'D',
                "KUNNR": self.customer['id'],
                "MANDT": values.mandt,
                "MANSP": None,
                "MANST": None,
                "SGTXT": 'D', # TODO add custom value
                "SHKZG": 'S', # Debit Indicator
                "SKFBT": 0,
                "WRBTR": round(sum([values.om_materials[self.materials[i]]['price']*self.quantities[i] for i, _ in enumerate(self.materials)]), 4),
                "WSKTO": 0,
                "ZBD1P": 0, # TODO add custom value
                "ZBD1T": 0, # TODO add custom value
                "ZBD2P": 0, # TODO add custom value
                "ZBD2T": 0, # TODO add custom value
                "ZBD3T": 0, # TODO add custom value
                "ZFBDT": cpudt, # TODO add custom value
                "ZTERM": self.customer['payment_term'],
            }