from gmailsendemail import SendEmailUtility
import os

remitente="hayde.mtzl@gmail.com"
destinario="adelriorz@gmail.com"
subject="Holi"
text="Holi por favor no usen mi pwd"

mailito = SendEmailUtility()
mailito.send_mail_no_attachment(remitente, "j43Y#n%%7i", destinario,subject, text)
