
import pytesseract
import numpy as np
import cv2 # OpenCV
import re
import pandas as pd
import json
import sys

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"

def isolate_field(image, x1, x2, y1, y2, coords: tuple):

  std_x, std_y = coords

  res_x = len(image[0])
  res_y = len(image)

  fator_x = std_x//res_x
  fator_y = std_y//res_y

  tlist = []

  for a in image:

    tlist2 = []
    for i in a:
      tlist2.append(i)
    tlist2 = tlist2[x1//fator_x:x2//fator_x]
    
    tlist.append(tlist2)

  tlist = tlist[y1//fator_y:y2//fator_y]
  image = np.array(tlist)

  return image

docs_std_resolution = {
                        'AGV': {'NFS': (2480, 3509), 'recibo_locacao': (2550, 3300), 'mapa_faturamento': (2550, 3300)},
                        'GKO': {'NFS': (3175, 4150)},
                        'MOVE': {'NFS': (2480, 3509)},
                        'RIO': {'NFS': (2480, 3509)},
                        'RODOLOG': {'NFS': (2483,3512), 'fatura_duplicata': (2480, 3509)},
                        'RUNTEC': {'NFS': (2480, 3525)},
                        'SHIFT': {'NFS': (2480, 3509), 'nota_debito': (2481, 3509)},
                        'DIREMADI': {'NFS': (2479, 3509)}
                       }

dict_document = {
                'NFS': ['CNPJ', 'con', 'vencimento', 'nome', 'PO', 'valor', 'descricao'],
                'recibo_locacao': ['con', 'nome', 'PO', 'valor', 'contaContabil', 'centroCusto'],
                'nota_debito': ['con', 'vencimento', 'nome', 'PO', 'valor', 'descricao'],
                'mapa_faturamento': ['PO', 'con', 'valor', 'nome', 'CNPJ'],
                'fatura_duplicata': ['con', 'vencimento', 'nome', 'PO', 'valor', 'descricao']
                 }

#AGV
dict_map = {}
dict_map['AGV'] = {}
dict_map['AGV']['NFS'] = {'CNPJ': (440, 760, 580, 630), 'con': (1910, 2164, 270, 320), 'vencimento': (470, 700, 1240, 1274),
                          'nome': (575, 900, 640, 678), 'PO': (310, 540, 1280, 1325), 'valor': (1300, 1575, 2144, 2188), 'descricao': (245, 2175, 1200, 1235)}

dict_map['AGV']['mapa_faturamento'] = {'CNPJ': (1067, 1383, 1802, 1847),'con': (432, 658, 320, 360), 'nome': (11037, 1412, 1752, 1793),'PO':(440, 2330, 860, 1080) ,
                                      'valor': (1953,2329, 1460, 1505)}

dict_map['AGV']['recibo_locacao'] = {'CNPJ': (230, 450, 430, 460),'con': (1949, 2105, 830, 889), 'nome': ( 1037, 1453, 2133, 2177),'PO':(261, 515, 1257, 1300) ,
                                      'valor': (1601,2057, 1580, 1630)}

dict_map['AGV']['fatura_duplicata'] = {}
dict_map['AGV']['nota_debito'] = {}

#GKO
dict_map['GKO'] = {}
dict_map['GKO']['NFS'] = {'CNPJ': (350, 840, 590, 650), 'con': (2650, 3050, 90, 165), 'vencimento': (420, 780, 2370, 2440), 'nome': (550, 1250, 670, 750),
                          'PO': (10, 20, 10, 20), 'valor': (1780, 2120, 3020, 3100), 'descricao': (40, 2600, 1550, 1900)}

dict_map['GKO']['mapa_faturamento'] = {}
dict_map['GKO']['recibo_locacao'] = {}
dict_map['GKO']['fatura_duplicata'] = {}
dict_map['GKO']['nota_debito'] = {}

#SHIFT
dict_map['SHIFT'] = {}
dict_map['SHIFT']['NFS'] = {'CNPJ': ( 445, 753, 582, 619), 'con': (1919, 2159, 267, 310), 'vencimento': ( 495,715, 1580, 1614),
                          'nome': (579, 1165, 641, 679), 'PO': (641, 853, 1320, 1355), 'valor': (1310,1563, 2142, 2195), 'descricao': (249,693, 1200, 1238)}

dict_map['SHIFT']['mapa_faturamento'] = {}
dict_map['SHIFT']['recibo_locacao'] = {}
dict_map['SHIFT']['fatura_duplicata'] = {}
dict_map['SHIFT']['nota_debito'] = {'con': ( 557, 703, 853, 893), 'vencimento': (1763, 1973, 850, 899),
                          'nome': (167, 1485, 213, 285), 'PO': (617, 855, 1960, 2020), 'valor': (1947,2191, 2801, 2860), 'descricao': (167, 1147, 2012, 2104)}

#RUNTEC
dict_map['RUNTEC'] = {}
dict_map['RUNTEC']['NFS'] = {'CNPJ': (577, 853, 752, 790), 'con': (1860, 1980, 220, 265), 'vencimento': ( 143,313, 1665, 1703),
                          'nome': ( 737, 1163, 610, 645), 'PO': (551, 751, 1473, 1511), 'valor': (687,817, 2583, 2617), 'descricao': (49, 2043, 1399, 1439)}

dict_map['RUNTEC']['mapa_faturamento'] = {}
dict_map['RUNTEC']['recibo_locacao'] = {}
dict_map['RUNTEC']['fatura_duplicata'] = {}
dict_map['RUNTEC']['nota_debito'] = {}

#MOVE
dict_map['MOVE'] = {}
dict_map['MOVE']['NFS'] = {'CNPJ': (930, 1320, 380, 420), 'con': (340, 670, 227, 300), 'vencimento': (343, 465, 977, 1007),
                          'nome': (725, 2230, 330, 380), 'PO': (640, 800, 915, 940), 'valor': (1010, 1200, 1730, 1790), 'descricao': (250, 1330, 950, 975)}

dict_map['MOVE']['mapa_faturamento'] = {}
dict_map['MOVE']['recibo_locacao'] = {}
dict_map['MOVE']['fatura_duplicata'] = {}
dict_map['MOVE']['nota_debito'] = {}

#RIO
dict_map['RIO'] = {}
dict_map['RIO']['NFS'] = {'CNPJ': (730, 1090, 670, 720), 'con': (2050, 2250, 220, 260), 'vencimento': (10, 20, 10, 20),
                          'nome': (880, 1520, 730, 780), 'PO': (10, 20, 10, 20), 'valor': (2060, 2360, 2720, 2780), 'descricao': (97, 2370, 2510, 2620)}

dict_map['RIO']['mapa_faturamento'] = {}
dict_map['RIO']['recibo_locacao'] = {}
dict_map['RIO']['fatura_duplicata'] = {}
dict_map['RIO']['nota_debito'] = {}

#RODOLOG
dict_map['RODOLOG'] = {}
dict_map['RODOLOG']['NFS'] = {'CNPJ': (1429, 1687, 540, 571), 'con': (2107, 2261, 798, 834), 'vencimento': (1149, 1351, 735, 780),
                          'nome': (893, 1571, 361, 399), 'PO': (10, 20, 10, 20), 'valor': (2030, 2313, 2881, 2930), 'descricao': (187, 2247, 1484, 1518)}

dict_map['RODOLOG']['mapa_faturamento'] = {}
dict_map['RODOLOG']['recibo_locacao'] = {}
dict_map['RODOLOG']['fatura_duplicata'] = {'con': (225, 365, 2005, 2050) ,'vencimento': (2015, 2230, 682, 730), 'nome': (337, 1231, 375, 420), 
                                           'PO': (10, 20, 10, 20) , 'valor': (2185, 2357, 1540, 1580), 'descricao': (120, 945, 1770, 1820)}
dict_map['RODOLOG']['nota_debito'] = {}

#DIREMADI
dict_map['DIREMADI'] = {}
dict_map['DIREMADI']['NFS'] = {'CNPJ': (796, 1078, 670, 710), 'con': (1880, 2100, 385, 431), 'vencimento': (1149, 1351, 735, 780),
                          'nome': (910, 1539, 720, 760), 'PO': (485, 683, 1265, 1305), 'valor': (1324, 1620, 2082, 2120), 'descricao': (368, 2150, 1234, 1266)}

dict_map['DIREMADI']['mapa_faturamento'] = {}
dict_map['DIREMADI']['recibo_locacao'] = {}
dict_map['DIREMADI']['fatura_duplicata'] = {}
dict_map['DIREMADI']['nota_debito'] = {}

def getField(filename, company, field, document, params=None):

  image = cv2.imread(filename,0)
  x1, x2, y1, y2 = dict_map[company][document][field]

  #funcs = {'NFS': lambda : isolate_field(image, x1, x2, y1, y2, docs_std_resolution[company][document])}

  #info = funcs[document]()

  info = isolate_field(image, x1, x2, y1, y2, docs_std_resolution[company][document])
  
  if params == None:
    texto = pytesseract.image_to_string(info)
  else:
    texto = pytesseract.image_to_string(info, config=params)

  if field == 'PO' and document == 'mapa_faturamento':
    po = re.search(r'PO []0-9]+', texto)
    if po != None:
      texto = po.group()
  return texto

def extract_data(filename, company, document):
  info = {}

  for field in dict_document[document]:
    info[field] = getField(filename, company, field, document, params='--oem 3  --psm 6').strip()

  return info

"""#Biblioteca com as coordenadas dos dados.

##Planilha
"""

def compare(nota, planilha):
  df_xl = pd.read_excel(planilha)
  check = False
  for i in range(len(df_xl)):
    
    if nota['nome'] == str(df_xl.loc[i, 'TRANSPORTADORA']) or nota['valor'] == str(df_xl.loc[i, 'VALOR A PAGAR'] or nota['con'] == str(df_xl.loc[i, 'NOTA FISCAL'])):
      check = True
      break

  if(check == False):
    return False

  else:
    return nota


def run_ocr(filename, company, document, nome_planilha):
  dados = extract_data(filename, company, document)
  print(dados)
  if compare(dados, nome_planilha) == False:
    print('Nota Inválida')
    return None
  else:
    return json.dumps(dados)


img_file = sys.argv[1]
empresa = sys.argv[2]
tipo_documento = sys.argv[3]
planilha = sys.argv[4]

result = run_ocr(img_file, empresa, tipo_documento, planilha)
print(result)