def export():
    import smtplib
    import os
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "ameykpatel@gmail.com"
    # toaddr = "sens@iiti.ac.in"
    toaddr = "cse160001003@iiti.ac.in"

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Sourcemeter Readings"

    body = "Hello"

    msg.attach(MIMEText(body, 'plain'))

    filename = "sourcemeter_records.csv"
    path = os.path.realpath(filename)
    attachment = open(path, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "cyclehelp@123")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

export()
