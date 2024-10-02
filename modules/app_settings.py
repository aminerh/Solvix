from datetime import datetime

class Settings():
    # APP SETTINGS
    # ///////////////////////////////////////////////////////////////
    ENABLE_CUSTOM_TITLE_BAR = True
    MENU_WIDTH = 240
    LEFT_BOX_WIDTH = 240
    RIGHT_BOX_WIDTH = 240
    TIME_ANIMATION = 500

    # BTNS LEFT AND RIGHT BOX COLORS
    BTN_LEFT_BOX_COLOR = "background-color: rgb(44, 49, 58);"
    BTN_RIGHT_BOX_COLOR = "background-color: #ff79c6;"

    # MENU SELECTED STYLESHEET
    MENU_SELECTED_STYLESHEET = """
    border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
    background-color: rgb(40, 44, 52);
    """
    print('2')

    DBNAME="Solvix"
    DBUSER="Usolvix"
    DBPWD="1234"
    DBHOST="10.49.0.179"  # or the IP address of your server
    DBPORT="5432"    

    REFUSER=""
    REFPWD=""


    current_date = datetime.now().strftime('%Y-%m-%d')

    #  ' loc AS "Emplacement avec quantité",
    #  ' qty AS "Quantité sans prélèvement" ,
    #   npcmnp AS "Reason Code",
    PICK_ANOMALIES = """
    SELECT 
    oerodp AS "Commande",
    OECCPL AS "Type de commande",
    CPT AS "Date CPT",
    CPTTIM AS "Heure CPT",
    DIGITS(pvjvpr) CONCAT '/' CONCAT DIGITS(pvmvpr) CONCAT '/' CONCAT DIGITS(pvsvpr) CONCAT DIGITS(pvavpr) AS "Date du manquant",
    SUBSTR(DIGITS(pvhvpr), 1, 2) CONCAT ':' CONCAT SUBSTR(DIGITS(pvhvpr), 3, 2) AS "Heure du manquant",
    pvcart AS "Asin",
    arlart AS "Description",
    pvqapb AS "Quantité manquante",
    pvc1em CONCAT ' ' CONCAT pvc2em CONCAT ' ' CONCAT pvc3em CONCAT ' ' CONCAT pvc4em CONCAT ' ' CONCAT pvc5em AS "Adresse",
    pvnsup AS "Support",


    case   when loc >= 1 then 'oui' else 'non' end as "a relancé" 
    FROM 
    INFSQL.NDDATEP 
    INNER JOIN AMAZONBD.HLPRELP ON pvtvpr = '1' 
        AND pvtnpr = '1' 
        AND pvcdpo = '001' 
        AND pvcact = '001' 
        AND pvsvpr = dasie 
        AND pvavpr = daann 
        AND pvmvpr = damois 
        AND pvjvpr = dajour 
    INNER JOIN AMAZONBD.HLNONPP ON npcact = pvcact 
        AND npcdpo = pvcdpo 
        AND npnann = pvnann 
        AND npnprl = pvnprl
    INNER JOIN AMAZONBD.HLARTIP ON pvcact = arcact 
        AND pvcart = arcart
    LEFT OUTER JOIN AMAZONBD.HLUTILP ON pvcuvp = utcuti
    INNER JOIN 
        (SELECT pecdpo, pecact, penann, penpre, oerodp, peccpl, pecrgc, OECCPL, ORSTAT, ORWAVD, ORWAVT, ORLAUC, ORLAUE, 
        DIGITS(pejdpr) CONCAT '/' CONCAT DIGITS(pemdpr) CONCAT '/' CONCAT DIGITS(pesdpr) CONCAT DIGITS(peadpr) AS CPT, 
        SUBSTR(DIGITS(pehdpr), 1, 2) CONCAT ':' CONCAT SUBSTR(DIGITS(pehdpr), 3, 2) AS CPTTIM 
        FROM AMAZONBD.HLPRENP
        LEFT OUTER JOIN AMAZONBD.HLPRPLP ON pecdpo = p1cdpo 
        AND pecact = p1cact 
        AND penann = p1nanp 
        AND penpre = p1npre
        LEFT OUTER JOIN AMAZONBD.HLODPEP ON pecdod = oecdpo 
        AND p1cact = oecact 
        AND p1nano = oenann 
        AND p1nodp = oenodp
        INNER JOIN AMRFXDD.AIORDEP ON oecdpo = ORCDPO 
        AND oecact = ORCACT 
        AND OERODP = ORRODP
        AND ORSLRR <> 'SUCCESS' 
        AND ORSTAT <>'Floor Denial' 
        AND ORSTAT <>'Cancelled'
        WHERE p1cdpo = '001' 
        AND pecact = '001'
        GROUP BY pecdpo, pecact, penann, penpre, oerodp, peccpl, pecrgc, ORSTAT, OECCPL, ORWAVD, ORWAVT, ORLAUC, ORLAUE, 
        DIGITS(pejdpr) CONCAT '/' CONCAT DIGITS(pemdpr) CONCAT '/' CONCAT DIGITS(pesdpr) CONCAT DIGITS(peadpr), 
        SUBSTR(DIGITS(pehdpr), 1, 2) CONCAT ':' CONCAT SUBSTR(DIGITS(pehdpr), 3, 2)) S
    ON pecdpo = pvcdpo 
        AND pecact = pvcact 
        AND penpre = pvnpre 
        AND penann = pvnanp
    LEFT OUTER JOIN 
        (SELECT gecdpo, gecact, gecart, COUNT(DISTINCT sunemp) AS loc, SUM(geqgei) AS qty
        FROM AMAZONBD.HLGEINP
        INNER JOIN AMAZONBD.HLSUPPP ON sucdpo = gecdpo 
        AND sunsup = gensup
        EXCEPTION JOIN AMAZONBD.HLPRELP ON pvcdpo = gecdpo 
        AND pvcact = gecact 
        AND pvngei = gengei 
        AND pvtvpr = '0'
        EXCEPTION JOIN AMAZONBD.HLLPRGP ON gecdpo = lgcdpo 
        AND gecact = lgcact 
        AND lgngei = gengei
        WHERE gecdpo = '001' 
        AND gecact = '001' 
        AND gecqal = 'STD' 
        AND getgdi = '1'
        GROUP BY gecdpo, gecact, gecart) GG
    ON gecdpo = pvcdpo 
        AND gecact = pvcact 
        AND gecart = pvcart
    WHERE  
    DADATE >= '"""+current_date+"""'
    AND NPCMNP <> 'OC'
    AND PVC1EM NOT LIKE 'BA%%' 
    AND PVC1EM NOT LIKE 'BB%%' 
    AND PVC1EM NOT LIKE 'BC%%' 
    AND PVC1EM NOT LIKE 'BD%%' 
    AND PVC1EM NOT LIKE 'BE%%' 
    AND PVC1EM NOT LIKE 'BF%%' 
    AND PVC1EM NOT LIKE 'BG%%' 
    AND PVC1EM NOT LIKE 'BH%%' 
    AND PVC1EM NOT LIKE 'BK05' 
    AND PVC1EM NOT LIKE 'BK04' 
    AND PVC1EM NOT LIKE 'VS%%' 
    AND PVC1EM NOT LIKE 'DA%%' 
    AND PVC1EM NOT LIKE 'DB%%' 
    AND PVC1EM NOT LIKE 'DC%%' 
    AND PVC1EM NOT LIKE 'FURN%%' 
    AND oerodp LIKE 'U%%'
    ORDER BY CPT,CPTTIM

    """ 
