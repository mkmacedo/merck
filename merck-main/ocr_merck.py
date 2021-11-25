
#from m210 import fill_form
from dictionaries import docs_std_resolution, dict_document, dict_map
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


#Get contractor's name
def nomeFornecedor(filename, full_name=False):
  img = cv2.imread(filename)
  config_tesseract = '--oem 3  --psm 11'
  texto = pytesseract.image_to_string(img, config=config_tesseract)
  vetorResul = re.findall(r'AGV LOGISTICA SA|RIO LOPES TRANSPORTES LTDA|GKO INFORMATICA LTDA|MOVEIDEIAS CONSULTORIA E INTEGRACAO DE NEGOCIOS LTDA - EPP|Rodolog Transportes Multimodais Ltda|RUNTECH INFORMATICA LTDA|SHIFT GESTAO DE SERVICOS LTDA|DENISE DOS ANJOS PINTO LUCENA|DIREMADI MARKETING E SERVICOS LTDA|LINE EXPRESS TRANSPORTES E DISTRIBUICAO LTDA', texto, flags=re.I)
  result = vetorResul[0].split(" ")
  if full_name == False:
    company = result[0]
  else:
    company = vetorResul[0]
  return company



def getField(filename, company, field, document, params=None):

  image = cv2.imread(filename,0)
  if(field == 'nome'):
    image = cv2.blur(image, (3,3))

  x1, x2, y1, y2 = dict_map[company][document][field]

  #funcs = {'NFS': lambda : isolate_field(image, x1, x2, y1, y2, docs_std_resolution[company][document])}

  #info = funcs[document]()

  info = isolate_field(image, x1, x2, y1, y2, docs_std_resolution[company][document])
  
  if params == None:
    texto = pytesseract.image_to_string(info)
  else:
    texto = pytesseract.image_to_string(info, config=params)

  if field == 'PO':
    if document == 'mapa_faturamento':
      po = re.search(r'PO:? [0-9]+', texto)
      if po != None:
        texto = po.group()
    elif document == 'NFS':
      po = re.search(r'(?:PO|Pedido):? [0-9]+', texto)
      if po != None:
        texto = po.group()
  return texto



def extract_data(filename, company, document):
  info = {}

  for field in dict_document[document]:
    info[field] = getField(filename, company, field, document, params='--oem 3  --psm 6').strip()
    if field == 'nome':
      s = re.search(r'(?:[A-Z]| )+', info[field])
      if s != None:
        info[field] = s.group().strip()

  return info



def compare(nota, planilha):
  df_xl = pd.read_excel(planilha)
  check = False

  #and nota['valor'] == str(df_xl.loc[i, 'VALOR FATURA'])
  temp = {}
  temp['AGV LOGISTICA SA'] = 'AGV LOGISTICA'
  temp['valor'] = ''
  valor = re.findall(r'[0-9]+|,[0-9][0-9]', nota['valor'])
  for e in valor:
    if e != ',00':
      temp['valor'] += e
  print(temp['valor'])
  temp['con'] = re.search(r'[1-9][0-9]*', nota['con']).group()

  print(temp['con'])
  for i in range(len(df_xl)):
    #and nota['valor'] == str(df_xl.loc[i, 'VALOR FATURA']

    """ if i > 8360:
        print(temp[nota['nome']],temp['valor'],temp['con'])
        print(str(df_xl.loc[i, 'TRANSPORTADORA']),str(df_xl.loc[i, 'VALOR FATURA']),str(df_xl.loc[i, 'NOTA FISCAL']))
        print() """

    if temp[nota['nome']] == str(df_xl.loc[i, 'TRANSPORTADORA']) and eval(temp['valor']) == df_xl.loc[i, 'VALOR FATURA'] and temp['con'] == str(df_xl.loc[i, 'NOTA FISCAL']):
      
      check = True
      break

  if(check == False):
    #verifica PO
    return False

  else:
    return nota



def run_ocr(filename, document, nome_planilha):
  company = nomeFornecedor(filename)
  dados = extract_data(filename, company, document)
  dados['Validacao'] = ''
  print(dados)
  if compare(dados, nome_planilha) == False:
    print('Nota Inválida')
    return dados
  else:
    #returns dictionary
    return dados


img_file = sys.argv[1]
#empresa = sys.argv[2]
tipo_documento = sys.argv[2]
planilha = sys.argv[3]

result = None
try:
  result = run_ocr(img_file, tipo_documento, planilha)
  print(result)
except:
  print('Não foi possível extrair dados')

""" try:
  out = result['nome']+result['con']+'.jpg'
  #fill_form(result, 'm210_blank.jpg', out)
except:
  print('Não foi possível gerar documento') """



def insert_data(filename, doctype, data: dict):
  data['tipo_documento'] = doctype
  with open('registros.txt', 'a') as f:
    #string = f'{filename}|'+'{"tipo_documento": '+f'"{doctype}", '+'"con": '+f'"{con}", '+'"valor": '+f'"{valor}"'+'}'
    string = json.dumps(data)
    f.write(f'{filename}|{string}')

insert_data(img_file, tipo_documento, result)
