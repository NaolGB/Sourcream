import uuid
import random
from datetime import datetime, timedelta
import values, helpers

class Purchasing:
    def __init__(self, params, start_date, index) -> None:
        self.index = index
        self.purchase_req_number = f'{str(uuid.uuid4())[-15:]}{self.index}' # HACK to avoid overflow - short ids are used, to maintain uniqueness - index is used
        self.purchase_order_number = f'{str(uuid.uuid4())[-15:]}{self.index}'
        self.mat_doc_number = f'{str(uuid.uuid4())[-15:]}{self.index}'
        self.unit = values.om_units[random.choice(list(values.om_units.keys()))]['MSEHI']
        self.lfbja = int(start_date.year)
        self.params = params

        self.tables = {
            'EBAN_json': {},
            'CDHDR_json': {},
            'CDPOS_json': {},
            'EKKO_json': {},
            'EKPO_json': {},
            'NAST_json': {},
            'MSEG_json': {},
            'EKBE_json': {}
        }

    def changes(self, objid, objclas, udate, uname, chngid, fname, tabkey, tabname, valold, valnew, tcode='DEFAULT'):
        changenr = f'{str(uuid.uuid4())[-15:]}{self.index}'
        # HACK one-to-one mapping between CDHDR adn CDPOS even for line items

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

    def create_contract(self, aedat, ernam):
        self.tables['EKKO_json'][str(uuid.uuid4())] = {
            'AEDAT': aedat,
            'BSART': 'F',
            'BSTYP': 'K', # type: Contract
            'BUKRS': self.params['company_code'],
            'EBELN': self.params['konnr'], # Contract's EBELN
            'EKORG': self.params['purchasing_org'],
            'ERNAM': ernam,
            'FRGGR': 'D', # TODO add custom value
            'FRGKE': '2',
            'FRGSX': 'D', # TODO add custom value
            'FRGZU': 'X', # TODO check the effects of this
            'KDATB': datetime.fromtimestamp(0).date(), # HACK 01/01/1970
            'KDATE': datetime.fromtimestamp(0).date(), # HACK 01/01/1970
            'KONNR': self.params['konnr'],
            'LIFNR': self.params['lifnr'],
            'LOEKZ': 'D',
            'MANDT': values.mandt,
            'RESWK': 'D', # HACK
            'STATU': 'B',
            'WAERS': 'EUR',
            'ZBD1P': 0,
            'ZBD1T': 0,
            'ZBD2P': 0,
            'ZBD2T': 0,
            'ZBD3T': 0,
            'ZTERM': self.params['payment_term'],
        }
        self.changes(
                objid=str(uuid.uuid4()), 
                objclas='EINKBELEG', 
                udate=aedat, 
                uname=ernam, 
                chngid='I', 
                fname='KEY', 
                tabkey=f'{values.mandt}{self.params["konnr"]}', 
                tabname='EKKO', 
                valold=None,
                valnew=None,
            )
        for i in range(len(self.params['matnrs'])):
            self.tables['EKPO_json'][str(uuid.uuid4())] = {
                'AEDAT': aedat,
                'AFNAM': self.params['requested_by'],
                'BPRME': 1,
                'BSTYP': 'K',
                'BUKRS': self.params['company_code'],
                'DPDAT': datetime.fromtimestamp(0).date(), # HACK 01/01/1970
                'EBELN': self.params['konnr'],
                'EBELP': i,
                'KONNR': self.params['konnr'],
                'KTMNG': self.params['quantities'][i],
                'KTPNR': i, # NOTE matches with EBAN
                'LOEKZ': 'D', # HACK
                'MANDT': values.mandt,
                'MATNR': self.params['matnrs'][i],
                'MEINS': self.unit,
                'MENGE': self.params['quantities'][i],
                'NETPR': self.params['prices'][i],
                'NETWR': self.params['prices'][i],
                'PEINH': 1,
                'REPOS': None, # Invoice not recieved
                'TXZ01': 'D', # TODO add custom value
                'UEBTO': 0,
                'WEBRE': None,
                'WEPOS': None, # Goods receipt indicator
                'WERKS': self.params['plant'],
                'ZWERT': self.params['prices'][i] # HACK target agreement value the same as total value
            }
            self.changes(
                objid=str(uuid.uuid4()), 
                objclas='EINKBELEG', 
                udate=aedat, 
                uname=ernam, 
                chngid='I', 
                fname='KEY', 
                tabkey=f'{values.mandt}{self.params["konnr"]}{i}', 
                tabname='EKPO', 
                valold=None,
                valnew=None,
            )

    def create_purchase_requisition_item(
            self, 
            badat, 
            ernam,
        ):
        
        for i in range(len(self.params['matnrs'])):
            self.tables['EBAN_json'][str(uuid.uuid4())] = {
                "AFNAM": self.params['requested_by'],
                "BADAT": badat,
                "BANFN": self.purchase_req_number,
                "BNFPO": i,
                "BSTYP": 'B',
                "ERNAM": ernam,
                "ESTKZ": 'B' if ernam == 'BATCH_JOB' else 'D', # Direct procurement if not from material planning
                "FRGKZ": '2', # 'RFQ/purchase order' in values.release_indicators
                "KONNR": self.params['konnr'], # matches with EKKO
                "KTPNR": i, # matches with EKPO
                "LIFNR": self.params['lifnr'],
                "LOEKZ": 'D', # TODO add custom value
                "MANDT": values.mandt,
                "MATNR": self.params['matnrs'][i],
                "MEINS": self.unit,
                "MENGE": self.params['quantities'][i],
                "PEINH": 1, # NOTE assumnig price is per item (pcs)
                "PREIS": self.params['prices'][i],
                "STATU": 'N', # NOTE not edited (RFQ not yet created)
                "TXZ01": 'D', # TODO add custom value
                "WAERS": 'EUR',
                "WERKS": self.params['plant'],
            }

            self.changes(
                objid=str(uuid.uuid4()), 
                objclas='BANF', 
                udate=badat, 
                uname=ernam, 
                chngid='I', 
                fname='KEY', 
                tabkey=f'{values.mandt}{self.purchase_req_number}{i}', 
                tabname='EBAN', 
                valold=None,
                valnew=None,
            )

    def create_purchase_order(self, aedat, ernam):
        self.tables['EKKO_json'][str(uuid.uuid4())] = {
            'AEDAT': aedat,
            'BSART': 'F',
            'BSTYP': 'F',
            'BUKRS': self.params['company_code'],
            'EBELN': self.purchase_order_number,
            'EKORG': self.params['purchasing_org'],
            'ERNAM': ernam,
            'FRGGR': 'D', # TODO add custom value
            'FRGKE': '2',
            'FRGSX': 'D', # TODO add custom value
            'FRGZU': 'X', # TODO check the effects of this
            'KDATB': datetime.fromtimestamp(0).date(), # HACK 01/01/1970
            'KDATE': datetime.fromtimestamp(0).date(), # HACK 01/01/1970
            'KONNR': self.params['konnr'],
            'LIFNR': self.params['lifnr'],
            'LOEKZ': 'D',
            'MANDT': values.mandt,
            'RESWK': 'D', # HACK
            'STATU': 'B',
            'WAERS': 'EUR',
            'ZBD1P': 0,
            'ZBD1T': 0,
            'ZBD2P': 0,
            'ZBD2T': 0,
            'ZBD3T': 0,
            'ZTERM': self.params['payment_term'],
        }
        self.changes(
                objid=str(uuid.uuid4()), 
                objclas='EINKBELEG', 
                udate=aedat, 
                uname=ernam, 
                chngid='I', 
                fname='KEY', 
                tabkey=f'{values.mandt}{self.purchase_order_number}', 
                tabname='EKKO', 
                valold=None,
                valnew=None,
            )
        for i in range(len(self.params['matnrs'])):
            self.tables['EKPO_json'][str(uuid.uuid4())] = {
                'AEDAT': aedat,
                'AFNAM': self.params['requested_by'],
                'BPRME': 1,
                'BSTYP': 'F',
                'BUKRS': self.params['company_code'],
                'DPDAT': datetime.fromtimestamp(0).date(), # HACK 01/01/1970
                'EBELN': self.purchase_order_number,
                'EBELP': i,
                'KONNR': self.params['konnr'],
                'KTMNG': self.params['quantities'][i],
                'KTPNR': i, # NOTE matches with EBAN
                'LOEKZ': 'D', # HACK
                'MANDT': values.mandt,
                'MATNR': self.params['matnrs'][i],
                'MEINS': self.unit,
                'MENGE': self.params['quantities'][i],
                'NETPR': self.params['prices'][i],
                'NETWR': self.params['prices'][i],
                'PEINH': 1,
                'REPOS': None, # Invoice not recieved
                'TXZ01': 'D', # TODO add custom value
                'UEBTO': 0,
                'WEBRE': None,
                'WEPOS': None, # Goods receipt indicator
                'WERKS': self.params['plant'],
                'ZWERT': self.params['prices'][i], # TODO add custom value
            }
            self.changes(
                objid=str(uuid.uuid4()), 
                objclas='EINKBELEG', 
                udate=aedat, 
                uname=ernam, 
                chngid='I', 
                fname='KEY', 
                tabkey=f'{values.mandt}{self.purchase_order_number}{i}', 
                tabname='EKPO', 
                valold=None,
                valnew=None,
            )

    def send_purchase_order(self, usnam, erdat):
        self.tables['NAST_json'][str(uuid.uuid4())] = {
            'AENDE': None,
            'DATVR': erdat,
            'ERDAT': erdat,
            'ERUHR': helpers.generate_random_time(),
            'KAPPL': 'EF',
            'KSCHL': 'NEU',
            'MANDT': values.mandt,
            'OBJKY': self.purchase_order_number,
            'PARNR': 'D', # TODO add custom value
            'PARVW': 'D', # TODO add custom value
            'SPRAS': 'E',
            'TCODE': 'D', # TODO add custom value
            'UHRVR': helpers.generate_random_time(),
            'USNAM': usnam,
        }

    def post_goods_receipt(self, cpudt, usnam, atime):
        temp_uuid = f'{str(uuid.uuid4())[-15:]}{self.index}'
        for i in range(len(self.params['matnrs'])): 
            self.tables['MSEG_json'][str(uuid.uuid4())] = {
                'BWART': '101',
                'CPUDT_MKPF': cpudt,
                'CPUTM_MKPF': atime,
                'EBELN': self.purchase_order_number,
                'EBELP': i,
                'ERFME': self.unit,
                'KDAUF': self.purchase_order_number,
                'KDPOS': i,
                'LBKUM': round(self.params['prices'][i]*self.params['quantities'][i], 4),
                'LFBJA': self.lfbja,
                'LFBNR': temp_uuid,
                'LGORT': 'D', # TODO add custom value,
                'LIFNR': self.params['lifnr'],
                'MANDT': values.mandt,
                'MATNR': self.params['matnrs'][i],
                'MBLNR': self.mat_doc_number,
                'MEINS': self.unit,
                'MENGE': self.params['quantities'][i],
                'MJAHR': self.lfbja,
                'SHKZG': 'S',
                'SJAHR': self.lfbja,
                'SMBLN': self.mat_doc_number,
                'SMBLP': None, # NOTE is not a reversal
                'USNAM_MKPF': usnam,
                'VBELN_IM': None,
                'VBELP_IM': None,
                'WERKS': self.params['plant'],
                'ZEILE': i,
            }
            self.tables['EKBE_json'][str(uuid.uuid4())] = { # TODO check how this affects OutgoingMaterialDocument (in OM/sales_doc_data)
                'BELNR': self.mat_doc_number,
                'BUZEI': i,
                'GJAHR': self.lfbja,
                'MANDT': values.mandt,
                'MENGE': self.params['quantities'][i],
                'VGABE': '1',
                'WAERS': 'EUR',
                'WRBTR': round(self.params['prices'][i]*self.params['quantities'][i], 4),
            }

