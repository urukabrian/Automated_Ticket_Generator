import csv
import smtplib
import ssl
from time import sleep
#from smtplib import SMTP

port = 587  # For starttls
smtp_server = "mail.nac.com.pg"
#user = input("Type your username and press enter:")
#password = input("Type your password and press enter:")
user = 'buruka'
sender_email = user + '@nac.com.pg'
password = 'Delta@170988'
#sender_email = "{user}@nac.com.pg"
receiver_email = "itservicedesk@nac.com.pg"
message = """\
Subject: {subject}


{issue}




{details}











@@Request Type={request_type}@@
@@Status={ticket_status}@@
@@Mode={reporting_mode}@@
@@Level={ticket_assignment_level}@@
@@Group={service_group}@@
@@Technician={assigned_technician}@@
@@Service Category={service_category}@@
@@E-mail ID(s) TO Notify={alert_receipients}@@
@@Site={site}@@
@@Created Date={date}@@
@@Scheduled End Time={scheduled_end_time}@@
@@Response DueBy Time={response_due_by_time}@@
@@Impact={impact}@@
@@Impact Details={impact_details}@@
@@Urgency={urgency}@@
@@Category={category}@@
@@Subcategory={subcategory}@@
@@Item={Item}@@
@@Scheduled Start Time={scheduled_start_time}@@
@@DueBy Date={dueby_date}@@
@@Request Closure Code={request_closure_code}@@
@@Request Closure Comments={request_closure_comments}@@



"""

update = """\
Ticket Processed for the issue: {subject}
"""


#with open("tasking.csv") as file:
    #reader = csv.reader(file)
    #next(reader)  # Skip header row
    #for subject, issue, details, time, assign, category, status in reader:
       #print(message.format(subject=(''.join(str(elt) for elt in subject)),issue=(''.join(str(elt) for elt in issue)),details=(''.join(str(elt) for elt in details)),time=(''.join(str(elt) for elt in time)),assign=(''.join(str(elt) for elt in assign)),category=(''.join(str(elt) for elt in category)),status=(''.join(str(elt) for elt in status)))
    #)

context = ssl.create_default_context()
with open("tasking.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    count = 0
    for subject, issue, details, time, assign, category, status in reader:
        count+= 1
        print(update.format(subject=(''.join(str(elt) for elt in subject)),issue=(''.join(str(elt) for elt in issue)),details=(''.join(str(elt) for elt in details)),time=(''.join(str(elt) for elt in time)),assign=(''.join(str(elt) for elt in assign)),category=(''.join(str(elt) for elt in category)),status=(''.join(str(elt) for elt in status))))
        print(count)
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(user, password)
            server.sendmail(
            sender_email,
            receiver_email,
            message.format(subject=(''.join(str(elt) for elt in subject)),issue=(''.join(str(elt) for elt in issue)),details=(''.join(str(elt) for elt in details)),time=(''.join(str(elt) for elt in time)),assign=(''.join(str(elt) for elt in assign)),category=(''.join(str(elt) for elt in category)),status=(''.join(str(elt) for elt in status)))
            #message.format(issue=(','.join(str(elt) for elt in issue)),subject=(','.join(str(elt) for elt in subject)),details=(','.join(str(elt) for elt in details)),time=(','.join(str(elt) for elt in time)),assign=(','.join(str(elt) for elt in assign)),category=(','.join(str(elt) for elt in category)))
            )
            server.quit()
        sleep(15)

