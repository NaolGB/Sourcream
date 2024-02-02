import uuid
import random
from datetime import datetime, timedelta
import values, helpers

class Purchasing:
    def __init__(self, params, start_date, index) -> None:
        self.index = index
        self.purchase_req_number = f'{str(uuid.uuid4())[-5:]}{self.index}' # HACK to avoid overflow - short ids are used, to maintain uniqueness - index is used
        self.purchase_order_number = f'{str(uuid.uuid4())[-5:]}{self.index}'
        self.mat_doc_number = f'{str(uuid.uuid4())[-5:]}{self.index}'
        self.unit = values.om_units[random.choice(list(values.om_units.keys()))]['MSEHI']
        self.pr_req_date = start_date
        self.fy = int(start_date.year)
        self.beleg_number = f'{str(uuid.uuid4())[-5:]}{self.index}'
        self.incoming_material_document_item_number = f'{str(uuid.uuid4())[-5:]}{self.index}'
        self.params = params

        self.tables = {
            'EBAN_json': {}, 
            'CDHDR_json': {},
            'CDPOS_json': {},
            'EKKO_json': {},
            'EKPO_json': {},
            'NAST_json': {},
            'MSEG_json': {},
            'EKBE_json': {},
            'RBKP_json': {},
            'RSEG_json': {},
            'EKET_json': {},
        }

    def changes(self, objid, objclas, udate, uname, chngid, fname, tabkey, tabname, valold, valnew, tcode='DEFAULT'):
        changenr = f'{str(uuid.uuid4())[-5:]}{self.index}'
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
        if self.params['has_contract']:
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
            if self.params['item_has_contract'][i]:
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
                    'NETPR': round(self.params['prices'][i]*self.params['quantities'][i], 4),
                    'NETWR': round(self.params['prices'][i]*self.params['quantities'][i], 4),
                    'PEINH': 1,
                    'REPOS': None, # Invoice not recieved
                    "TXZ01": self.params['matnrs'][i],
                    'UEBTO': 0,
                    'WEBRE': None,
                    'WEPOS': None, # Goods receipt indicator
                    'WERKS': self.params['plant'],
                    'ZWERT': round(self.params['prices'][i]*self.params['quantities'][i], 4),
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

    def create_purchase_requisition_item(self, badat, ernam):
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
                "KONNR": self.params['konnr'] if self.params['item_has_contract'][i] else None,
                "KTPNR": i if self.params['item_has_contract'][i] else -1, # HACK not None so as to make pd not consider this a float and add .0 to all
                "LIFNR": self.params['lifnr'],
                "LOEKZ": 'D', # TODO add custom value
                "MANDT": values.mandt,
                "MATNR": None if self.params['is_free_text'] else self.params['matnrs'][i],
                "MEINS": self.unit,
                "MENGE": self.params['quantities'][i],
                "PEINH": 1, # NOTE assumnig price is per item (pcs)
                "PREIS": self.params['prices'][i],
                "STATU": 'N', # NOTE not edited (RFQ not yet created)
                "TXZ01": self.params['free_text_materials'][i] if self.params['is_free_text'] else self.params['matnrs'][i],
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
            'FRGZU': None, # No Approval needed
            'KDATB': datetime.fromtimestamp(0).date(), # HACK 01/01/1970
            'KDATE': datetime.fromtimestamp(0).date(), # HACK 01/01/1970
            'KONNR': self.params['konnr'] if self.params['has_contract'] else None, # TODO check what the effect of using has_contract is vs having multiple POs for contracts
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
                'KONNR': self.params['konnr'] if self.params['item_has_contract'][i] else None,
                'KTMNG': self.params['quantities'][i],
                'KTPNR': i if self.params['item_has_contract'][i] else -1, # HACK not None so as to make pd not consider this a float and add .0 to all
                'LOEKZ': 'D', # HACK
                'MANDT': values.mandt,
                "MATNR": None if self.params['is_free_text'] else self.params['matnrs'][i],
                'MEINS': self.unit,
                'MENGE': self.params['quantities'][i],
                'NETPR': round(self.params['prices'][i]*self.params['quantities'][i], 4),
                'NETWR': round(self.params['prices'][i]*self.params['quantities'][i], 4),
                'PEINH': 1,
                'REPOS': None, # Invoice not recieved
                "TXZ01": self.params['free_text_materials'][i] if self.params['is_free_text'] else self.params['matnrs'][i],
                'UEBTO': 0,
                'WEBRE': None,
                'WEPOS': None, # Goods receipt indicator
                'WERKS': self.params['plant'],
                'ZWERT': round(self.params['prices'][i]*self.params['quantities'][i], 4),
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
        temp_uuid = f'{str(uuid.uuid4())[-5:]}{self.index}'
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
                'LFBJA': self.fy,
                'LFBNR': temp_uuid,
                'LGORT': 'D', # TODO add custom value,
                'LIFNR': self.params['lifnr'],
                'MANDT': values.mandt,
                'MATNR': self.params['matnrs'][i],
                'MBLNR': self.mat_doc_number,
                'MEINS': self.unit,
                'MENGE': self.params['quantities'][i],
                'MJAHR': self.fy,
                'SHKZG': 'S',
                'SJAHR': self.fy,
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
                'GJAHR': self.fy,
                'MANDT': values.mandt,
                'MENGE': self.params['quantities'][i],
                'VGABE': '1',
                'WAERS': 'EUR',
                'WRBTR': round(self.params['prices'][i]*self.params['quantities'][i], 4),
            }
            for k, v in self.tables['EKPO_json'].items():
                if( v['EBELN'] == self.purchase_order_number) and (v['EBELP'] == i):
                    self.tables['EKPO_json'][k]['WEPOS'] = 'X' # Goods Receipt Indicator
