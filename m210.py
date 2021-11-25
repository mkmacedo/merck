from PIL import Image, ImageDraw, ImageFont
from groupPDF import make_pdf
import sys

def fill_form(files_info: dict, files_list: list, form, output_file):

    img = Image.open(form)
    fnt = ImageFont.truetype('Arial.ttf', 45)
    d = ImageDraw.Draw(img)
    coords = {}
    coords['con'] = (1970, 340)
    coords['nome'] = (175, 577)
    coords['vencimento'] = (1960, 440)
    coords['PO'] = (1170, 1160)
    coords['valor'] = (355, 2338)

    fields = {'nome': False, 'con': False, 'vencimento': False, 'PO': False, 'valor': False}
    
    d.text((485, 357), 'X', font=fnt, fill=(0, 0, 0))
    d.text((171,460), 'X', font=fnt, fill=(0, 0, 0))
    d.text((485,1168), 'X', font=fnt, fill=(0, 0, 0))
    d.text((147,2534), 'X', font=fnt, fill=(0, 0, 0))
    d.text((1720,1170), 'X', font=fnt, fill=(0, 0, 0))
    d.text((2045, 520), 'X', font=fnt, fill=(0, 0, 0))
    d.text((2045, 600), 'X', font=fnt, fill=(0, 0, 0))
    d.text((140,950), 'X', font=fnt, fill=(0, 0, 0))
    d.text((1305,950), 'X', font=fnt, fill=(0, 0, 0))
    d.text((1710,950), 'X', font=fnt, fill=(0, 0, 0))

    for file in files_list:
        input_data = files_info[file]
        for key in coords.keys():
            if fields[key] == False and input_data.get(key) != None:
                d.text(coords[key], input_data[key], font=fnt, fill=(0, 0, 0))
                fields[key] = True

    img.save(output_file)

flow_files = {}

for line in sys.stdin.read().split('\n'):
    
    key_value = line.split('|')
    
    flow_files[key_value[0]] = eval(key_value[1])
    flow_files[key_value[0]]['match'] = False

#print(flow_files)

files_to_group = []
keys_list = list(flow_files.keys())

if len(keys_list) > 1:
    for i in range(0, len(keys_list)):

        if i + 1 < len(keys_list) and flow_files[keys_list[i]]['match'] == False:
            
            for j in range(i + 1, len(keys_list)):

                if flow_files[keys_list[i]]['con'] == flow_files[keys_list[j]]['con'] and \
                flow_files[keys_list[i]]['valor'] == flow_files[keys_list[j]]['valor'] and \
                flow_files[keys_list[i]]['tipo_documento'] != flow_files[keys_list[j]]['tipo_documento']:

                    if flow_files[keys_list[i]]['match'] == False:
                        files_to_group.append(keys_list[i])

                    if flow_files[keys_list[j]]['match'] == False:
                        files_to_group.append(keys_list[j])
                    
                    flow_files[keys_list[i]]['match'] = True
                    flow_files[keys_list[j]]['match'] = True

else:
    files_to_group = keys_list
                    
print(files_to_group)
print(flow_files)
filled_m210 = sys.argv[1]
output_pdf = sys.argv[2]
fill_form(flow_files, files_to_group, 'm210_blank.jpg', filled_m210)

files_to_group.append(filled_m210)

make_pdf(files_to_group, output_pdf)



