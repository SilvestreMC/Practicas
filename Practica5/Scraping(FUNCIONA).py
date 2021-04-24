import os
import requests
from lxml import html
import re

url="https://wall.alphacoders.com/by_resolution.php?w=3840&h=2160&lang=Spanish"

print("Obteniendo fondos de pantalla de : "+ url)
        
response = requests.get(url)  
parsed_body = html.fromstring(response.text)
    
links = parsed_body.xpath('//a/@href')
exp_regular= re.compile(r"big.php\S*")
mo = exp_regular.findall(str(links))
#print(links)
#print(mo)

os.system("mkdir images")
url="https://wall.alphacoders.com/"
for php in mo:
	print("\nObteniendo la imagen de la url: "+url+php)
	link=url+php
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
			if download.endswith("thumb-", 1, 42):
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



