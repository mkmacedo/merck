docs_std_resolution = {
                        'AGV': {'NFS': (2480, 3509), 'recibo_locacao': (2550, 3300), 'mapa_faturamento': (2550, 3300)},
                        'GKO': {'NFS': (3175, 4150)},
                        'MOVEIDEIAS': {'NFS': (2480, 3509)},
                        'RIO': {'NFS': (2480, 3509)},
                        'RODOLOG': {'NFS': (2483,3512), 'fatura_duplicata': (2480, 3509)},
                        'RUNTEC': {'NFS': (2480, 3525)},
                        'SHIFT': {'NFS': (2480, 3509), 'nota_debito': (2481, 3509)},
                        'DIREMADI': {'NFS': (2479, 3509)},
                        'DENISE': {'NFS': (2479, 3509)},
                        'LINE': {'NFS':(1240,1755), 'fatura_duplicata':(1240,1755)}
                       }

dict_document = {
                'NFS': ['CNPJ', 'con', 'vencimento', 'nome', 'PO', 'valor', 'descricao','desconto'],
                'recibo_locacao': ['con', 'nome', 'PO', 'valor', 'contaContabil', 'centroCusto','desconto'],
                'nota_debito': ['con', 'vencimento', 'nome', 'PO', 'valor', 'descricao','desconto'],
                'mapa_faturamento': ['PO', 'con', 'valor', 'nome', 'CNPJ','desconto'],
                'fatura_duplicata': ['con', 'vencimento', 'nome', 'PO', 'valor', 'descricao','desconto','valorAPagar']
                 }

#AGV
dict_map = {}
dict_map['AGV'] = {}
dict_map['AGV']['NFS'] = {'CNPJ': (440, 760, 580, 630), 'con': (1910, 2164, 270, 320), 'vencimento': (470, 700, 1240, 1274),
                          'nome': (550, 930, 640, 690), 'PO': (310, 540, 1280, 1325), 'valor': (1300, 1575, 2144, 2188), 'descricao': (245, 2175, 1200, 1235)}

dict_map['AGV']['mapa_faturamento'] = {'CNPJ': (1067, 1383, 1802, 1847),'con': (432, 658, 320, 360), 'nome': (11037, 1412, 1752, 1793),'PO':(440, 2330, 860, 1080) ,
                                      'valor': (1953,2329, 1460, 1505)}

dict_map['AGV']['recibo_locacao'] = {'CNPJ': (230, 450, 430, 460),'con': (1949, 2105, 830, 889), 'nome': ( 1037, 1453, 2133, 2177),'PO':(261, 515, 1257, 1300) ,
                                      'valor': (1601,2057, 1580, 1630)}

#dict_map['AGV']['fatura_duplicata'] = {}
#dict_map['AGV']['nota_debito'] = {}

#GKO
dict_map['GKO'] = {}
dict_map['GKO']['NFS'] = {'CNPJ': (350, 840, 590, 650), 'con': (2650, 3050, 90, 165), 'vencimento': (420, 780, 2370, 2440), 'nome': (550, 1250, 670, 750),
                          'PO': (40, 3130, 1480, 2880), 'valor': (1780, 2120, 3020, 3100), 'descricao': (40, 3130, 1480, 2880)}
#'descricao': (40, 2600, 1550, 1900)

#dict_map['GKO']['mapa_faturamento'] = {}
#dict_map['GKO']['recibo_locacao'] = {}
#dict_map['GKO']['fatura_duplicata'] = {}
#dict_map['GKO']['nota_debito'] = {}

#SHIFT
dict_map['SHIFT'] = {}
dict_map['SHIFT']['NFS'] = {'CNPJ': ( 445, 753, 582, 619), 'con': (1919, 2159, 267, 310), 'vencimento': ( 495,715, 1580, 1614),
                          'nome': (579, 1165, 641, 679), 'PO': (641, 853, 1320, 1355), 'valor': (1310,1563, 2142, 2195), 'descricao': (249,693, 1200, 1238)}

#dict_map['SHIFT']['mapa_faturamento'] = {}
#dict_map['SHIFT']['recibo_locacao'] = {}
#dict_map['SHIFT']['fatura_duplicata'] = {}
dict_map['SHIFT']['nota_debito'] = {'con': ( 557, 703, 853, 893), 'vencimento': (1763, 1973, 850, 899),
                          'nome': (167, 1485, 213, 285), 'PO': (617, 855, 1960, 2020), 'valor': (1947,2191, 2801, 2860), 'descricao': (167, 1147, 2012, 2104)}

#RUNTEC
dict_map['RUNTEC'] = {}
dict_map['RUNTEC']['NFS'] = {'CNPJ': (577, 853, 752, 790), 'con': (1860, 1980, 220, 265), 'vencimento': ( 143,313, 1665, 1703),
                          'nome': ( 737, 1163, 610, 645), 'PO': (551, 751, 1473, 1511), 'valor': (687,817, 2583, 2617), 'descricao': (49, 2043, 1399, 1439)}

#dict_map['RUNTEC']['mapa_faturamento'] = {}
#dict_map['RUNTEC']['recibo_locacao'] = {}
#dict_map['RUNTEC']['fatura_duplicata'] = {}
#dict_map['RUNTEC']['nota_debito'] = {}

