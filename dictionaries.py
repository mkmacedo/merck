docs_std_resolution = {
                        'AGV': {'NFS': (2480, 3509), 'recibo_locacao': (2550, 3300), 'mapa_faturamento': (2550, 3300),'custo_frete':(1753,1240),'fatura_duplicata': (989,1280)},
                        'GKO': {'NFS': (3175, 4150)},
                        'MOVEIDEIAS': {'NFS': (2480, 3509)},
                        'RIO': {'NFS': (2480, 3509)},
                        'RODOLOG': {'NFS': (2483,3512), 'fatura_duplicata': (2480, 3509)},
                        'RUNTEC': {'NFS': (2480, 3525)},
                        'SHIFT': {'NFS': (2480, 3509), 'nota_debito': (2481, 3509)},
                        'DIREMADI': {'NFS': (2480, 3509), 'fatura_duplicata': (1654, 1182)},
                        'DENISE': {'NFS': (2479, 3509)},
                        'LINE': {'NFS':(1240,1755), 'fatura_duplicata':(1240,1755),'custo_frete':(1753,1240)},
                        'ANDREANI':{'fatura_duplicata':(1240,1755), 'custo_frete':(1753,1240)},
                        'FL':{'DACTE':(1240,1753), 'custo_frete':(1753,1240),'fatura_frete':(1241,1755)},
                        None:{'fatura_frete': (1241,1755)},
                        'MULTIRIO':{'NFS':(1240,1755)},
                        'ICTSI':{'NFS':(1240,1755)},
                        'DHL' :{'nota_debito':(1240,1755),'NFS':(1240,1755)}
                       }

dict_document = {
                'NFS': ['CNPJ', 'con', 'vencimento', 'nome', 'PO', 'valor', 'descricao','pesobruto'], #'desconto'],
                'recibo_locacao': ['con', 'nome', 'PO', 'valor'],# 'contaContabil', 'centroCusto','desconto'],
                'nota_debito': ['con', 'vencimento', 'nome', 'PO', 'valor','descricao','pesobruto'], #'descricao','desconto'],
                'mapa_faturamento': ['PO', 'con', 'valor', 'nome', 'CNPJ'],#'desconto'],
                'fatura_duplicata': ['con', 'vencimento', 'nome', 'PO', 'valor', 'descricao'],#'desconto','valorAPagar']
                'custo_frete':['nome', 'con','CNPJ','valor'], 
                'DACTE':['con','CNPJ','nome','valor','vencimento'],
                'fatura_frete':['CNPJ','vencimento','valor'],
                'detalhamento_notafiscal':['valorImposto','valorSem','CIF','taxa','descricao','nome','moeda','periodo','tipoServico'],
                'minuta_calculo':['valorCIF','valor']
                 }

docTypeMap = {'mapa de faturamento': 'mapa_faturamento',
                'mapa faturamento': 'mapa_faturamento',
                'recibo locação': 'recibo_locacao',
                'recibo locacao': 'recibo_locacao',
                'recibo de locação': 'recibo_locacao',
                'recibo de locacao': 'recibo_locacao',
                'nota fiscal de serviço': 'NFS',
                'nota fiscal de servico': 'NFS',
                'nfs-e': 'NFS',
                'nfs': 'NFS',
                'fatura duplicata': 'fatura_duplicata',
                'fatura/duplicata': 'fatura_duplicata',
                'nota fiscal': 'NFS',
                'custo de frete': 'custo_frete',
                'custo frete': 'custo_frete',
                'nota de debito': 'nota_debito',
                'nota de débito': 'nota_debito',
                'nota débito': 'nota_debito',
                'nota debito': 'nota_debito',
                'dacte': 'DACTE',
                'conferencia de faturas': 'fatura_frete',
                'detalhamento dos itens da nota fiscal': 'detalhamento_notafiscal'
                }

docHierarchy = {
                'minuta_calculo': 10,
                'detalhamento_notafiscal':9,
                'fatura_frete': 8,
                'nota_debito': 7,
                'fatura_duplicata': 6,
                'recibo_locacao': 5,
                'mapa_faturamento': 4,
                'custo_frete': 3,
                'DACTE': 2,
                'NFS': 1
                }
#AGV
dict_map = {}
dict_map['AGV'] = {}
dict_map['AGV']['NFS'] = {'CNPJ': (440, 760, 580, 630), 'con': (1910, 2164, 270, 320), 'vencimento': (470, 700, 1240, 1274),
                          'nome': (550, 930, 640, 690), 'PO': (310, 540, 1280, 1325), 'valor': (1300, 1575, 2144, 2188), 'descricao': (245, 2175, 1200, 1235)}