# --------------------------------------------------------------------------
            # Logic by Tim von Luecken
            # Create schedule based on desired delivery Status
            # Evtl deviation in days
            days_deviation = helpers.UPTO_MONTH()*self.params['delivery_status'][i]['prob']
            days_temp = round(days_deviation.total_seconds()/(24*3600))
            days_deviation = timedelta(days=days_temp)
            if self.params['delivery_status'][i]['status'] == 'late':
                scheduled_date = cpudt - days_deviation
                cpudt = max(self.pr_req_date + timedelta(days=14), scheduled_date)
            elif self.params['delivery_status'][i]['status'] == 'early':
                cpudt = cpudt + days_deviation

            # Create schedule of po item. If it is neither late nor early, the cpudt
            # has not changed and is the same as the posting date
            self.create_purchase_order_schedule_line(eindt=cpudt, ernam=usnam, ebelp=i)

    def create_purchase_order_schedule_line(self, eindt, ernam, ebelp):
        self.tables['EKET_json'][str(uuid.uuid4())] = {
            'EBELN': self.purchase_order_number,
            'EBELP': ebelp,
            'EINDT': eindt,
            'ETENR': ebelp, # Delivery Schedule Line Counter
            'MANDT': values.mandt,
            'MENGE': self.params['quantities'][ebelp], # Quatity Scheduled
            'WEMNG': self.params['quantities'][ebelp], # Quantity of goods received
        }
        self.changes(
            objid = str(uuid.uuid4()), 
            objclas =str(uuid.uuid4()), 
            udate = eindt, 
            uname = ernam, 
            chngid = 'I', #'I' then CreationTime, 'D' DeletionTime 
            fname = 'KEY', 
            tabkey = f'{values.mandt}{self.purchase_order_number}{ebelp}{ebelp}', 
            tabname = 'EKET', 
            valold = None, 
            valnew = None
        )
