-- Create avtivities table
DROP TABLE IF EXISTS "_CEL_O2C_ACTIVITIES";
CREATE TABLE "_CEL_O2C_ACTIVITIES" (
  _CASE_KEY VARCHAR(255),
  ACTIVITY VARCHAR(255),
  _SORTING INT,
  USERNAME VARCHAR(255),
  USERTYPE VARCHAR(32),
  EVENT_TIME TIMESTAMP,
  VBELN VARCHAR(255),
  POSNR INT
);

-- Create Order
INSERT INTO "_CEL_O2C_ACTIVITIES" (
   _CASE_KEY,
    ACTIVITY,
    _SORTING,
    USERNAME,
    USERTYPE,
    EVENT_TIME,
    VBELN,
    POSNR
)
SELECT
  "vbap"."MANDT" || "vbap"."VBELN" || "vbap"."POSNR" AS _CASE_KEY,
  'Create Order' AS ACTIVITY,
  100 AS _SORTING,
  "vbak"."ERNAM" AS USERNAME,
  "usr01"."UTYPE" AS USERTYPE,
  "vbak"."ERDAT" AS EVENT_TIME,
  "vbap"."VBELN" AS VBELN,
  "vbap"."POSNR" AS POSNR
FROM "vbap"
LEFT JOIN "vbak" ON "vbak"."VBELN" = "vbap"."VBELN"
LEFT JOIN "usr01" ON "vbak"."ERNAM" = "usr01"."BNAME";


-- Generate Delivery Document
INSERT INTO "_CEL_O2C_ACTIVITIES" (
   _CASE_KEY,
    ACTIVITY,
    _SORTING,
    USERNAME,
    USERTYPE,
    EVENT_TIME,
    VBELN,
    POSNR
)
SELECT 
  "lips"."MANDT" || "lips"."KDAUF" || "lips"."POSNR" AS _CASE_KEY,
  'Generate Delivery Document' AS ACTIVITY,
  200 AS _SORTING,
  "likp"."ERNAM" AS USERNAME,
  "usr01"."UTYPE" AS USERTYPE,
  "likp"."ERDAT" AS EVENT_TIME,
  "lips"."VBELN" AS VBELN,
  "lips"."POSNR" AS POSNR
FROM "lips"
   JOIN "likp" ON "likp"."VBELN" = "lips"."VBELN"
   JOIN "usr01" ON "usr01"."BNAME" = "likp"."ERNAM";

-- Release Delivery, Receive Delivery Confirmation, Clear Invoice, Set delivery block, Remove billing block, Cancel order, Return goods
INSERT INTO "_CEL_O2C_ACTIVITIES" (
   _CASE_KEY,
    ACTIVITY,
    _SORTING,
    USERNAME,
    USERTYPE,
    EVENT_TIME,
    VBELN,
    POSNR
)
SELECT 
  "vbap"."MANDT" || "vbap"."VBELN" || "vbap"."POSNR" AS _CASE_KEY,
  CASE
    WHEN 
      "cdhdr"."OBJECTCLAS" = 'DELIVERY' AND "cdpos"."TABNAME" = 'VBUK' AND "cdpos"."FNAME" = 'LFSTK' AND "cdpos"."OLDVALUE" ISNULL AND "cdpos"."NEWVALUE" = 'DELIVERYRELEASED'
    THEN 'Release Delivery' 
    WHEN 
      "cdhdr"."OBJECTCLAS" = 'DELIVERY' AND "cdpos"."TABNAME" = 'VBUK' AND "cdpos"."FNAME" = 'LFSTK' AND "cdpos"."OLDVALUE" = 'DELIVERYRELEASED' AND "cdpos"."NEWVALUE" = 'DELIVERYCONFIRMED'
    THEN 'Receive Delivery Confirmation' 
    WHEN 
      "cdhdr"."OBJECTCLAS" = 'BILLING' AND "cdpos"."TABNAME" = 'VBUK' AND "cdpos"."FNAME" = 'FKSTK' AND "cdpos"."OLDVALUE" ISNULL AND "cdpos"."NEWVALUE" = 'INVOICECLEARED'
    THEN 'Clear Invoice' 
    WHEN 
      "cdhdr"."OBJECTCLAS" = 'BILLING' AND "cdpos"."TABNAME" = 'VBAK' AND "cdpos"."FNAME" = 'FAKSK' AND "cdpos"."OLDVALUE" ISNULL AND "cdpos"."NEWVALUE" = 'BILLINGBLOCK'
    THEN 'Set Billing Block' 
    WHEN 
      "cdhdr"."OBJECTCLAS" = 'BILLING' AND "cdpos"."TABNAME" = 'VBAK' AND "cdpos"."FNAME" = 'FAKSK' AND "cdpos"."OLDVALUE" = 'BILLINGBLOCK' AND "cdpos"."NEWVALUE" ISNULL
    THEN 'Remove Billing Block'
    WHEN 
      "cdhdr"."OBJECTCLAS" = 'SALESORDER' AND "cdpos"."TABNAME" = 'VBUK' AND "cdpos"."FNAME" = 'VBTYP' AND "cdpos"."NEWVALUE" ='h'
    THEN 'Cancel Order' 
    WHEN 
      "cdhdr"."OBJECTCLAS" = 'SALESORDER' AND "cdpos"."TABNAME" = 'VBUK' AND "cdpos"."FNAME" = 'VBTYP' AND "cdpos"."NEWVALUE" ='H'
    THEN 'Return Goods'  
    -- ELSE 'HI NY!'
  END AS ACTIVITY,
  CASE
    WHEN "cdpos"."FNAME" = 'LFSTK' AND "cdpos"."NEWVALUE" = 'DELIVERYRELEASED' THEN 300
    WHEN "cdpos"."FNAME" = 'LFSTK' AND "cdpos"."NEWVALUE" = 'DELIVERYCONFIRMED' THEN 600
    WHEN "cdpos"."FNAME" = 'FKSTK' AND "cdpos"."NEWVALUE" = 'INVOICECLEARED' THEN 700
    WHEN "cdpos"."TABNAME" = 'VBAK' AND "cdpos"."FNAME" = 'FAKSK' AND "cdpos"."NEWVALUE" = 'BILLINGBLOCK' THEN 310
    WHEN "cdpos"."TABNAME" = 'VBAK' AND "cdpos"."FNAME" = 'FAKSK' AND "cdpos"."NEWVALUE" ISNULL THEN 410
    WHEN "cdpos"."TABNAME" = 'VBUK' AND "cdpos"."FNAME" = 'VBTYP' AND "cdpos"."NEWVALUE" = 'h' THEN 120
    WHEN "cdpos"."TABNAME" = 'VBUK' AND "cdpos"."FNAME" = 'VBTYP' AND "cdpos"."NEWVALUE" = 'H' THEN 610
  END AS _SORTING,
  "cdhdr"."USERNAME" AS USERNAME,
  "usr01"."UTYPE" AS USERTYPE,
  "cdhdr"."ERDAT" AS EVENT_TIME,
  "cdhdr"."OBJECTID" AS VBELN,
  "vbap"."POSNR" AS POSNR