dict_map['AGV']['mapa_faturamento'] = {'CNPJ': (1050, 1400, 1790, 1845),'con': (432, 658, 320, 360), 'nome': (1037, 1412, 1752, 1793),'PO':(440, 2330, 860, 1080) ,
                                      'valor': (1933,2327, 1453, 1505)}

dict_map['AGV']['recibo_locacao'] = {'CNPJ': (230, 450, 430, 460),'con': (1949, 2105, 830, 889), 'nome': ( 1037, 1453, 2133, 2177),'PO':(255, 537, 1225, 1300) ,
                                      'valor': (1601,2057, 1580, 1630)}

dict_map['AGV']['custo_frete'] = {'con':(333, 383, 255, 278) ,'CNPJ':(292, 475, 406, 431) ,'nome':(483, 785, 404, 431),'valor':(1465, 1595, 670, 695)}

dict_map['AGV']['fatura_duplicata'] = {'con': (150, 230, 760, 780) ,'vencimento': (683, 787, 758, 780), 'nome': (560, 720, 500, 518), 
                                    'valor': (760, 920, 410, 430), 'CNPJ': (550, 716, 570, 595)}

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
dict_map['DIREMADI']['NFS'] = {'CNPJ': (720, 1025, 579, 620), 'con': (1915, 2165, 265, 310), 'vencimento': (10, 20, 10, 20),
                          'nome': (853, 1549, 635, 681), 'PO': (374, 599, 1237, 1273), 'valor': (1311, 1570, 2140, 2188), 'descricao': (245, 2000, 1196, 1500)}

dict_map['DIREMADI']['fatura_duplicata'] = {'con': (370, 510, 400, 450) ,'vencimento': (1000, 1170, 400, 450), 'nome': (70, 700, 250, 290), 
                                           'PO': (370, 500, 400, 450) , 'valor': (600, 750, 400, 450), 'descricao': (300, 1577, 610, 760)}

#dict_map['DIREMADI']['mapa_faturamento'] = {}
#dict_map['DIREMADI']['recibo_locacao'] = {}
#dict_map['DIREMADI']['fatura_duplicata'] = {}
#dict_map['DIREMADI']['nota_debito'] = {}

#DENISE
dict_map['DENISE'] = {}
dict_map['DENISE']['NFS'] = {'CNPJ': (432, 800, 560, 640), 'con': (1903, 2200, 261, 311), 'vencimento': (10, 20, 10, 20),
                          'nome': (575, 1183, 635, 678), 'PO': (317, 583, 1311, 1359), 'valor': (1327, 1565, 2140, 2185), 'descricao': (245, 2229, 1194, 2079)}

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
dict_map['LINE']['custo_frete'] = {'con':(333, 383, 255, 278) ,'CNPJ':(292, 475, 406, 431) ,'nome':(483, 785, 404, 431),'valor':(1465, 1595, 670, 695)}
#dict_map['LINE']['mapa_faturamento'] = {}
#dict_map['LINE']['recibo_locacao'] = {}
#dict_map['LINE']['nota_debito'] = {}

#ANDREANI
dict_map['ANDREANI'] = {}
#dict_map['ANDREANI']['NFS'] = {}
dict_map['ANDREANI']['fatura_duplicata'] = {'con': (175, 260, 170, 190) ,'vencimento': (57, 139, 175, 195), 'nome': (56, 282, 103, 125), 
                                        'valor': (485, 645, 175, 199), 'CNPJ': (373, 488, 365, 381)}
dict_map['ANDREANI']['custo_frete'] = {'con':(333, 383, 255, 278) ,'CNPJ':(292, 475, 406, 431) ,'nome':(483, 785, 404, 431),'valor':(1465, 1595, 670, 695)}

#dict_map['ANDREANI']['mapa_faturamento'] = {}
#dict_map['ANDREANI']['recibo_locacao'] = {}
#dict_map['ANDREANI']['nota_debito'] = {}

#FLBRASIL
dict_map['FL'] = {}
dict_map['FL']['fatura_duplicata'] = {'con': (553, 640, 148, 167) ,'vencimento': (653, 757, 148, 168), 'nome': (192, 395, 80, 189), 
                                        'valor': (1038, 1212, 846,872), 'CNPJ': (67, 190, 235, 255)}

dict_map['FL']['custo_frete'] = {'con':(330,402, 254,276) ,'CNPJ':(333,476, 405,430) ,'nome':(483,725, 407,430),'valor':(1470,1624, 592,615)}
dict_map['FL']['DACTE'] = {'con': (553, 640, 148, 167) ,'vencimento': (653, 757, 148, 168), 'nome': (192, 395, 80, 189), 
                                        'valor': (1038, 1212, 846,872), 'CNPJ': (67, 190, 235, 255)}

