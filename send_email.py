import smtplib
import ssl

def send_email(receiver, message):
    host = "smtp.gmail.com"
    port = 465

    user = "python3.apps@gmail.com"
    password = "ismhrlqqexhoviei"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user, password)
        server.sendmail(receiver, user, message)

if __name__ == "__main__":
    send_email("fff", "fff")