FROM "cdpos"
  LEFT JOIN "cdhdr" ON "cdhdr"."CHANGENR" = "cdpos"."CHANGENR"
  LEFT JOIN "usr01" ON "usr01"."BNAME" = "cdhdr"."USERNAME"
  LEFT JOIN "vbap" ON "vbap"."VBELN" = "cdhdr"."OBJECTID";

-- Ship Goods
INSERT INTO "_CEL_O2C_ACTIVITIES" (
   _CASE_KEY,
    ACTIVITY,
    _SORTING,
    USERNAME,
    USERTYPE,
    EVENT_TIME,
    VBELN,
    POSNR
)
SELECT 
  "mseg"."MANDT" || "mseg"."KDAUF" || "mseg"."KDPOS" AS _CASE_KEY,
  'Ship Goods' AS ACTIVITY,
  400 AS _SORTING,
  "mkpf"."USNAM" AS USERNAME,
  "usr01"."UTYPE" AS USERTYPE,
  "mkpf"."AEDAT" AS EVENT_TIME,
  "mseg"."KDAUF" AS VBELN,
  "mseg"."KDPOS" AS POSNR
FROM "mkpf"
  LEFT JOIN "mseg" ON "mkpf"."MBLNR" = "mseg"."MBLNR"
  LEFT JOIN "usr01" ON "usr01"."BNAME" = "mkpf"."USNAM";

-- Send Invoice
INSERT INTO "_CEL_O2C_ACTIVITIES" (
   _CASE_KEY,
    ACTIVITY,
    _SORTING,
    USERNAME,
    USERTYPE,
    EVENT_TIME,
    VBELN,
    POSNR
)
SELECT 
  "vbrp"."MANDT" || "vbrp"."AUBEL" || "vbrp"."POSNR" AS _CASE_KEY,
  'Send Invoice' AS ACTIVITY,
  500 AS _SORTING,
  "vbrk"."ERNAM" AS USERNAME,
  "usr01"."UTYPE" AS USERTYPE,
  "vbrk"."ERDAT" AS EVENT_TIME,
  "vbrp"."VBELN" AS VBELN,
  "vbrp"."POSNR" AS POSNR
FROM "vbrp"
  LEFT JOIN "vbrk" ON "vbrk"."VBELN" = "vbrp"."VBELN"
  LEFT JOIN "usr01" ON "usr01"."BNAME" = "vbrk"."ERNAM";

-- SELECT COUNT(*) FROM _CEL_O2C_ACTIVITIES WHERE ACTIVITY ISNULL