#MOVEIDEIAS
dict_map['MOVEIDEIAS'] = {}
dict_map['MOVEIDEIAS']['NFS'] = {'CNPJ': (930, 1320, 380, 420), 'con': (340, 670, 227, 300), 'vencimento': (343, 465, 977, 1007),
                          'nome': (720, 2230, 330, 380), 'PO': (640, 800, 915, 940), 'valor': (1010, 1200, 1730, 1790), 'descricao': (250, 1330, 950, 975)}

#dict_map['MOVEIDEIAS']['mapa_faturamento'] = {}
#dict_map['MOVEIDEIAS']['recibo_locacao'] = {}
#dict_map['MOVEIDEIAS']['fatura_duplicata'] = {}
#dict_map['MOVEIDEIAS']['nota_debito'] = {}

#RIO
dict_map['RIO'] = {}
dict_map['RIO']['NFS'] = {'CNPJ': (730, 1090, 670, 720), 'con': (2050, 2250, 220, 260), 'vencimento': (10, 20, 10, 20),
                          'nome': (880, 1520, 730, 780), 'PO': (10, 20, 10, 20), 'valor': (2060, 2360, 2720, 2780), 'descricao': (97, 2370, 2510, 2620)}

#dict_map['RIO']['mapa_faturamento'] = {}
#dict_map['RIO']['recibo_locacao'] = {}
#dict_map['RIO']['fatura_duplicata'] = {}
#dict_map['RIO']['nota_debito'] = {}

#RODOLOG
dict_map['RODOLOG'] = {}
dict_map['RODOLOG']['NFS'] = {'CNPJ': (1429, 1687, 540, 571), 'con': (2107, 2261, 798, 834), 'vencimento': (1149, 1351, 735, 780),
                          'nome': (893, 1571, 361, 399), 'PO': (10, 20, 10, 20), 'valor': (2030, 2313, 2881, 2930), 'descricao': (187, 2247, 1484, 1518)}

#dict_map['RODOLOG']['mapa_faturamento'] = {}
#dict_map['RODOLOG']['recibo_locacao'] = {}
dict_map['RODOLOG']['fatura_duplicata'] = {'con': (225, 365, 2005, 2050) ,'vencimento': (2015, 2230, 682, 730), 'nome': (337, 1231, 375, 420), 
                                           'PO': (10, 20, 10, 20) , 'valor': (2185, 2357, 1540, 1580), 'descricao': (120, 945, 1770, 1820)}
#dict_map['RODOLOG']['nota_debito'] = {}

#DIREMADI
dict_map['DIREMADI'] = {}
dict_map['DIREMADI']['NFS'] = {'CNPJ': (796, 1078, 670, 710), 'con': (1880, 2100, 385, 431), 'vencimento': (1149, 1351, 735, 780),
                          'nome': (910, 1539, 720, 760), 'PO': (485, 683, 1265, 1305), 'valor': (1324, 1620, 2082, 2120), 'descricao': (368, 2150, 1234, 1266)}

#dict_map['DIREMADI']['mapa_faturamento'] = {}
#dict_map['DIREMADI']['recibo_locacao'] = {}
#dict_map['DIREMADI']['fatura_duplicata'] = {}
#dict_map['DIREMADI']['nota_debito'] = {}

#DENISE
dict_map['DENISE'] = {}
dict_map['DENISE']['NFS'] = {'CNPJ': (530, 850, 670, 720), 'con': (1880, 2100, 385, 431), 'vencimento': (10, 20, 10, 20),
                          'nome': (660, 1230, 1220, 1240), 'PO': (370, 2156, 1185, 2150), 'valor': (1324, 1620, 2082, 2126), 'descricao': (370, 2156, 1185, 2150)}

#dict_map['DENISE']['mapa_faturamento'] = {}
#dict_map['DENISE']['recibo_locacao'] = {}
#dict_map['DENISE']['fatura_duplicata'] = {}
#dict_map['DENISE']['nota_debito'] = {}

#LINE
dict_map['LINE'] = {}
dict_map['LINE']['NFS'] = {'CNPJ': (379, 535, 370, 393), 'con': (862, 927, 220, 240), 'vencimento': (10, 20, 10, 20),
                          'nome': (237, 683,290, 309), 'PO': (91, 1132, 686, 1101), 'valor': (991, 1100, 1285, 1310), 'descricao': (91, 1132, 686, 1101)}
dict_map['LINE']['fatura_duplicata'] = {'con': (254, 319, 251, 278) ,'vencimento': (930, 1041, 251, 277), 'nome': (295,790, 86, 112), 'PO': (207, 1170,318, 387) , 
                                        'valor': (395, 505, 252,277), 'descricao': (207, 1170,318, 387), 'desconto':(559,636,250,278),'valorAPagar':(673,777,250,278)}

#dict_map['LINE']['mapa_faturamento'] = {}
#dict_map['LINE']['recibo_locacao'] = {}
#dict_map['LINE']['nota_debito'] = {}


companies = ['AGV LOGISTICA SA', 
            'RODOLOG TRANSPORTES MULTIMODAIS LTDA', 
            'DIREMADI MARKETING E SERVICOS LTDA', 
            'SHIFT GESTAO DE SERVICOS LTDA', 
            'RUNTEC INFOMATICA LTDA', 
            'DENISE DOS ANJOS PINTO LUCENA',
            'GKO INFORMATICA LTDA',
            'MOVEIDEIAS CONSULTORIA E INTEGRACAO DE NEGOCIOS LTDA',
            'RIO LOPES TRANSPORTES LTDA',
            'LINE EXPRESS TRANSPORTES E DISTRIBUICAO LTDA'
            ]