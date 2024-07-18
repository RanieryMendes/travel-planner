import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_email, body):
    from_email = "k4eie5l2psy5t6tj@ethereal.email"
    login = "k4eie5l2psy5t6tj@ethereal.email"
    key = "Hy9n4P3GBQZkaKCaFV"

    message = MIMEMultipart()
    message["from"] = "trip_confirmation@email.com"
    message["to"] = ', '.join(to_email)

    message["Subject"] = "Congratulations! Your trip has been confirmed :)"
    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(host="smtp.ethereal.email", port=587 ) #587 is not secure
    server.starttls()
    server.login(login, password=key)
    text_email = message.as_string()

    for email in to_email:
        server.sendmail(from_addr=from_email, to_addrs=email, msg=text_email)
    server.quit()

    
