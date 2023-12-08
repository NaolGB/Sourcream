def create_sales_order(
        vbak_args, vbkd_args, vbuk_args, tvkot_args, tvtwt_args, tvsbt_args, t001_args, 
        tvkbt_args, dd07t_vbtyp_args, tvakt_args):
    vbak_json.append({
        "MANDT": vbak_args["MANDT"],
        "VBELN": vbak_args["VBELN"],
        "ERDAT": vbak_args["ERDAT"],
        "ERZET": vbak_args["ERZET"],
        "ERNAM": vbak_args["ERNAM"],
        "OBJNR": vbak_args["OBJNR"],
        "AUART": vbak_args['AUART'],
        "BUKRS_VF": vbak_args["BUKRS_VF"] ,
        "MANDT": vbak_args["MANDT"] ,
        "KUNNR": vbak_args["KUNNR"] ,
        "VSBED": vbak_args["VSBED"],
        "VKBUR": vbak_args["VKBUR"],
        "MANDT": vbak_args["MANDT"],
        "KUNNR": vbak_args["KUNNR"],
        "KKBER": vbak_args["KKBER"],
        "NETWR": vbak_args["NETWR"],
        "WAERK": vbak_args["WAERK"],
        "VBTYP": vbak_args["VBTYP"],
        "VBELN": vbak_args["VBELN"],
        "VDATU": vbak_args["VDATU"],
        "MANDT": vbak_args["MANDT"],
        "BSTNK": vbak_args["BSTNK"],
        "BSTDK": vbak_args["BSTDK"],
        "VKORG": vbak_args["VKORG"],
        "VTWEG": vbak_args["VTWEG"],
    })
    vbdk_json.append({
        "INCO2": vbkd_args["INCO2"],
        "INCO1": vbkd_args["INCO1"],
        "INCO2": vbkd_args["INCO2"],
        "INCO1": vbkd_args["INCO1"],
        "ZTERM": vbkd_args["ZTERM"],
    })
    vbuk_json.append({
        "GBSTK": vbuk_args["GBSTK"],
        "BESTK": vbuk_args["BESTK"],
    })
    tvakt_json.append({
        "BEZEI": tvakt_args["BEZEI"],
    })
    
    tvkot_json.append({
        "VTEXT": tvkot_args["VTEXT"],
    })
    tvtwt_json.append({
        "VTEXT" : tvtwt_args["VTEXT"],
    })
    tvsbt_json.append({
        "VTEXT": tvsbt_args["VTEXT"],
    })
    t001_json.append({
        "BUTXT": t001_args["BUTXT"],
    })
    tvkbt_json.append({
        "BEZEI": tvkbt_args["BEZEI"],
    })
    dd07t_vbtyp_json.append({
        "DDTEXT": dd07t_vbtyp_args["DDTEXT"],
    })