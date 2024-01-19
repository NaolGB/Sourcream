import uuid
import random
from datetime import datetime, timedelta
import values, helpers

class SalesAndDistribution:
    def __init__(self, vbeln, params, start_date: datetime) -> None:
        self.vbeln = vbeln
        self.params = params
        self.objnr = f'{str(uuid.uuid4())[-17:]}' # HACK to avoid overflow when multiple ids being cancatenated
        self.likp_vbeln = f'{str(uuid.uuid4())[-17:]}' 
        self.vbrk_vbeln = f'{str(uuid.uuid4())[-17:]}'
        self.bkpf_belnr = f'{str(uuid.uuid4())[-17:]}'
        self.mblnr = f'{str(uuid.uuid4())[-17:]}'
        start_date = start_date
        self.mjahr = int(start_date.year)

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
            'JCDS_json': {},
            'VBFA_json': {}
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
            "LIFSK": 'None',
            'FAKSK': 'None'
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
            temp_vbeln = f'{str(uuid.uuid4())[-17:]}'
            self.tables['VBAP_json'][temp_vbeln] = {
                "ABGRU": 'D', # HACK
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
                'FAKSP': 'None'
            }
            self.tables['VBEP_json'][temp_vbeln] = {
                "BMENG": self.params['quantities'][i], # HACK all qauntities are the same as their confirmed queantities
                "EDATU": erdat,
                "ETENR": i,
                "MANDT": values.mandt,
                "MBDAT": 1970, # TODO MaterialAvailabilityDate edit later on shipping
                "MEINS": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "POSNR": i,
                "VBELN": self.vbeln,
                "WADAT": 1970, # TODO MaterialAvailabilityDate edit later on shipping,
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
            uname=usnam, 
            chngid='U', 
            fname='CMGST', 
            tabkey=f'{values.mandt}{self.vbeln}', 
            tabname='VBUK', 
            valold='B',
            valnew='A'
        )

        for k, v in self.tables['VBUK_json'].items():
            if v['VBELN'] == self.vbeln:
                self.tables['VBUK_json'][k]['CMGST'] = 'A'

    def reject_sales_order(self, udate, usnam, all_rejection_reasons=values.om_sales_doc_rejection_reasons):
        for i  in range(len(self.params['matnrs'])):
            # new_val = all_rejection_reasons[random.choice(list(all_rejection_reasons.keys()))]['ABGRU']
            new_val = 'Z0' if random.random() < 0.7 else 'Z1'
            self.changes(
                objid=str(uuid.uuid4()), 
                objclas=str(uuid.uuid4()), 
                udate=udate, 
                uname=usnam, 
                chngid='U', 
                fname='ABGRU', 
                tabkey=f'{values.mandt}{self.vbeln}{i}', 
                tabname='VBAP', 
                valold='D', # HACK
                valnew=new_val,
            )

            for k, v in self.tables['VBAP_json'].items():
                if (v['VBELN'] == self.vbeln) and (v['POSNR'] == i):
                    self.tables['VBAP_json'][k]['ABGRU'] = new_val

    def approve_sales_order(self, udate, usnam, atime):
        changenr = f'{str(uuid.uuid4())[-17:]}'

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
            "KODAT": picking_date,
            "KOUHR": atime,
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
        new_value=all_delivery_blocs[random.choice(list(all_delivery_blocs.keys()))]['LIFSP']
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas=str(uuid.uuid4()), 
            udate=udate, 
            uname=usnam, 
            chngid='U', 
            fname='LIFSK', 
            tabkey=f'{values.mandt}{self.vbeln}', 
            tabname='VBAK', 
            valold='None',
            valnew=new_value,
        )

        for k, v in self.tables['VBAK_json'].items():
            if v['VBELN'] == self.vbeln:
                self.tables['VBAK_json'][k]['LIFSK'] = new_value

    def release_delivery_block(self, udate, usnam, all_delivery_blocs=values.om_delivery_blocks):
        old_value=all_delivery_blocs[random.choice(list(all_delivery_blocs.keys()))]['LIFSP']
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas=str(uuid.uuid4()), 
            udate=udate, 
            uname=usnam, 
            chngid='U', 
            fname='LIFSK', 
            tabkey=f'{values.mandt}{self.vbeln}', 
            tabname='VBAK', 
            valold=old_value,
            valnew='None',
        )

        for k, v in self.tables['VBAK_json'].items():
            if v['VBELN'] == self.vbeln:
                self.tables['VBAK_json'][k]['LIFSK'] = 'None'

    def pick_items(self, usnam, udate, atime):
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
                self.tables['LIKP_json'][k]['KOUHR'] = atime

    def post_goods_issue(self, cpudt, usnam, atime, all_units=values.om_units):
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
            }
        
        self.record_flow( 
            erdat=cpudt, 
            prev_vbeln=self.likp_vbeln, 
            prev_type='J', 
            next_vbeln=self.mblnr, 
            next_type='R'
        )
  
    def create_invoice(self, ernam, erdat, atime):
        self.tables['VBRK_json'][str(uuid.uuid4())] = {
            "ERDAT": erdat,
            "ERNAM": ernam,
            "ERZET": atime,
            "KUNAG": self.params['kunnr'],
            "MANDT": values.mandt,
            "VBELN": self.vbrk_vbeln,
            "VBTYP": 'M', # M: Invoice
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
                'VGTYP': 'J'
            }
        
        self.tables['BKPF_json'][str(uuid.uuid4())] = {
            "AWKEY": self.vbrk_vbeln,
            "AWTYP": 'VBRK',
            "BELNR": self.bkpf_belnr,
            "BLART": 'D', # TODO add custom value
            "BLDAT": erdat, # FIXME use document creation date
            "BUKRS": 'CC01', # TODO make thie comapny code the same as used in KNB1
            "CPUDT": erdat,
            "CPUTM": atime,
            "GJAHR": self.mjahr,
            "MANDT": values.mandt,
            "USNAM": ernam,
            "WAERS": 'EUR',
            "XREVERSAL": None, # NOTE might need change if P2P or AR is involved
        }

        for i in range(len(self.params['matnrs'])):
            self.tables['BSEG_json'][str(uuid.uuid4())] = {
                "AUGDT": 1970,
                "AUGBL": None,
                "AUGGJ": 1970, # HACK this is considered an initial value. If we use Nan, Pandas will consider the whole column to be float adn add '.0' at the end of the values.
                "BELNR": self.bkpf_belnr,
                "BSCHL": '01',
                "BUKRS": 'CC01', # TODO make thie comapny code the same as used in KNB1
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
                "ZTERM": self.params['payment_term'],
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
            objclas=str(uuid.uuid4()), 
            udate=udate, 
            uname=usnam, 
            chngid='U', 
            fname='FAKSK', 
            tabkey=f'{values.mandt}{self.vbeln}', 
            tabname='VBAK', 
            valold='None',
            valnew=new_value,
        )

        for k, v in self.tables['VBAK_json'].items():
            if v['VBELN'] == self.vbeln:
                self.tables['VBAK_json'][k]['FAKSK'] = new_value

        # SalesOrderItem Block
        for matnr in blocked_matnrs:
            for key, value in self.tables['VBAP_json'].items():
                if value.get('VBELN') == self.vbeln and value.get('MATNR') == matnr:
                    posnr = value['POSNR']

            self.changes(
                objid=str(uuid.uuid4()), 
                objclas=str(uuid.uuid4()), 
                udate=udate, 
                uname=usnam, 
                chngid='U', 
                fname='FAKSP', 
                tabkey=f'{values.mandt}{self.vbeln}{posnr}', 
                tabname='VBAP', 
                valold='None',
                valnew=new_value,
            )

            for k, v in self.tables['VBAP_json'].items():
                if (v['VBELN'] == self.vbeln) and (v['MATNR'] == matnr):
                    self.tables['VBAP_json'][k]['FAKSP'] = new_value
            
    def release_sales_order_billing_block(self, udate, usnam, blocked_matnrs):
        old_value='01' # HACK match with values.om_billing_blocks
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas=str(uuid.uuid4()), 
            udate=udate, 
            uname=usnam, 
            chngid='U', 
            fname='FAKSK', 
            tabkey=f'{values.mandt}{self.vbeln}', 
            tabname='VBAK', 
            valold=old_value,
            valnew=None,
        )

        for k, v in self.tables['VBAK_json'].items():
            if v['VBELN'] == self.vbeln:
                self.tables['VBAK_json'][k]['FAKSK'] = 'None'

        for matnr in blocked_matnrs:
            for k, v in self.tables['VBAP_json'].items():
                if (v['VBELN'] == self.vbeln) and (v['MATNR'] == matnr):
                    posnr = self.tables['VBAP_json'][k]['POSNR']

            self.changes(
                objid=str(uuid.uuid4()), 
                objclas=str(uuid.uuid4()), 
                udate=udate, 
                uname=usnam, 
                chngid='U', 
                fname='FAKSP', 
                tabkey=f'{values.mandt}{self.vbeln}{posnr}', 
                tabname='VBAP', 
                valold=old_value,
                valnew='None',
            )

            for k, v in self.tables['VBAP_json'].items():
                if (v['VBELN'] == self.vbeln) and (v['MATNR'] == matnr):
                    self.tables['VBAP_json'][k]['FAKSP'] = 'None'

    def set_customer_billing_block(self, udate, usnam):
        new_value='02' # HACK match with values.om_billing_blocks
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas=str(uuid.uuid4()), 
            udate=udate, 
            uname=usnam, 
            chngid='U', 
            fname='FAKSD', 
            tabkey=f'{values.mandt}{self.params["kunnr"]}', 
            tabname='KNA1', 
            valold=None,
            valnew=new_value,
        )

    def release_customer_billing_block(self, udate, usnam):
        old_value='02' # HACK match with values.om_billing_blocks
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas=str(uuid.uuid4()), 
            udate=udate, 
            uname=usnam, 
            chngid='U', 
            fname='FAKSD', 
            tabkey=f'{values.mandt}{self.params["kunnr"]}', 
            tabname='KNA1', 
            valold=old_value,
            valnew=None,
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
        
    def clear_debit_invoice(self, cpudt, usnam, cleared_date, atime):
        cleared_bkpf_belnr = f'{str(uuid.uuid4())[-17:]}'
        self.tables['BKPF_json'][str(uuid.uuid4())] = {
            "AWKEY": self.vbrk_vbeln,
            "AWTYP": 'VBRK',
            "BELNR": cleared_bkpf_belnr,
            "BLART": 'D', # TODO add custom value
            "BLDAT": cpudt, # FIXME use document creation date
            "BUKRS": 'CC01', # TODO make thie comapny code the same as used in KNB1
            "CPUDT": cpudt,
            "CPUTM": atime,
            "GJAHR": self.mjahr,
            "MANDT": values.mandt,
            "USNAM": usnam,
            "WAERS": 'EUR',
            "XREVERSAL": None, # NOTE might need change if P2P or AR is involved
        }

        for i in range(len(self.params['matnrs'])):
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
                "ZTERM": self.params['payment_term'],
            }

    def change_payment_term(self, udate, usnam):
        old_value = self.params['payment_term']
        new_value = 'Z060'
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas=str(uuid.uuid4()), 
            udate=udate, 
            uname=usnam, 
            chngid='U', 
            fname='ZTERM', 
            tabkey='000000000000000000000000', # HACK only need SUBSTR(14, 6) to be '000000'
            tabname='VBKD', 
            valold=old_value,
            valnew=new_value, # TODO add custom value
        )

        for k, v in self.tables['VBKD_json'].items():
            if v['VBELN'] == self.vbeln:
                self.tables['VBKD_json'][k]['ZTERM'] = new_value
