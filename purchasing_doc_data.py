import uuid
import random
from datetime import datetime, timedelta
import values, helpers

class Purchasing:
    def __init__(self, params) -> None:
        self.purchase_req_number = f'{str(uuid.uuid4())[-17:]}' # HACK to avoid overflow when multiple ids being cancatenated
        self.purchase_order_number = f'{str(uuid.uuid4())[-17:]}'
        self.params = params

        self.tables = {
            'EBAN_json': {},
            'CDHDR_json': {},
            'CDPOS_json': {},
            'EKKO_json': {},
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
            req_by, 
            badat, 
            ernam,
            all_units=values.om_units,
        ):
        for i in range(len(self.params['matnrs'])):
            self.tables['EBAN_json'][str(uuid.uuid4())] = {
                "AFNAM": req_by,
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
                "MEINS": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
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
            aedat
        ):
        self.tables['EKKO_json'][str(uuid.uuid4())] = {
            'AEDAT': aedat,
            'BSART': 'F',
            'BSTYP': 'F',
            'BUKRS': self.params['company_code'],
            'EBELN': self.purchase_order_number,
            'EKORG': '',
            'ERNAM': '',
            'FRGGR': '',
            'FRGKE': '',
            'FRGSX': '',
            'FRGZU': '',
            'KDATB': '',
            'KDATE': '',
            'KONNR': '',
            'LIFNR': '',
            'LOEKZ': '',
            'MANDT': '',
            'RESWK': '',
            'STATU': '',
            'WAERS': '',
            'ZBD1P': '',
            'ZBD1T': '',
            'ZBD2P': '',
            'ZBD2T': '',
            'ZBD3T': '',
            'ZTERM': '',
            'AEDAT': '',
            'AFNAM': '',
        }
        