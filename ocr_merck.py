
#from m210 import fill_form
#import traceback
from pdf_splitter  import splitPDF
from convertPDF2JPG import convertPDF2Image
from api_client import API_Client
from dictionaries import docs_std_resolution, dict_document, dict_map, docTypeMap, docHierarchy, companies
import pytesseract
import numpy as np
import cv2 # OpenCV
import re
import pandas as pd
import json
import sys

#pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def getDocumentType(filename):
  img = cv2.imread(filename)
  config_tesseract = '--oem 3  --psm 11'
  texto = pytesseract.image_to_string(img, config=config_tesseract)
  #print(texto)
  texto = texto.lower()
  
  vetorResultado = re.findall(r'fatura.?duplicata|mapa [de]? faturamento|recibo de locação|recibo de locacao|nota fiscal de serviço|nota fiscal|\
  nfs-e|nfs|fatura duplicata|nota fiscal eletronica de servicos e fatura|custo de frete|custo de frete|nota de debito|nota de débito|dacte|conferencia de faturas', texto, flags=re.I)
  #print(vetorResultado)

  standardized_docs_list = []

  for v in vetorResultado:
    standardized_docs_list.append(docTypeMap[v])

  #print(standardized_docs_list)

  docPriority = 0
  doc = ''

  for d in standardized_docs_list:
    if docHierarchy[d] > docPriority:
      docPriority = docHierarchy[d]
      doc = d
  
  return doc


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
  #print(texto)
  
  vetorResul = re.findall(r'AGV LOGISTICA SA|RIO LOPES TRANSPORTES LTDA|GKO INFORMATICA LTDA|MOVEIDEIAS CONSULTORIA E INTEGRACAO DE NEGOCIOS LTDA - EPP|Rodolog Transportes Multimodais Ltda|RUNTEC|SHIFT GESTAO DE SERVICOS LTDA|DENISE DOS ANJOS PINTO LUCENA|DIREMADI [MARKETING E SERVICOS LTDA]?|LINE EXPRESS TRANSPORTES E DISTRIBUICAO LTDA|LINE EXPRESS|ANDREANI LOGISTICA|FL BRASIL HOLDING|FL ?BRASIL|MULTI RIO OPERACOES PORTUARIAS|ICTSI RIO BRASIL TERMINAL 1 SA', texto, flags=re.I)
  #print(vetorResul)
  if len(vetorResul) > 0:
    result = vetorResul[0].split(" ")

    if full_name == False:
      company = result[0]

    else:
      company = vetorResul[0]

    if company == 'FLBRASIL':
      company = 'FL'
      return company.upper()

    return company.upper()

  else:
    return None



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
      s = re.match(r'[0-9]+', info[field])
      if s == None:
        info[field] = ''

  return info



def compare(nota):

  check = False

  #and nota['valor'] == str(df_xl.loc[i, 'VALOR FATURA'])
  temp = {}
  temp['AGV LOGISTICA SA'] = 'AGVLOGISTICA'
  temp['DIREMADI MARKETING E SERVICOS LTDA'] = 'DIREMADI'
  temp['DIREMADI'] = 'DIREMADI'
  temp['ANDREANI LOGISTICA'] = 'ANDREANI'
  temp['RIO LOPES TRANSPORTES LTDA'] = 'RIOLOPES'
  temp['GKO INFORMATICA LTDA'] = 'GKO INFORMATICA LTDA'
  temp['MOVEIDEIAS CONSULTORIA E INTEGRACAO DE NEGOCIOS LTDA'] = 'MOVEIDEIAS'
  temp['Rodolog Transportes Multimodais Ltda'] = 'Rodolog'
  temp['RUNTECH INFORMATICA LTDA'] = 'RUNTECH INFORMATICA LTDA'
  temp['SHIFT GESTAO DE SERVICOS LTDA'] = 'SHIFT GESTAO DE SERVICOS LTDA'
  temp['LINE EXPRESS TRANSPORTES E DISTRIBUICAO LTDA'] = 'LINE EXPRESS TRANSPORTES E DISTRIBUICAO LTDA'
  temp['DENISE DOS ANJOS PINTO LUCENA'] = 'DENISE DOS ANJOS PINTO LUCENA'
  temp['FLBRASIL'] = 'FLBRASIL'
  temp['FL BRASIL'] = 'FLBRASIL'
  temp['FL'] = 'FLBRASIL'
  temp['MULTI RIO OPERACOES PORTUARIAS S/A'] = 'MULTIRIO'
  temp['MULTI RIO OPERACOES PORTUARIAS S/A'] = 'MULTI RIO'
  temp['ICTSI RIO BRASIL TERMINAL 1 SA'] = 'ICTSI'
  temp['DHL GLOBAL FORWARDING (BRAZIL) LOGISTICS LTDA'] = 'DHL'
  temp['DHL GLOBAL FORWARDING (BRAZIL) LOGISTICS LTDA'] = 'DHL GLOBAL'
  
  temp['valor'] = ''
  valor = re.findall(r'[0-9]+|,[0-9][0-9]', nota['valor'])
  for e in valor:
    if e != ',00':
      temp['valor'] += e

  if re.search(r',[0-9][0-9]', temp['valor']) != None:
    temp['valor'] = re.sub(',', '.', temp['valor'])
    
  #print(temp['valor'])
  temp['con'] = re.search(r'[1-9][0-9]+', nota['con'])
  if temp['con'] != None:
    temp['con'] = temp['con'].group()
  else:
    temp['con'] = '000'
  #print(temp['con'], 'CON',nota['nome'],'NOTA NOME')

  api_json = API_Client('https://wise.klink.ai/api/admin/list/planilhavalidacao/'+temp[nota['nome']]+'/'+str(temp['con'])).result
  
  if len(api_json) > 0:
    for i in api_json:
      if i['valorFatura'] == temp['valor']:
        check = True
        #print(i['valorFatura'])
        break

  #elif check == False:
    #print('API FAIL')
    #print(temp['valor'], temp[nota['nome']], temp['con'])

  #print(temp['con'])
  """ for i in range(len(df_xl)):
    #and nota['valor'] == str(df_xl.loc[i, 'VALOR FATURA']

    if i > 8360:
        print(temp[nota['nome']],temp['valor'],temp['con'])
        print(str(df_xl.loc[i, 'TRANSPORTADORA']),str(df_xl.loc[i, 'VALOR FATURA']),str(df_xl.loc[i, 'NOTA FISCAL']))
        print()

    if str(temp.get(nota.get('nome'))) == str(df_xl.loc[i, 'TRANSPORTADORA']) and str(eval(temp['valor'])) == str(df_xl.loc[i, 'VALOR FATURA']) and str(temp['con']) == str(df_xl.loc[i, 'NOTA FISCAL']):
      
      check = True
      break """

  if check == True:
    nota['planilha'] = 'true'
    nota['validacao'] = 'true'
  else:
    nota['planilha'] = 'false'

  if(check == False):
    if nota.get("PO") != None:
      #verifica PO
      if re.search(r'[0-9]+', nota.get("PO")) == None:
        nota['validacao'] = 'false'
      else:
        nota['validacao'] = 'true'
    else:
      nota['validacao'] = 'false'
  
  return nota



