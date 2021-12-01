
#from m210 import fill_form
from api_client import API_Client
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

  fator_x = std_x/res_x + 0.5
  fator_y = std_y/res_y + 0.5

  fator_x = int(fator_x)
  fator_y = int(fator_y)

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
  print(texto)
  
  vetorResul = re.findall(r'AGV LOGISTICA SA|RIO LOPES TRANSPORTES LTDA|GKO INFORMATICA LTDA|MOVEIDEIAS CONSULTORIA E INTEGRACAO DE NEGOCIOS LTDA - EPP|Rodolog Transportes Multimodais Ltda|RUNTEC INFORMATICA LTDA|SHIFT GESTAO DE SERVICOS LTDA|DENISE DOS ANJOS PINTO LUCENA|DIREMADI MARKETING E SERVICOS LTDA|LINE EXPRESS TRANSPORTES E DISTRIBUICAO LTDA|LINE EXPRESS|ANDREANI LOGISTICA|FL BRASIL HOLDING LOGISTICA E TRANSPORTE', texto, flags=re.I)
  print(vetorResul)
  result = vetorResul[0].split(" ")

  if full_name == False:
    company = result[0]
  else:
    company = vetorResul[0]
  return company.upper()



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
      po = re.search(r'(?:PO|Pedido):? [0-9]+', texto)
      if po != None:
        po = re.search(r'[0-9]+', po.group())
        texto = po.group()
    elif document == 'NFS':
      po = re.search(r'(?:PO|Pedido):? [0-9]+', texto)
      if po != None:
        po = re.search(r'[0-9]+', po.group())
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

    #PO - NUMERIC    
    if field == 'PO':
      s = re.search(r'[0-9]+', info[field])
      if s == None:
        info[field] = ''

  return info



def compare(nota, planilha):
  df_xl = pd.read_excel(planilha)
  check = False

  #and nota['valor'] == str(df_xl.loc[i, 'VALOR FATURA'])
  temp = {}
  temp['AGV LOGISTICA SA'] = 'AGV LOGISTICA'
  temp['DIREMADI MARKETING E SERVICOS LTDA'] = 'DIREMADI'
  temp['ANDREANI LOGISTICA'] = 'ANDREANI LOGISTICA'
  temp['RIO LOPES TRANSPORTES LTDA'] = 'RIO LOPES TRANSPORTES LTDA'
  temp['GKO INFORMATICA LTDA'] = 'GKO INFORMATICA LTDA'
  temp['MOVEIDEIAS CONSULTORIA E INTEGRACAO DE NEGOCIOS LTDA - EPP'] = 'MOVEIDEIAS CONSULTORIA E INTEGRACAO DE NEGOCIOS LTDA - EPP'
  temp['Rodolog Transportes Multimodais Ltda'] = 'Rodolog Transportes Multimodais Ltda'
  temp['RUNTECH INFORMATICA LTDA'] = 'RUNTECH INFORMATICA LTDA'
  temp['SHIFT GESTAO DE SERVICOS LTDA'] = 'SHIFT GESTAO DE SERVICOS LTDA'
  temp['LINE EXPRESS TRANSPORTES E DISTRIBUICAO LTDA'] = 'LINE EXPRESS TRANSPORTES E DISTRIBUICAO LTDA'
  temp['DENISE DOS ANJOS PINTO LUCENA'] = 'DENISE DOS ANJOS PINTO LUCENA'
  
  temp['valor'] = ''
  valor = re.findall(r'[0-9]+|,[0-9][0-9]', nota['valor'])
  for e in valor:
    if e != ',00':
      temp['valor'] += e
  print(temp['valor'])
  temp['con'] = re.search(r'[1-9][0-9]*', nota['con'])
  if temp['con'] != None:
    temp['con'] = temp['con'].group()

  print(temp['con'])
  for i in range(len(df_xl)):
    #and nota['valor'] == str(df_xl.loc[i, 'VALOR FATURA']

    """ if i > 8360:
        print(temp[nota['nome']],temp['valor'],temp['con'])
        print(str(df_xl.loc[i, 'TRANSPORTADORA']),str(df_xl.loc[i, 'VALOR FATURA']),str(df_xl.loc[i, 'NOTA FISCAL']))
        print() """

    if str(temp.get(nota.get('nome'))) == str(df_xl.loc[i, 'TRANSPORTADORA']) and str(eval(temp['valor'])) == str(df_xl.loc[i, 'VALOR FATURA']) and str(temp['con']) == str(df_xl.loc[i, 'NOTA FISCAL']):
      
      check = True
      break

  if(check == False and nota.get("PO") != None):
    #verifica PO
    if re.search(r'[0-9]+', nota.get("PO")) == None:
      nota['Validacao'] = 'Nota Invalida'
    else:
      nota['Validacao'] = 'Nota Valida'
  else:
    nota['Validacao'] = 'Nota Valida'
  
  return nota



def run_ocr(filename, document, nome_planilha):
  company = nomeFornecedor(filename, True)
  #api_json = API_Client('https://wise.klink.ai/api/admin/find/fornecedor/tenant/merck').result
  centroCusto = None
  contaContabil = None
  """ for c in api_json:
    if c['razaoSocial'].upper() == company.upper():
      centroCusto = c['centroCusto']
      contaContabil = c['contaContabil']
      break"""

  dados = extract_data(filename, company.split()[0], document)
  if(centroCusto != None):
    dados['centro_custo'] = centroCusto

  if(contaContabil != None):
    dados['conta_contabil'] = contaContabil

  if dados.get('desconto') != None:
    dados['valorBruto'] = dados['valor'] - dados['desconto']
  else:
    dados['valorBruto'] = dados['valor']

  #print(dados)
  return compare(dados, nome_planilha)


img_file = sys.argv[1]
#empresa = sys.argv[2]
tipo_documento = sys.argv[2]
planilha = sys.argv[3]

#result = None

result = run_ocr(img_file, tipo_documento, planilha)
print(result)
#except:
#  print('Não foi possível extrair dados')

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
    f.write(f'{filename}|{string}\n')

insert_data(img_file, tipo_documento, result)
