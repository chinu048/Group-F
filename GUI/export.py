def export(sendersEmail,receiversEmail,password,path,filename):
    import smtplib
    import os
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = sendersEmail
    toaddr = receiversEmail

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Sourcemeter Readings"

    body = "Hello"

    msg.attach(MIMEText(body, 'plain'))

    attachment = open(path, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

#export('ameykpatel@gmail.com','cse160001003@iiti.ac.in','cyclehelp@123','C:/Users/Amey Patel/Desktop/test_generate_csv.csv','ssd')
