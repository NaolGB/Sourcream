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
        self.beleg_number = f'{str(uuid.uuid4())[-17:]}'
        self.incoming_material_document_item_number = f'{str(uuid.uuid4())[-17:]}'
        self.purchase_order_schedline_number = f'{str(uuid.uuid4())[-17:]}'
        self.etens = 0
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
            'EKES_json': {},
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

    #ApprovePurchaseOrder
    def approve_purchase_order(
            self,
            aedat,
            ernam,
            ):        
        self.changes(
                objid=str(uuid.uuid4()), 
                objclas='EINKBELEG', 
                udate=aedat, 
                uname= ernam, 
                chngid='I', 
                fname='FRGZU', 
                tabkey=f'{values.mandt}{self.purchase_order_number}', 
                tabname='EKKO', 
                valold=None,
                valnew=None,
            )

    # RestorePurchaseOrderItem
    def restore_purchase_order_item(
            self,
            badat,
            ernam,
            ebelp
            ):
        self.changes(
            objid = str(uuid.uuid4()), 
            objclas ='EINKBELEG', 
            udate = badat, 
            uname = ernam, 
            chngid = 'I', 
            fname = 'LOEKZ', 
            tabkey = f'{values.mandt}{self.purchase_order_number}{ebelp}', 
            tabname = 'EKPO', 
            valold = 'L', 
            valnew = ''
        )

        for k, v in self.tables['EKPO_json'].items():
            if v['EBELN'] == self.purchase_order_number and v['EBELP'] == ebelp:
                self.tables['EKPO_json'][k]['LOEKZ'] = ''

    

    # BlockPurchaseOrderItem
    def block_purchase_order_item(
            self,
            badat,
            ernam,
            ebelp):
        self.changes(
            objid = str(uuid.uuid4()), 
            objclas ='EINKBELEG', 
            udate = badat, 
            uname = ernam, 
            chngid = 'I', 
            fname = 'LOEKZ', 
            tabkey = f'{values.mandt}{self.purchase_order_number}{ebelp}', 
            tabname = 'EKPO', 
            valold = '%', 
            valnew = 'S'
        )

        for k, v in self.tables['EKPO_json'].items():
            if v['EBELN'] == self.purchase_order_number and v['EBELP'] == ebelp:
                self.tables['EKPO_json'][k]['LOEKZ'] = 'S'

    def create_purchase_order_schedule_line(
            self,
            eindt,
            ernam
        ):

        for i in range(len(self.params['matnrs'])):
            self.tables['EKET_json'][str(uuid.uuid4())] = {
                'EBELN': self.purchase_order_schedline_number,
                'EBELP': i,
                'EINDT': eindt,
                'ETENR': i, # Delivery Schedule Line Counter
                'MANDT': values.mandt,
                'MENGE': self.params['quantities'][i], # Quatity Scheduled
                'WEMNG': self.params['quantities'][i], # Quantity of goods received
            }

            #Create purchase order schedule line
            self.changes(
                objid = str(uuid.uuid4()), 
                objclas ='', 
                udate = eindt, 
                uname = ernam, 
                chngid = 'I', #'I' then CreationTime, 'D' DeletionTime 
                fname = 'KEY', 
                tabkey = f'{values.mandt}{self.purchase_order_schedline_number}', 
                tabname = 'EKET', 
                valold = '', 
                valnew = ''
            )


    def set_confirmed_poitem_delivery_date(self,
                                    ernam,
                                   ebelp,
                                   confdate):
        self.etens +=1 
        self.tables['EKES_json'][str(uuid.uuid4())] = {
            'EBELN': self.purchase_order_number,
            'EBELP': ebelp,
            'EBTYP': 'L',
            'EINDT': confdate, # Delivery Date of Vendor Confirmation
            'ERDAT': confdate, # Creation Date of Confirmation
            'ETENS': self.etens, # Sequential Number of Vendor Confirmation
            'EZEIT': helpers.generate_random_time(),
            'MANDT': values.mandt,
            'MENGE': self.params['quantities'][ebelp],
        }

        self.changes(
                objid = str(uuid.uuid4()), 
                objclas ='', 
                udate = confdate, 
                uname = ernam, 
                chngid = 'U', #'I' then CreationTime, 'D' DeletionTime 
                fname = 'EINDT', 
                tabkey = f'{values.mandt}{self.purchase_order_number}{ebelp}{self.etens}', 
                tabname = 'EKES', 
                valold = '', 
                valnew = ''
            )

    def create_vendor_invoice(
            self,
            bldat, 
            ernam,
            cputm):
        self.tables['RBKP_json'][str(uuid.uuid4())] = {
            'BELNR': self.beleg_number,
            'BLDAT': bldat, # document date in document
            'BUKRS': self.params['company_code'],
            'CPUDT': bldat, # Day on which accounting doc was entered
            'CPUTM': cputm, # Time of Entry
            'GJAHR': bldat.year,
            'LIFNR': self.params['lifnr'],
            'MANDT': values.mandt,
            'SGTXT': '', #Item text
            'USNAM': ernam,
            'VGART': 'RD', #Logistics Invoice (requirement)
            'WAERS': 'EUR',
            'ZBD1P': 0,
            'ZBD1T': 0,
            'ZBD2P': 0,
            'ZBD2T': 0,
            'ZBD3T': 0,
            'ZFBDT': 0,
            'ZLSCH': 'T', # No values found
            'ZLSPR': 'D', #No values found for Payment Block Key
            'ZTERM': self.params['payment_term']
        }

        for i in range(len(self.params['matnrs'])):
            self.tables['RSEG_json'][str(uuid.uuid4())] = {
                'BELNR': self.beleg_number,
                'BSTME': self.unit, #Unit of Measurement
                'BUKRS': self.params['company_code'],
                'BUZEI': i, #Document Item in Invoice Document
                'EBELN': self.purchase_order_number,
                'EBELP': i,
                'GJAHR': bldat.year,
                'LFBNR': self.beleg_number,
                'LFGJA': bldat.year, #fiscal year of current perios
                'LFPOS': i, #item of reference document
                'LIFNR': self.params['lifnr'],
                'MANDT': values.mandt,
                'MATNR': self.params['matnrs'][i],
                'MENGE': self.params['quantities'][i],
                'WERKS': self.params['plant'],
                'WRBTR': self.params['prices'][i] * self.params['quantities'][i] #Amount in document currency
            }

            #IncomingMaterialDocumentitem
            self.tables['MSEG_json'][str(uuid.uuid4())] = {
                'BWART':'101', #MaterialTransactionType: '101' THEN 'GoodsReceipt', '602' THEN 'ReverseGoodsIssue'
                'CPUDT_MKPF': bldat,
                'CPUTM_MKPF': cputm,
                'EBELN': self.purchase_order_number,
                'EBELP': i,
                'ERFME': self.unit,
                'KDAUF':'', #Sales Order Number (AP)
                'KDPOS':'', #Item Number in Sales Order (AP)
                'LBKUM': 0, #Total valuated Stock before posting
                'LFBJA': bldat.year,
                'LFBNR': self.beleg_number,
                'LGORT': '',#Storage location T001L
                'LIFNR': self.params['lifnr'],
                'MANDT': values.mandt,
                'MATNR': self.params['matnrs'][i],
                'MBLNR': self.incoming_material_document_item_number,
                'MEINS': self.unit,
                'MENGE': self.params['quantities'][i],
                'MJAHR': bldat.year,
                'SHKZG': 'S', #Debit(H), Credit(S) indicator
                'SJAHR': '', #Material Document Year
                'SMBLN': '', #Number of Material Document
                'SMBLP': 0, # Item in Material Document
                'USNAM_MKPF': ernam,
                'VBELN_IM':'' , #From AP
                'VBELP_IM':0 , #From AP
                'WERKS': self.params['plant'],
                'ZEILE': i,
            }