def run_ocr(filename, document, output, company):
  #company = nomeFornecedor(filename)
  if company != None:
    #api_json = API_Client('https://wise.klink.ai/api/admin/list/planilhavalidacao/AGVLOGISTICA/494112').result
    centroCusto = None
    contaContabil = None
    """ for c in api_json:
      if c['razaoSocial'].upper() == company.upper():
        centroCusto = c['centroCusto']
        contaContabil = c['contaContabil']
        break """
    dados = extract_data(filename, company.split()[0], document)
    if(centroCusto != None):
      dados['centro_custo'] = centroCusto

    if(contaContabil != None):
      dados['conta_contabil'] = contaContabil

    if dados.get('desconto') != None:
      dados['valorBruto'] = dados['valor'] - dados['desconto']
    else:
      dados['valorBruto'] = dados['valor']

    if(dados.get('descricao') != None):
      dados['descricao'] = re.sub('\n', ' ', dados['descricao'])
    #print(dados)

    dados['tipoDocumento'] = document


    res = compare(dados)

    outputString = json.dumps(res)

    with open(output, 'w') as f:
      f.write(outputString)

  else:
    #res = 'No company name was found in this document.'
    res = dados = extract_data(filename, None, document)

  return res




def insert_data(filename, doctype, data: dict):
  #data['tipo_documento'] = doctype
  with open('registros.txt', 'a') as f:
    #string = f'{filename}|'+'{"tipo_documento": '+f'"{doctype}", '+'"con": '+f'"{con}", '+'"valor": '+f'"{valor}"'+'}'
    string = json.dumps(data)
    f.write(f'{filename}|{string}\n')






#img_file = sys.argv[1]

#empresa = sys.argv[2]
#docType = sys.argv[2]

#docType = str(getDocumentType(img_file))
#docType = docTypeMap[docType.lower()]

pdf_file = sys.argv[1]
outputFileName = sys.argv[2]
splitted_files = splitPDF(pdf_file)
#print(splitted_files)

#createdFiles = convertPDF2Image(pdf_file)
companyName = None
count = 0
for file in splitted_files:

  jpgFile = convertPDF2Image(file)
  docType = None

  try:
    docType = getDocumentType(jpgFile)

    infoList = dict_document.get(docType)
    if infoList != None:

      if companyName == None and 'nome' in infoList:
        companyName = nomeFornecedor(jpgFile) 
      #print(companyName)
      #print(docType)

  except:
    print('Unable to retrieve company name in', file)

  finally:
    if docType in list(dict_document.keys()):
      if companyName in list(docs_std_resolution.keys()):
        
        if count == 0:
          pageOutputName = outputFileName+'.txt'
        else:
          pageOutputName = outputFileName+f'_{count}.txt'
      
        imgFile = convertPDF2Image(file, docs_std_resolution[companyName][docType])
        try:
          out = run_ocr(imgFile, docType, pageOutputName, companyName)
          insert_data(imgFile, docType, out)
          print('JSON:', file)
          print(out)
          print()
          count += 1
        except Exception as e:
          #traceback.print_exc()
          print('Unable to read file.')

      else:
        if companyName == None or 'nome' not in infoList:
          if docType == 'custo_frete':
            try:
              out = run_ocr(imgFile, docType, pageOutputName, companyName)
              insert_data(imgFile, docType, out)
              print('JSON:', file)
              print(out)
              print()
              count += 1
            except Exception as e:
              #traceback.print_exc()
              print('Unable to read file.')
            

    else:
      print(file,'is not a valid document')



#empresa = sys.argv[2]
#docType = sys.argv[2]
#docType = str(getDocumentType(img_file))
#docType = docTypeMap[docType.lower()]

#outputFile = sys.argv[2]

#result = None

#result = run_ocr(img_file, docType, outputFile)

#print(result)
#except:
#  print('Não foi possível extrair dados')

""" try:
  out = result['nome']+result['con']+'.jpg'
  #fill_form(result, 'm210_blank.jpg', out)
except:
  print('Não foi possível gerar documento') """