# --------------------------------------------------------------------------

    def create_vendor_invoice(self, ernam, cupdt):
        self.tables['RBKP_json'][str(uuid.uuid4())] = {
            'BELNR': self.beleg_number,
            'BLDAT': cupdt, # document date in document
            'BUKRS': self.params['company_code'],
            'CPUDT': cupdt, # Day on which accounting doc was entered
            'CPUTM': helpers.generate_random_time(),
            'GJAHR': self.fy,
            'LIFNR': self.params['lifnr'],
            'MANDT': values.mandt,
            'SGTXT': 'D', # TODO add custom value
            'USNAM': ernam,
            'VGART': 'RD', #Logistics Invoice (requirement)
            'WAERS': 'EUR',
            'ZBD1P': 0,
            'ZBD1T': 0,
            'ZBD2P': 0,
            'ZBD2T': 0,
            'ZBD3T': 0,
            'ZFBDT': self.pr_req_date, # Baseline Date for Due Date Calculation
            'ZLSCH': 'D', # TODO add custom value
            'ZLSPR': 'D', # TODO add custom value
            'ZTERM': self.params['payment_term']  # TODO see if this needs to match when self.change_payment_term is called
        }

        for i in range(len(self.params['matnrs'])):
            self.tables['RSEG_json'][str(uuid.uuid4())] = {
                'BELNR': self.beleg_number,
                'BSTME': self.unit, #Unit of Measurement
                'BUKRS': self.params['company_code'],
                'BUZEI': i, #Document Item in Invoice Document
                'EBELN': self.purchase_order_number,
                'EBELP': i,
                'GJAHR': self.fy,
                'LFBNR': self.mat_doc_number,
                'LFGJA': self.fy,
                'LFPOS': i, #item of reference document
                'LIFNR': self.params['lifnr'],
                'MANDT': values.mandt,
                'MATNR': self.params['matnrs'][i],
                'MENGE': self.params['quantities'][i],
                'WERKS': self.params['plant'],
                'WRBTR': round(self.params['prices'][i]*self.params['quantities'][i], 4),
            }

    def approve_purchase_order(self, aedat, ernam):
        new_value = 'X'        
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas='EINKBELEG', 
            udate=aedat, 
            uname= ernam, 
            chngid='U', 
            fname='FRGZU', 
            tabkey=f'{values.mandt}{self.purchase_order_number}', 
            tabname='EKKO', 
            valold=None,
            valnew=new_value,
        )
        for k, v in self.tables['EKKO_json'].items():
            if( v['EBELN'] == self.purchase_order_number):
                self.tables['EKKO_json'][k]['FRGZU'] = new_value

    def change_payment_term(self, udate, ernam):
        new_value = self.params['new_payment_term']
        self.changes(
                objid=str(uuid.uuid4()), 
                objclas=str(uuid.uuid4()), 
                udate=udate, 
                uname=ernam, 
                chngid='U', 
                fname='ZTERM',
                tabkey=f'{values.mandt}{self.purchase_order_number}', 
                tabname='EKKO', 
                valold=None,
                valnew=new_value,
            )
        
        for k, v in self.tables['EKKO_json'].items():
            if v['EBELN'] == self.purchase_order_number:
                self.tables['EKKO_json'][k]['ZTERM'] = new_value

    def change_vendor(self, udate, ernam):
        new_value = self.params['new_vendor']
        self.changes(
                objid=str(uuid.uuid4()), 
                objclas=str(uuid.uuid4()), 
                udate=udate, 
                uname=ernam, 
                chngid='U', 
                fname='LIFNR',
                tabkey=f'{values.mandt}{self.purchase_order_number}', 
                tabname='EKKO', 
                valold=None, # HACK using none instead of the old EKKO.LIFNR because it is not a requirement in the transformation
                valnew=new_value,
            )
        
        for k, v in self.tables['EKKO_json'].items():
            if v['EBELN'] == self.purchase_order_number:
                self.tables['EKKO_json'][k]['LIFNR'] = new_value
    
    def change_quantity(self, badat, ernam, line_numbers, line_quantities):
        for i, item_position in enumerate(line_numbers):
            self.changes(
                objid = str(uuid.uuid4()), 
                objclas =str(uuid.uuid4()), 
                udate = badat, 
                uname = ernam, 
                chngid = 'U', 
                fname = 'MENGE', 
                tabkey = f'{values.mandt}{self.purchase_order_number}{item_position}', 
                tabname = 'EKPO', 
                valold = None, 
                valnew = line_quantities[i]
            )

            # change line 
            for k, v in self.tables['EKPO_json'].items():
                if (v['EBELN'] == self.purchase_order_number) and (v['EBELP'] == item_position):
                    self.tables['EKPO_json'][k]['MENGE'] = line_quantities[i]

