from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass
import argparse
 
msg = MIMEMultipart()

# setup the parameters of the message

description = """Ejemplo de uso
Para que funcione el script, hacer lo siguiente:
python nombre_script.py -sender 'correo remitente' -receiver 'correo receptor' -subjet 'asunto' -message 'mensaje'
-subjet, -message : OPCIONALES
despues tendras que ingresar contraseña del correo remitente
El script funciona solo con correos de office"""

parser = argparse.ArgumentParser(description='Envio de correos', epilog=description,
formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument("-sender", metavar='SENDER', dest="sender", help="correo electrónico del remitente", required=True)
parser.add_argument("-receiver", metavar='RECEIVER', dest="receiver", help="correo electrónico del destinatario", required=True)
parser.add_argument("-subjet", metavar='SUBJET', dest="subjet", help="Asunto del correo", default="Script de prueba")
parser.add_argument("-message", metavar='MESSAGE', dest="message", help="Mensaje a enviar", default="Hola, saludos")

params = parser.parse_args()

sender = params.sender
receiver = params.receiver
subjet = params.subjet
message = params.message

password = getpass.getpass()

msg['Subject'] = subjet
# add in the message body
msg.attach(MIMEText(message, 'plain'))

#create server
server = smtplib.SMTP('smtp.office365.com:587')

server.starttls()

# Login Credentials for sending the mail
server.login(sender,password)

# send the message via the server.
server.sendmail(sender, receiver, msg.as_string())

server.quit()

print("successfully sent email to ", receiver)
