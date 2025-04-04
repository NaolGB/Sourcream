import uuid
import random
from datetime import datetime, timedelta
from helpers import helpers
from values import values_default as values

class SalesAndDistribution:
    def __init__(self, vbeln, params, start_date: datetime, index) -> None:
        self.index = index
        self.vbeln = vbeln
        self.params = params
        self.objnr = f'{str(uuid.uuid4())[-17:]}' # HACK to avoid overflow when multiple ids being cancatenated
        self.likp_vbeln = f'{str(uuid.uuid4())[-11:]}' 
        self.vbrk_vbeln = f'{str(uuid.uuid4())[-11:]}'
        self.bkpf_belnr = f'{str(uuid.uuid4())[-11:]}'
        self.mblnr = f'{str(uuid.uuid4())[-11:]}'
        self.start_date = start_date
        self.mjahr = int(start_date.year)
        self.purchase_order_number = f'{str(uuid.uuid4())[-5:]}{self.index}'
        self.unit = values.om_units[random.choice(list(values.om_units.keys()))]['MSEHI']

        self.tables = {
            'BKPF_json': {},
            'BSEG_json': {},
            'CDHDR_json': {},
            'CDPOS_json': {},
            'EKBE_json': {}, 
            'EKKO_json': {},
            'EKPO_json': {},
            'JCDS_json': {},
            'LIKP_json': {},
            'LIPS_json': {},
            'MSEG_json': {},
            'NAST_json':{},
			'VBAK_json': {},
            'VBAP_json': {},
            'VBEP_json': {},
            'VBFA_json': {},
            'VBKD_json': {},
            'VBRK_json': {},
            'VBRP_json': {},
            'VBUK_json': {},
            'VTTK_json': {},
            'VTTP_json': {},
        }

    def changes(self, objid, objclas, udate, utime, uname, chngid, fname, tabkey, tabname, valold, valnew, tcode='DEFAULT'):
        changenr = f'{str(uuid.uuid4())[-11:]}'
        # HACK one-to-one mapping between CDHDR adn CDPOS even for line items

        self.tables['CDHDR_json'][str(uuid.uuid4())] = {
            "CHANGENR": changenr,
            "MANDANT": values.mandt,
            "OBJECTCLAS": objclas,
            "OBJECTID": objid,
            "TCODE": tcode,
            "UDATE": udate,
            "USERNAME": uname,
            "UTIME": utime,
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
        for i in range(len(self.params['matnrs'])):
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
                    "MATNR": self.params['matnrs'][i]
                }

    def create_sales_order(
        self,
        shipping_condition,
        erdat,
        reqested_delivery_date,
        ernam,
        atime,
        
        all_units=values.om_units,
        all_categories=values.om_sales_doc_item_categories,
        all_routes=values.om_routes,
    ):
        self.tables['VBAK_json'][str(uuid.uuid4())] = {
            "AUART": self.params['sales_doc_type'],
            "BSTDK": erdat,
            "BSTNK": self.vbeln,
            "BUKRS_VF": self.params['company_code'],
            "ERDAT": erdat,
            "ERNAM": ernam,
            "ERZET": atime,
            "KKBER": 'D', # TODO add custom value
            "KUNNR": self.params['kunnr'],
            "MANDT": values.mandt,
            "NETWR": round(sum([self.params['prices'][i]*self.params['quantities'][i] for i in range(len(self.params['matnrs']))]), 4),
            "OBJNR": self.objnr,
            "VBELN": self.vbeln,
            "VBTYP": 'C',
            "VDATU": reqested_delivery_date,
            "VKBUR": self.params['sales_office'],
            "VKORG": self.params['sales_org'],
            "VSBED": shipping_condition,
            "VTWEG": self.params['distribution_channel'],
            "WAERK": 'EUR',
            "LIFSK": None,
            'FAKSK': None
        }
        self.tables['VBKD_json'][str(uuid.uuid4())] = {
            "INCO1": 'D', # TODO add custom value
            "INCO2": 'D', # TODO add custom value
            "MANDT": values.mandt,
            "POSNR": '000000',
            "VBELN": self.vbeln,
            "ZTERM": self.params['payment_term'],
        }
        self.tables['VBUK_json'][str(uuid.uuid4())] = {
            "BESTK": 'A',
            "GBSTK": 'A',
            "MANDT": values.mandt,
            "VBELN": self.vbeln,
            "KOSTK": 'A', # Not yet processed
            "CMGST": None, # Credit Block
        }

        for i in range(len(self.params['matnrs'])):
            temp_vbeln = f'{str(uuid.uuid4())[-11:]}'
            self.tables['VBAP_json'][temp_vbeln] = {
                "ABGRU": None, # 'D' HACK
                "BRGEW": 99, # TODO add custom value
                "ERDAT": erdat,
                "ERNAM": ernam,
                "ERZET": str(helpers.add_random_hours(1, atime)),
                "FKREL": 'A',
                "GEWEI": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "KDMAT": self.params['matnrs'][i],
                "KPEIN": 1,
                "KWMENG": self.params['quantities'][i],
                "MANDT": values.mandt,
                "MATNR": self.params['matnrs'][i],
                "NETPR": self.params['prices'][i],
                "NETWR": round(self.params['prices'][i]*self.params['quantities'][i], 4),
                "NTGEW": 99, # TODO add custom value
                "OBJNR": self.objnr,
                "POSNR": i,
                "PSTYV": all_categories[random.choice(list(all_categories.keys()))]['PSTYV'],
                "ROUTE": all_routes[random.choice(list(all_routes.keys()))]['ROUTE'],
                "VBELN": self.vbeln,
                "VGBEL": self.vbeln, # same value as VBUK.VBELN
                "VGPOS": i, # same value as VBUP.VGPOS where VBUP.VBELN is vbeln
                "VGTYP": 'C',
                "VRKME": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "WAERK": 'EUR',
                "WERKS": self.params['plant'],
                'FAKSP': None
            }
            self.tables['VBEP_json'][temp_vbeln] = {
                "BMENG": self.params['quantities'][i], # HACK all qauntities are the same as their confirmed queantities
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

    def set_credit_block(self, udate, usnam):
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas=str(uuid.uuid4()), 
            udate=udate, 
            utime = helpers.generate_random_time(),
            uname=usnam, 
            chngid='U', 
            fname='CMGST', 
            tabkey=f'{values.mandt}{self.vbeln}', 
            tabname='VBUK', 
            valold='B',
            valnew='B'
        )

        for k, v in self.tables['VBUK_json'].items():
            if v['VBELN'] == self.vbeln:
                self.tables['VBUK_json'][k]['CMGST'] = 'B'
     
    def release_credit_block(self, udate, usnam):
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas=str(uuid.uuid4()), 
            udate=udate, 
            utime = helpers.generate_random_time(),
            uname=usnam, 
            chngid='U', 
            fname='CMGST', 
            tabkey=f'{values.mandt}{self.vbeln}', 
            tabname='VBUK', 
            valold='B',
            valnew='D'
        )

        for k, v in self.tables['VBUK_json'].items():
            if v['VBELN'] == self.vbeln:
                self.tables['VBUK_json'][k]['CMGST'] = 'D'

    def reject_sales_order(self, udate, usnam, all_rejection_reasons=values.om_sales_doc_rejection_reasons):
        for i  in range(len(self.params['matnrs'])):
            # new_val = all_rejection_reasons[random.choice(list(all_rejection_reasons.keys()))]['ABGRU']
            new_val = '02' if random.random() < 0.7 else random.choice(list(values.om_sales_doc_rejection_reasons.keys()))
            #new_val = 'Z0' if random.random() < 0.7 else 'Z1'
            self.changes(
                objid=str(uuid.uuid4()), 
                objclas='VERKBELEG', 
                udate=udate, 
                utime = helpers.generate_random_time(),
                uname=usnam, 
                chngid='U', 
                fname='ABGRU', 
                tabkey=f'{values.mandt}{self.vbeln}{i}', 
                tabname='VBAP', 
                valold=None,
                #valold='D', # HACK
                valnew=new_val,
            )

            for k, v in self.tables['VBAP_json'].items():
                if (v['VBELN'] == self.vbeln) and (v['POSNR'] == i):
                    self.tables['VBAP_json'][k]['ABGRU'] = new_val

            if new_val == '01':  #ROOT CAUSE delivery changes if customer cancellation
                newdate = helpers.add_random_days(4, 15, udate)
                self.changes(
                    objid=str(uuid.uuid4()), 
                    objclas='VERKBELEG', 
                    udate=udate, 
                    utime = helpers.generate_random_time(),
                    uname=usnam, 
                    chngid='U', 
                    fname='EDATU', 
                    tabkey=f'{values.mandt}{self.vbeln}{i}{i}', 
                    tabname='VBEP', 
                    valold=udate,
                    #valold='D', # HACK
                    valnew=newdate
                )

                for k, v in self.tables['VBEP_json'].items():
                    if (v['VBELN'] == self.vbeln) and (v['POSNR'] == i):
                        self.tables['VBEP_json'][k]["EDATU"] = newdate

    def approve_sales_order(self, udate, usnam, atime):
        changenr = f'{str(uuid.uuid4())[-11:]}'

        self.tables['JCDS_json'][str(uuid.uuid4())] = {
            "CDTCODE": changenr, # TODO add custom value
            "CHGNR": changenr,
            "INACT": None,
            "MANDT": values.mandt,
            "OBJNR": self.objnr,
            "STAT": 'I0002',
            "UDATE": udate,
            "USNAM": usnam,
            "UTIME": atime,
        }

    def generate_delivery_document(
            self, 
            ernam, 
            erdat,
            planned_delivery_date,
            picking_date,
            delivery_date,
            confirmation_date,
            atime,
            all_units=values.om_units,
        ):
        self.tables['LIKP_json'][str(uuid.uuid4())] = {
            "BTGEW": 99, # TODO add custom value
            "ERDAT": erdat,
            "ERNAM": ernam,
            "ERZET": atime,
            "GEWEI": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
            "KODAT": picking_date,  #PickingDate
            "KOUHR": atime,         #PickingDate
            "KUNNR": self.params['kunnr'],
            "LFART": 'D', # TODO add custom value
            "LFDAT": delivery_date,
            "MANDT": values.mandt,
            "NTGEW": len(self.params['matnrs'])*99, # TODO add custom weight and assign accordingly to VBAP
            "PODAT": confirmation_date,
            "POTIM": atime,
            "VBELN": self.likp_vbeln,
            "VBTYP": 'J',
            "VOLEH": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
            "VOLUM": 99, # TODO add custom value
            "WADAT": planned_delivery_date,
        }



        for i in range(len(self.params['matnrs'])):
            self.tables['LIPS_json'][str(uuid.uuid4())] = {
                "ERDAT": erdat,
                "ERNAM": ernam,
                "ERZET": str(helpers.add_random_hours(1, atime)),
                "GEWEI": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "LFIMG": self.params['quantities'][i],
                "LGORT": 'D',#TODO add custom value
                "MANDT": values.mandt,
                "MATNR": self.params['matnrs'][i],
                "NTGEW": 99, # TODO add custom value
                "POSNR": i,
                "VBELN": self.likp_vbeln,
                "VGBEL": self.vbeln,
                "VGPOS": i,
                "VGTYP": 'C',
                "VOLEH": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "VOLUM": 99, # TODO add custom value
                "VRKME": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "WERKS": self.params['plant']
            }
        self.record_flow( 
            erdat=erdat, 
            prev_vbeln=self.vbeln, 
            prev_type='C', 
            next_vbeln=self.likp_vbeln, 
            next_type='J'
        )

    def set_delivery_block(self, udate, usnam, all_delivery_blocs=values.om_delivery_blocks):
        # new_value=all_delivery_blocs[random.choice(list(all_delivery_blocs.keys()))]['LIFSP']
        new_value='01'
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas='VERKBELEG', # CHANGED FROM str(uuid.uuid4()), 
            udate=udate, 
            utime = helpers.generate_random_time(),
            uname=usnam, 
            chngid='U', 
            fname='LIFSK', 
            tabkey=f'{values.mandt}{self.vbeln}', 
            tabname='VBAK', 
            valold=None,
            valnew=new_value
        )

        for k, v in self.tables['VBAK_json'].items():
            if v['VBELN'] == self.vbeln:
                self.tables['VBAK_json'][k]['LIFSK'] = new_value 
                self.tables['VBAK_json'][k]['VSBED'] = None # delivery block root cause INCOMPLETE ORDER adjust shipping conditions

    def release_delivery_block(self, udate, usnam, all_delivery_blocs=values.om_delivery_blocks):
        # old_value=all_delivery_blocs[random.choice(list(all_delivery_blocs.keys()))]['LIFSP']
        old_value='01'
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas='VERKBELEG', # CHANGED FROM str(uuid.uuid4()), 
            udate=udate, 
            utime = helpers.generate_random_time(),
            uname=usnam, 
            chngid='U', 
            fname='LIFSK', 
            tabkey=f'{values.mandt}{self.vbeln}', 
            tabname='VBAK', 
            valold='Removed block',
            valnew=None
        )

        for k, v in self.tables['VBAK_json'].items():
            if v['VBELN'] == self.vbeln:
                self.tables['VBAK_json'][k]['LIFSK'] = None
                self.tables['VBAK_json'][k]['VSBED'] = None # delivery block root cause INCOMPLETE ORDER adjust shipping conditions

    def pick_items(self, usnam, udate, atime):
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas='LIEFERUNG', # CHANGED FROM str(uuid.uuid4()), 
            udate=udate, 
            utime =atime,
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
                self.tables['LIKP_json'][k]['KOUHR'] = atime

    def post_goods_issue(self, cpudt, usnam, atime, delivery_date_deviation, all_units=values.om_units):
        for i in range(len(self.params['matnrs'])): 
            self.tables['MSEG_json'][str(uuid.uuid4())] = {
                "BWART": '601',
                "CPUDT_MKPF": cpudt,
                "CPUTM_MKPF": atime,
                "ERFME": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "KDAUF": self.vbeln,
                "KDPOS": i,
                "LBKUM": round(self.params['prices'][i]*self.params['quantities'][i], 4),
                "LGORT": 'D', # TODO add custom value
                "LIFNR": None, # HACK only cosidering OM not Procurement
                "MANDT": values.mandt,
                "MATNR": self.params['matnrs'][i],
                "MBLNR": self.mblnr,
                "MEINS": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "MENGE": self.params['quantities'][i],
                "MJAHR": self.mjahr,
                "SHKZG": 'H', # Credit
                "SJAHR": self.mjahr,
                "SMBLN": self.mblnr,
                "SMBLP": i,
                "USNAM_MKPF": usnam,
                "VBELN_IM": self.likp_vbeln,
                "VBELP_IM": i,
                "WERKS": self.params['plant'],
                "ZEILE": i,
            }
            self.tables['EKBE_json'][str(uuid.uuid4())] = { # HACK every SO has 1:1 mapping form PO
                "BELNR": self.mblnr,
                "BUZEI": i,
                "GJAHR": self.mjahr,
                "MANDT": values.mandt,
                "MENGE": self.params['quantities'][i],
                "VGABE": 1, # Good Receipt
                "WAERS": 'EUR',
                "WRBTR": round(self.params['prices'][i]*self.params['quantities'][i], 4),
                "CPUDT": cpudt,
            }

            # Change the confirmed delivery date of the item to influence late, early
            #creation_date
            #late or early
            #self.params['delivery_date_deviation'][i]
            if delivery_date_deviation[i] != 0:
                date_dev = max(self.start_date + timedelta(days=1), cpudt+timedelta(days=delivery_date_deviation[i]))
                # print(f'---- Deviation from delivery date is {delivery_date_deviation[i]} days. Min Date is {self.start_date+ timedelta(days=1)} new date should be {cpudt+timedelta(days=delivery_date_deviation[i])} new scheduled date is {date_dev}')
            else:
                date_dev = cpudt
            #print(f'Deviation from delivery date is {delivery_date_deviation[i]} days. Min Date is {self.start_date+ timedelta(days=5)} new date should be {cpudt+timedelta(days=delivery_date_deviation[i])} new scheduled date is {date_dev}')
            for k, v in self.tables['VBEP_json'].items():
                if (v['VBELN'] == self.vbeln) and (v['POSNR'] == i):
                    self.tables['VBEP_json'][k]["EDATU"] = date_dev


        
        self.record_flow( 
            erdat=cpudt, 
            prev_vbeln=self.likp_vbeln, 
            prev_type='J', 
            next_vbeln=self.mblnr, 
            next_type='R'
        )

        self.create_shipment(aedat=cpudt, shipping_condition=values.shipping_conditions, ernam=usnam, all_routes=values.om_routes)

    def create_shipment(self, aedat, shipping_condition, ernam, all_routes=values.om_routes):
        shipping_number = f'{str(uuid.uuid4())[-17:]}'
        self.tables['VTTK_json'][str(uuid.uuid4())] = {
            'VSBED': shipping_condition,
            'TKNUM': shipping_number, # to edit SystemShipmentNumber
            'SHTYP': '0001', # to edit ShippingType / check
            'ROUTE': all_routes[random.choice(list(all_routes.keys()))]['ROUTE'],
            'MANDT': values.mandt,
            'ERZET': helpers.generate_random_time(),
            'ERNAM': ernam,
            'ERDAT': aedat,
        }
        for i in range(len(self.params['matnrs'])):
            self.tables['VTTP_json'][str(uuid.uuid4())] = {
                'VBELN': self.likp_vbeln,
                'TPNUM': i,
                'TKNUM': shipping_number,
                'MANDT': values.mandt,
                'ERZET': helpers.generate_random_time(),
                'ERNAM': ernam ,
                'ERDAT': aedat,
            }
  
    def create_invoice(self, ernam, erdat, atime):
        self.tables['VBRK_json'][str(uuid.uuid4())] = {
            "ERDAT": erdat,
            "ERNAM": ernam,
            "ERZET": atime,
            "KUNAG": self.params['kunnr'],
            "KUNRG": self.params['kunnr'], # for AR starter
            "MANDT": values.mandt,
            "SPART": '10', # for AR starter , division of goods / services join on knvv
            "VBELN": self.vbrk_vbeln,
            "VBTYP": 'M', # M: Invoice, 
            "VKORG": self.params['sales_org'], #for AR starter
            "VTWEG": self.params['distribution_channel'], # for AR starter
            "WAERK": 'EUR',
            "NETWR": round(sum([self.params['prices'][i]*self.params['quantities'][i] for i in range(len(self.params['matnrs']))]), 4), # new field to adjust if price or quantity change, 
            "ZTERM": self.params['payment_term'] # new field to edit, 
        }

        for i in range(len(self.params['matnrs'])):
            self.tables['VBRP_json'][str(uuid.uuid4())] = {
                "AUBEL": self.vbeln,
                "AUPOS": i,
                "ERDAT": erdat,
                "ERNAM": ernam,
                "ERZET": helpers.add_random_hours(1, atime),
                "MANDT": values.mandt,
                "MATNR": self.params['matnrs'][i],
                "POSNR": i,
                "VBELN": self.vbrk_vbeln,
                "WERKS": self.params['plant'],
                "VGTYP": 'J', 
                "FKIMG": 'd', # add proper value... 
                "NETWR": round(self.params['prices'][i]*self.params['quantities'][i], 4), # to adjust if quantity or price change activity...?
                "VRKME": 'd' # add proper value... 
            }
        
        self.tables['BKPF_json'][str(uuid.uuid4())] = {
            "AWKEY": self.vbrk_vbeln,
            "AWTYP": 'VBRK',
            "BELNR": self.bkpf_belnr,
            "BLART": 'D', # TODO add custom value
            "BLDAT": erdat, # FIXME use document creation date
            "BUKRS": self.params['company_code'],  # 'CC01', TODO make thie comapny code the same as used in KNB1
            "CPUDT": erdat,
            "CPUTM": atime,
            "GJAHR": self.mjahr,
            "MANDT": values.mandt,
            "USNAM": ernam,
            "WAERS": 'EUR',
            "XREVERSAL": None # NOTE might need change if P2P or AR is involved
        }

        for i in range(len(self.params['matnrs'])):
            self.tables['BSEG_json'][str(uuid.uuid4())] = {
                "AUGDT": None,
                "AUGBL": None,
                "AUGGJ": None, # HACK this is considered an initial value. If we use Nan, Pandas will consider the whole column to be float adn add '.0' at the end of the values.
                "BELNR": self.bkpf_belnr,
                "BSCHL": '01',
                "BUKRS": self.params['company_code'], # 'cc01' TODO make thie comapny code the same as used in KNB1
                "BUZEI": i,
                "GJAHR": self.mjahr,
                "KOART": 'D',
                "KUNNR": self.params['kunnr'],
                "MANDT": values.mandt,
                "MANSP": None,
                "MANST": None,
                "SGTXT": 'D', # TODO add custom value
                "SHKZG": 'S', # Debit Indicator
                "SKFBT": 0,
                "WRBTR": round(self.params['prices'][i]*self.params['quantities'][i], 4),
                "WSKTO": 0,
                "ZBD1P": 0, # TODO add custom value
                "ZBD1T": 0, # TODO add custom value
                "ZBD2P": 0, # TODO add custom value
                "ZBD2T": 0, # TODO add custom value
                "ZBD3T": 0, # TODO add custom value
                "ZFBDT": erdat, # TODO add custom value
                "ZTERM": self.params['payment_term']
            }


        self.record_flow( 
            erdat=erdat, 
            prev_vbeln=self.mblnr, 
            prev_type='J', 
            next_vbeln=self.vbrk_vbeln, 
            next_type='M'
        )

    def set_sales_order_billing_block(self, udate, usnam, blocked_matnrs):
        # SalesOrder Block
        new_value='01' # HACK match with values.om_billing_blocks
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas='VERKBELEG', # replaced unique ID str(uuid.uuid4()) with 'VERKBELEG', 
            udate=udate, 
            utime = helpers.generate_random_time(),
            uname=usnam, 
            chngid='U', 
            fname='FAKSK', 
            tabkey=f'{values.mandt}{self.vbeln}', 
            tabname='VBAK', 
            valold=None,
            valnew=new_value
        )

        for k, v in self.tables['VBAK_json'].items():
            if v['VBELN'] == self.vbeln:
                self.tables['VBAK_json'][k]['FAKSK'] = new_value

        # SalesOrderItem Block
        # for matnr in blocked_matnrs:
        #     for key, value in self.tables['VBAP_json'].items():
        #         if value.get('VBELN') == self.vbeln and value.get('MATNR') == matnr:
        #             posnr = value['POSNR']
        for pos in blocked_matnrs:
            # for key, value in self.tables['VBAP_json'].items():
            #     if value.get('VBELN') == self.vbeln and value.get('MATNR') == self.params['matnrs'][index]:
            #         posnr = value['POSNR']

            self.changes(
                objid=str(uuid.uuid4()), 
                objclas='VERKBELEG', # replaced unique ID str(uuid.uuid4()) with 'VERKBELEG',
                udate=udate, 
                utime = helpers.generate_random_time(),
                uname=usnam, 
                chngid='U', 
                fname='FAKSP', 
                tabkey=f'{values.mandt}{self.vbeln}{pos}', 
                tabname='VBAP', 
                valold=None,
                valnew=new_value
            )

            for k, v in self.tables['VBAP_json'].items():
                if (v['VBELN'] == self.vbeln) and (v['MATNR'] == self.params['matnrs'][pos]):
                    self.tables['VBAP_json'][k]['FAKSP'] = new_value
                    self.tables['VBAP_json'][k]['NETWR'] = 0.00  # for zero price root cause
            
    def release_sales_order_billing_block(self, udate, usnam, blocked_matnrs):
        old_value='01' # HACK match with values.om_billing_blocks
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas='VERKBELEG', # replaced unique ID str(uuid.uuid4()) with 'VERKBELEG', 
            udate=udate, 
            utime = helpers.generate_random_time(),
            uname=usnam, 
            chngid='U', 
            fname='FAKSK', 
            tabkey=f'{values.mandt}{self.vbeln}', 
            tabname='VBAK', 
            valold='Removed Block',
            valnew=None
        )

        for k, v in self.tables['VBAK_json'].items():
            if v['VBELN'] == self.vbeln:
                self.tables['VBAK_json'][k]['FAKSK'] = None

        # for matnr in blocked_matnrs:
        #     for k, v in self.tables['VBAP_json'].items():
        #         if (v['VBELN'] == self.vbeln) and (v['MATNR'] == matnr):
        #             posnr = self.tables['VBAP_json'][k]['POSNR']
        for pos in blocked_matnrs:
            # for key, value in self.tables['VBAP_json'].items():
            #     if value.get('VBELN') == self.vbeln and value.get('MATNR') == self.params['matnrs'][index]:
            #         posnr = value['POSNR']


            self.changes(
                objid=str(uuid.uuid4()), 
                objclas='VERKBELEG', # replaced unique ID str(uuid.uuid4()) with 'VERKBELEG', 
                udate=udate, 
                utime = helpers.generate_random_time(),
                uname=usnam, 
                chngid='U', 
                fname='FAKSP', 
                tabkey=f'{values.mandt}{self.vbeln}{pos}', 
                tabname='VBAP', 
                valold='Removed Block',
                valnew=None
            )

            for k, v in self.tables['VBAP_json'].items():
                if (v['VBELN'] == self.vbeln) and (v['MATNR'] == self.params['matnrs'][pos]):
                    self.tables['VBAP_json'][k]['FAKSP'] = None
                    self.tables['VBAP_json'][k]['NETWR'] = 0.00  # for zero price root cause

    def set_customer_billing_block(self, udate, usnam):
        new_value='02' # HACK match with values.om_billing_blocks
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas=str(uuid.uuid4()), 
            udate=udate, 
            utime = helpers.generate_random_time(),
            uname=usnam, 
            chngid='U', 
            fname='FAKSD', 
            tabkey=f'{values.mandt}{self.params["kunnr"]}', 
            tabname='KNA1', 
            valold=None,
            valnew=new_value
        )

    def release_customer_billing_block(self, udate, usnam):
        old_value='02' # HACK match with values.om_billing_blocks
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas=str(uuid.uuid4()), 
            udate=udate, 
            utime = helpers.generate_random_time(),
            uname=usnam, 
            chngid='U', 
            fname='FAKSD', 
            tabkey=f'{values.mandt}{self.params["kunnr"]}', 
            tabname='KNA1',     
            valold='Removed Block',
            valnew=None
        )

    def set_customer_delivery_block(self, udate, usnam):
        new_value='02' # HACK match with values.om_delivery_blocks
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas=str(uuid.uuid4()), 
            udate=udate, 
            utime = helpers.generate_random_time(),
            uname=usnam, 
            chngid='U', 
            fname='LIFSD', 
            tabkey=f'{values.mandt}{self.params["kunnr"]}', 
            tabname='KNA1', 
            valold=None,
            valnew=new_value
        )

    def release_customer_delivery_block(self, udate, usnam):
        old_value='02' # HACK match with values.om_delivery_blocks
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas=str(uuid.uuid4()), 
            udate=udate, 
            utime = helpers.generate_random_time(),
            uname=usnam, 
            chngid='U', 
            fname='LIFSD', 
            tabkey=f'{values.mandt}{self.params["kunnr"]}', 
            tabname='KNA1',     
            valold='Removed Block',
            valnew=None
        )


    def delivery_confirmation(self, usnam, udate):
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas=str(uuid.uuid4()), 
            udate=udate, 
            utime = helpers.generate_random_time(),
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
        
    def clear_debit_invoice(self, cpudt, usnam, cleared_date, atime):
        cleared_bkpf_belnr = f'{str(uuid.uuid4())[-11:]}'
        self.tables['BKPF_json'][str(uuid.uuid4())] = {
            "AWKEY": self.vbrk_vbeln,
            "AWTYP": 'VBRK',
            "BELNR": cleared_bkpf_belnr,
            "BLART": 'D', # TODO add custom value
            "BLDAT": cpudt, # FIXME use document creation date
            "BUKRS": self.params['company_code'], #'CC01', # TODO make thie comapny code the same as used in KNB1
            "CPUDT": cpudt,
            "CPUTM": atime,
            "GJAHR": self.mjahr,
            "MANDT": values.mandt,
            "USNAM": usnam,
            "WAERS": 'EUR',
            "XREVERSAL": None # NOTE might need change if P2P or AR is involved
        }

        for i in range(len(self.params['matnrs'])):
            self.tables['BSEG_json'][str(uuid.uuid4())] = {
                "AUGDT": cleared_date,
                "BELNR": cleared_bkpf_belnr,
                "AUGBL": cleared_bkpf_belnr, # TODO add custom value
                "AUGGJ": self.mjahr,
                "BSCHL": '01',
                "BUKRS": self.params['company_code'], #'CC01', # TODO make thie comapny code the same as used in KNB1
                "BUZEI": i,
                "GJAHR": self.mjahr,
                "KOART": 'D',
                "KUNNR": self.params['kunnr'],
                "MANDT": values.mandt,
                "MANSP": None,
                "MANST": None,
                "SGTXT": 'D', # TODO add custom value
                "SHKZG": 'S', # Debit Indicator
                "SKFBT": 0,
                "WRBTR": round(self.params['prices'][i]*self.params['quantities'][i], 4),
                "WSKTO": 0,
                "ZBD1P": 0, # TODO add custom value
                "ZBD1T": 0, # TODO add custom value
                "ZBD2P": 0, # TODO add custom value
                "ZBD2T": 0, # TODO add custom value
                "ZBD3T": 0, # TODO add custom value
                "ZFBDT": cpudt, # TODO add custom value
                "ZTERM": self.params['payment_term']
            }

    def change_payment_term(self, udate, usnam):
        old_value = self.params['payment_term']
        new_value = 'Z060'
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas='VERKBELEG', # replaced unique ID str(uuid.uuid4()) with 'VERKBELEG'
            udate=udate, 
            utime = helpers.generate_random_time(),
            uname=usnam, 
            chngid='U', 
            fname='ZTERM', 
            tabkey=f'{values.mandt}{self.vbeln}000000', #'000000000000000000000000', # HACK only need SUBSTR(14, 6) to be '000000'
            tabname='VBKD', 
            valold=old_value,
            valnew=new_value # TODO add custom value
        )

        for k, v in self.tables['VBKD_json'].items():
            if v['VBELN'] == self.vbeln:
                self.tables['VBKD_json'][k]['ZTERM'] = new_value
    
    def change_quantity(self, udate, usnam, line_numbers, line_quantities):
        for i, item_position in enumerate(line_numbers):
            old_value = self.params['quantities'][item_position]
            new_value = line_quantities[i]
            self.params['quantities'][i] = new_value
            self.changes(
                objid=str(uuid.uuid4()), 
                objclas='VERKBELEG', # replaced unique ID str(uuid.uuid4()) with 'VERKBELEG'
                udate=udate, 
                utime = helpers.generate_random_time(),
                uname=usnam, 
                chngid='U', 
                fname='KWMENG', 
                tabkey=f'{values.mandt}{self.vbeln}{item_position}',
                tabname='VBAP', 
                valold=old_value,
                valnew=new_value 
            )

            for k, v in self.tables['VBAP_json'].items():
                if (v['VBELN'] == self.vbeln) and (v['POSNR'] == item_position):
                    self.tables['VBAP_json'][k]['KWMENG'] = new_value
                    self.tables['VBAP_json'][k]['NETWR']: round(self.params['prices'][item_position]*self.params['quantities'][item_position], 4)

        for k, v in self.tables['VBAK_json'].items():
                if v['VBELN'] == self.vbeln:
                    self.tables['VBAK_json'][k]['NETWR'] = round(sum([self.params['prices'][i]*self.params['quantities'][i] for i in range(len(self.params['matnrs']))]), 4)

    def change_price(self, udate, usnam, line_numbers, line_prices):
        for i, item_position in enumerate(line_numbers):
            old_value = self.params['prices'][item_position]
            new_value = line_prices[i]
            self.params['prices'][i] = new_value
            self.changes(
                objid=str(uuid.uuid4()), 
                objclas='VERKBELEG', # replaced unique ID str(uuid.uuid4()) with 'VERKBELEG'
                udate=udate, 
                utime = helpers.generate_random_time(),
                uname=usnam, 
                chngid='U', 
                fname='NETPR', 
                tabkey=f'{values.mandt}{self.vbeln}{item_position}',
                tabname='VBAP', 
                valold=old_value,
                valnew=new_value 
            )

            for k, v in self.tables['VBAP_json'].items():
                if (v['VBELN'] == self.vbeln) and (v['POSNR'] == item_position):
                    self.tables['VBAP_json'][k]['NETPR'] = new_value
                    self.tables['VBAP_json'][k]['NETWR']: round(self.params['prices'][item_position]*self.params['quantities'][item_position], 4)

        for k, v in self.tables['VBAK_json'].items():
                if v['VBELN'] == self.vbeln:
                    self.tables['VBAK_json'][k]['NETWR'] = round(sum([self.params['prices'][i]*self.params['quantities'][i] for i in range(len(self.params['matnrs']))]), 4)

    # def change_delivery_date(self, udate, usnam):
    #     self.changes(
    #         objid=str(uuid.uuid4()), 
    #         objclas=str(uuid.uuid4()), 
    #         udate=erdat, 
    #         utime = helpers.generate_random_time(),
    #         uname=ernam, 
    #         chngid='U', 
    #         fname='LFDAT', 
    #         tabkey=f'{values.mandt}{self.likp_vbeln}', 
    #         tabname='LIKP', 
    #         valold='B',
    #         valnew='B'
    #     )


    def send_purchase_order(self, usnam, erdat):
        self.tables['NAST_json'][str(uuid.uuid4())] = {
            "AENDE": None,
            "DATVR": erdat,
            "ERDAT": erdat,
            "ERUHR": helpers.generate_random_time(),
            "KAPPL": 'EF',
            "KSCHL": 'NEU',
            "MANDT": values.mandt,
            "OBJKY": self.purchase_order_number,
            "PARNR": 'D', # TODO add custom value
            "PARVW": 'LF', # TODO add custom value
            "SPRAS": 'E',
            "TCODE": 'D', # TODO add custom value
            "UHRVR": helpers.generate_random_time(),
            "USNAM": usnam,
        }

    def create_purchase_order(self, aedat, ernam, utime):
            header_time = helpers.generate_random_time()
            self.tables['EKKO_json'][str(uuid.uuid4())] = {
                "AEDAT": aedat,
                "BSART": 'F',
                "BSTYP": 'F',
                "BUKRS": self.params['company_code'],
                "EBELN": self.purchase_order_number,
                "EKORG": self.params['purchasing_org'],
                "ERNAM": ernam,
                "FRGGR": 'D', # TODO add custom value
                "FRGKE": '2',
                "FRGSX": 'D', # TODO add custom value
                "FRGZU": None, # No Approval needed
                "KDATB": datetime.fromtimestamp(0).date(), # HACK 01/01/1970
                "KDATE": datetime.fromtimestamp(0).date(), # HACK 01/01/1970
                "KONNR": self.params['konnr'], # TODO to adjust if needed
                "LIFNR": self.params['lifnr'],
                "LOEKZ": 'D', # DeletionIndicator
                "MANDT": values.mandt,
                "RESWK": None, # HACK
                "STATU": 'B',
                "WAERS": 'EUR',
                "ZBD1P": 0, #self.params['cashdiscount'],#random.uniform(0.1, 0.3), #if random.random() > 0.5 else None, # test
                "ZBD1T": 0, #self.params['paymentdays'], # test
                "ZBD2P": 0, #random.uniform(0.1, 0.4), #if random.random() > 0.5 else None, # test
                "ZBD2T": 0, # test
                "ZBD3T": 0, # test
                "ZTERM": self.params['payment_term'],
            }
            self.changes(
                    objid=str(uuid.uuid4()), 
                    objclas='EINKBELEG', 
                    udate=aedat, 
                    utime=utime,
                    uname=ernam, 
                    chngid='I', 
                    fname='KEY', 
                    tabkey=f'{values.mandt}{self.purchase_order_number}', 
                    tabname='EKKO', 
                    valold=None,
                    valnew=None,
                )
            for i in range(len(self.params['proc_matnrs'])):
                randnom = random.random()
                #priceifnocontract = self.params['prices'][i] * (random.uniform(1.1, 1.5))
                self.tables['EKPO_json'][str(uuid.uuid4())] = {
                    "AEDAT": aedat,
                    "AFNAM": self.params['requested_by'],
                    "BANFN": None, # if self.params['has_pr'] == True else None,
                    "BNFPO": None, # if self.params['has_pr'] == True else None,
                    "BPRME": 1,
                    "BSTYP": 'F',
                    "BUKRS": self.params['company_code'],
                    "DPDAT": datetime.fromtimestamp(0).date(), # HACK 01/01/1970
                    "EBELN": self.purchase_order_number,
                    "EBELP": i,
                    "KONNR": self.params['konnr'], # if self.params['item_has_contract'][i] and self.params['has_contract'] else None,
                    "KTMNG": self.params['proc_quantities'][i],
                    "KTPNR": i, #if self.params['item_has_contract'][i] else None, # HACK -1 not None so as to make pd not consider this a float and add .0 to all
                    "LOEKZ": 'D', # DeletionIndicator
                    "MANDT": values.mandt,
                    "MATNR": self.params['proc_matnrs'][i], # if self.params['is_free_text'] and randnom > 0.3 else self.params['matnrs'][i],
                    "MEINS": self.unit,
                    "MENGE": self.params['proc_quantities'][i],
                    "NETPR": self.params['proc_prices'][i], # if self.params['item_has_contract'][i] else self.params['priceifnocontract'][i],
                    "NETWR": round(self.params['proc_prices'][i]*self.params['proc_quantities'][i], 2), # if self.params['item_has_contract'][i] else round(self.params['priceifnocontract'][i] * self.params['quantities'][i], 2) ,
                    "PEINH": 1,
                    "REPOS": None, # InvoiceReceiptIndicator
                    "TXZ01": self.params['proc_matnrs'][i], # self.params['free_text_materials'][i] if self.params['is_free_text'] and randnom > 0.3 else self.params['matnrs'][i],
                    "UEBTO": 0,
                    "WEBRE": None, # InvoiceAfterGoodsReceiptIndicator
                    "WEPOS": None, # Goods receipt indicator
                    "WERKS": self.params['plant'],
                    "ZWERT": round(self.params['proc_prices'][i]*self.params['proc_quantities'][i], 2),
                }
                self.changes(
                    objid=str(uuid.uuid4()), 
                    objclas='EINKBELEG', 
                    udate=aedat, 
                    utime=helpers.add_time(utime, helpers.UPTO_3_HOURS()),
                    uname=ernam, 
                    chngid='I', 
                    fname='KEY', 
                    tabkey=f'{values.mandt}{self.purchase_order_number}{i}', 
                    tabname='EKPO', 
                    valold=None,
                    valnew=None,
                )