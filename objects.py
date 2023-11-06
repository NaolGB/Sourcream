import uuid
import values, helpers
import random
import pandas as pd

class Materials:
    def __init__(self, id: uuid.UUID, name: str, availability: float) -> None:
        self.id = id
        self.name = name
        self.availability = availability

class SalesOrderItem:
    def __init__(self, vbeln, posnr, kwmeng, matnr, netwr, material) -> None:
        self.mandt = values.mandt
        self.vbeln = vbeln
        self.posnr = posnr
        self.kwmeng = kwmeng
        self.matnr = matnr
        self.netwr = netwr
        self.material = material

class Users:
    def __init__(self, name, user_type) -> None:
        self.name = name
        self.user_type = user_type