dict_map['FL']['fatura_frete'] = {'CNPJ':(322,440,102,113), 'vencimento':(819,905,128,142),'valor':(1057,1133,268,282)}
dict_map[None] = {}
dict_map[None]['fatura_frete'] = {'CNPJ':(322,440,102,113), 'vencimento':(819,905,128,142),'valor':(1057,1133,268,282)}
#dict_map['FL']['mapa_faturamento'] = {}
#dict_map['FL']['recibo_locacao'] = {}
#dict_map['FL']['nota_debito'] = {}

#MULTI RIO
dict_map['MULTIRIO'] = {}
dict_map['MULTIRIO']['NFS'] = {'CNPJ': (213,365,295,313), 'con': (939,1050,157,135), 'vencimento': (898,1005,205,182),
                          'nome': (278,618,320,339), 'PO': (115,1089,601,1066), 'valor': (639,810,1098,1076), 'descricao': (115,1089,601,1066)}

#dict_map['MULTIRIO']['fatura_duplicata'] = {}
#dict_map['MULTIRIO']['custo_frete'] = {}
#dict_map['MULTIRIO']['mapa_faturamento'] = {}
#dict_map['MULTIRIO']['recibo_locacao'] = {}
#dict_map['MULTIRIO']['nota_debito'] = {}

#ICTSI
dict_map['ICTSI'] = {}
dict_map['ICTSI']['NFS'] = {'CNPJ': (359,510,313,293), 'con': (957,1082,158,135), 'vencimento': (918,1030,202,181),
                          'nome': (425,700,338,320), 'PO': (122,1111,1231,1063), 'valor': (650,785,1092,1071), 'descricao': (122,1111,1063,600)}
#dict_map['ICTSI']['fatura_duplicata'] = {}
#dict_map['ICTSI']['custo_frete'] = {}
#dict_map['ICTSI']['mapa_faturamento'] = {}
#dict_map['ICTSI']['recibo_locacao'] = {}
#dict_map['ICTSI']['nota_debito'] = {}
dict_map['ICTSI']['detalhamento_notafiscal'] = {'CIF':(480,628,655,636),'taxa':(990,650,655,635),'descricao':(62,1195,1395,100),'tipoServico':(60,1170,1725,1525),
                                                'nome':(150,265,99,45),'moeda':(995,1105,689,670),'periodo':(62,145,919,898),'valorImposto':(975,1090,916,900),'valorSem':(490,635,916,900)}

#DHL
dict_map['DHL'] = {}
dict_map['DHL']['NFS'] = {'CNPJ': (361,571,267,249), 'con': (970,1042,54,73), 'vencimento': (960,1058,168,152),
                          'nome': (445,795,298,266),'valor': (355,465,1345,1330), 'descricao': (23,1209,1219,593)}

#dict_map['DHL']['fatura_duplicata'] = {}
#dict_map['DHL']['custo_frete'] = {}
#dict_map['DHL']['mapa_faturamento'] = {}
#dict_map['DHL']['recibo_locacao'] = {}
dict_map['DHL']['nota_debito'] = {'con': (1089,1155,40,21), 'vencimento': (865,945,190,171),
                          'nome': (267,600,45,77), 'valor': (969,1200,1445,1423),'descricao':(22,1201,1153,533)}

companies = ['AGV LOGISTICA SA', 
            'RODOLOG TRANSPORTES MULTIMODAIS LTDA', 
            'DIREMADI MARKETING E SERVICOS LTDA', 
            'SHIFT GESTAO DE SERVICOS LTDA', 
            'RUNTEC INFOMATICA LTDA', 
            'DENISE DOS ANJOS PINTO LUCENA',
            'GKO INFORMATICA LTDA',
            'MOVEIDEIAS CONSULTORIA E INTEGRACAO DE NEGOCIOS LTDA',
            'RIO LOPES TRANSPORTES LTDA',
            'LINE EXPRESS TRANSPORTES E DISTRIBUICAO LTDA',
            'ANDREANI LOGISTICA LTDA',
            'FL BRASIL HOLDING LOGISTICA E TRANSPORTE LTDA',
            'MULTI RIO OPERACOES PORTUARIAS S/A',
            'ICTSI RIO BRASIL TERMINAL 1 SA',
            'DHL GLOBAL FORWARDING (BRAZIL) LOGISTICS LTDA'
            ]