import smtplib

class sendMail:

    def __init__(self, to, cc, bcc):
    
        """Initialize the instance where the email address stored"""

        self.to = to
        self.cc = cc
        self.bcc = bcc

    def sending(self):
        
        """Sending mail through python by calling sending method.
        it takes the email address as an arguments after sending mail it prints 
        a message "Sucessfully sent" in terminal"""

        from_mail = 'radhamaredi1995@gmail.com'
        password = 'yqozteemfxuiurzs'

        subject = "Sending mail using Python"
        body = "Hi! i am Radha, this mail generated by python"

        message = f'To: {self.to} \rCc: {", ".join(self.cc)} \r\nSubject: {subject}\n\n{body}'
        
        #puts the connection to the SMTP server into SSL mode.
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        #smtp_server =smtplib.SMTP('smtp.gmail.com',587)  
        #smtp_server.starttls() # security purpose
        smtp_server.login(from_mail, password)
        smtp_server.sendmail(from_mail, [self.to] + self.cc + self.bcc, message)
        smtp_server.close()
        print ("Successfully sent")


email1 = sendMail('vibha.rawan@neosoftmail.com',['grandheraj68@gmail.com'],['mailto:lakshmi73862@gmail.com'])
 
email1.sending()