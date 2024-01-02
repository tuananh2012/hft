
import smtplib
class Notification:
    # creates SMTP session
    def SendEmail(self, subject):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # start TLS for security
        s.starttls()
        # Authentication
        s.login("tuananh.ams", "gzdcgupk xroe usuh")
        # message to be sent
        # sending the mail
        message = """\
        Subject: Hi there

        """ + subject
        print("subject:", subject, "target: " , self.target)
        s.sendmail("tuananh.ams", self.target, message)
        # terminating the session
        s.quit()
    def SetTarget(self, target):
        self.target = target