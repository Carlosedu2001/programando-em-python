import smtplib
import email.message

def enviar_email():
    corpo_email = """
    <p>Parágrafo 1</p>
    <p>Parágrafo 2</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"    
    msg['From'] = 'De'    
    msg['To'] = 'Para'    
    password = 'senha'    
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    
    #   Credenciais para enviar o email
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()