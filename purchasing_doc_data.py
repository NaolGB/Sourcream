import uuid
import random
from datetime import datetime, timedelta
import values, helpers

class Purchasing:
    def __init__(self, params) -> None:
        self.purchase_req_number = f'{str(uuid.uuid4())[-17:]}' # HACK to avoid overflow when multiple ids being cancatenated
        self.purchase_order_number = f'{str(uuid.uuid4())[-17:]}'
        self.unit = values.om_units[random.choice(list(values.om_units.keys()))]['MSEHI']
        self.params = params

        self.tables = {
            'EBAN_json': {},
            'CDHDR_json': {},
            'CDPOS_json': {},
            'EKKO_json': {},
            'EKPO_json': {},
        }

    def changes(self, objid, objclas, udate, uname, chngid, fname, tabkey, tabname, valold, valnew, tcode='DEFAULT'):
        changenr = f'{str(uuid.uuid4())[-17:]}'
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

    def create_purchase_order(
            self,
            aedat,
            ernam
        ):
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
                'ZWERT': 'D', # TODO add custom value
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

    def send_purchase_order(self):
        pass
