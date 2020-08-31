import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
fromaddr = 'email_address'
toaddr = 'email_address'
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Mail Sending Test"
body = "Body of the mail"
msg.attach(MIMEText(body, 'plain'))

filename = "df_closure_learn.pickle"

attachment = open("pickle1.pickle", "rb") 

p = MIMEBase('application', 'octet-stream') 
p.set_payload((attachment).read()) 
encoders.encode_base64(p) 
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
s.starttls() 
# Authentication 
s.login(fromaddr, "password") 
# Converts the Multipart msg into a string 
text = msg.as_string() 
# sending the mail 
s.sendmail(fromaddr, toaddr, text) 
# terminating the session 
s.quit() 


### https://myaccount.google.com/lesssecureapps