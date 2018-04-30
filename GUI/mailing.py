def send_mail(sendersAddress,receiversAddress,mesg):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    fromaddr = sendersAddress
    toaddr = receiversAddress
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Your Password"
    body = "Userid = " + str(mesg[0]) + "\nPassword = " + str(mesg[1])
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "keithley123")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()