#!/usr/bin/env python3
import os
import requests
from lxml import html
import re

url="https://www.xtrafondos.com/"

print("Obteniendo fondos de pantalla de : "+ url)
        
response = requests.get(url)  
parsed_body = html.fromstring(response.text)
    
links = parsed_body.xpath('//a/@href')
exp_regular= re.compile(r"https://www.xtrafondos.com/wallpaper/\S*")
mo = exp_regular.findall(str(links))
#print(mo)

os.system("mkdir images")
for link in mo:
	print("\nObteniendo imagenes de la url: "+link[:-2])
	link = link[:-2]
	try:
		response = requests.get(str(link))  
		parsed_body = html.fromstring(response.text)
		# expresion regular para obtener imagenes
		images = parsed_body.xpath('//img/@src')
		for image in images:
			if image.startswith("http") == False:
				download = link + image
			else:
				download = image
			if download.endswith("thumbs", 0, 33) == False:
				print(download)
				# download images in images directory
				r = requests.get(download)
				f = open('images/%s' % download.split('/')[-1], 'wb')
				f.write(r.content)
				f.close()
                
	except Exception as e:
		print(e)
		print ("Error conexion con " + url)
		pass
