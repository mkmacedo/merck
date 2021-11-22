from PIL import Image, ImageDraw, ImageFont

""" 
img = Image.open("m210_blank.jpg")
 
fnt = ImageFont.truetype('Arial.ttf', 45)
d = ImageDraw.Draw(img)
d.text((900,347), "X", font=fnt, fill=(0, 0, 0))
 
img.save(r'pil_text_font.pdf')
 """

def fill_form(input_data, form, output_file):

    img = Image.open(form)
    fnt = ImageFont.truetype('Arial.ttf', 45)
    d = ImageDraw.Draw(img)
    coords = {}
    coords['con'] = (1970, 340)
    coords['nome'] = (175, 577)
    coords['vencimento'] = (1960, 440)
    coords['PO'] = (1170, 1160)
    coords['valor'] = (355, 2338)
    
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
    

    for key in coords.keys():
        d.text(coords[key], input_data[key], font=fnt, fill=(0, 0, 0))

    img.save(output_file)
