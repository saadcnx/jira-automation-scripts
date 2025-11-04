from jira import JIRA
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import  encoders
from datetime import *
import time as t

user = '' # add your jira account email
apikey = '' # add your api token
server = '' # add your jira server

jira = JIRA(server=server, basic_auth=(user, apikey))


issue_in_project = jira.search_issues('created >= -5m AND project = SP and assignee in (empty) and resolution = Unresolved')
total= len(issue_in_project)

tnumber=[]
uname=[]
eaddress=[]
subdetails=[]

for issues in issue_in_project:
    ticket_number = str(issues.key)
    tnumber.append(ticket_number)

    username= str(issues.fields.reporter)
    uname.append(username)

    emailadd = issues.fields.reporter.emailAddress
    eaddress.append(emailadd)

    sdetails = issues.key + ":" + issues.fields.summary
    subdetails.append(sdetails)


if total==0:
    print("JIRA not found from last 5 min ")
else:
    print("JIRA found")
    for jiraticket in range(total):
        my_mail = "" # add your mail
        password = "" # add your app password
        msg = MIMEMultipart()
        msg['Subject'] = subdetails[jiraticket]
        msg['From'] = my_mail
        msg['To'] = eaddress[jiraticket]
        msg['Cc'] = 'saad3nd77@gmail.com'

        body="<p> Dear " + uname[jiraticket] +" , <br> <br> Thank you for writing us. <br> <br> This reply to acknowledgment your message. We have received your JIRA ticket number : " +tnumber[jiraticket] + " and our team is looking into it and we will get back to you , We look forward to intrect soon. <br><br> Thank you <br> Support team</p>"
        t.sleep(3)
        msg.attach(MIMEText(body, 'html'))
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()  # TLS transport layer security

        connection.login(user=my_mail, password=password)
        connection.send_message(msg)
        print("mail has been sent " ,uname[jiraticket] )
        connection.close()

