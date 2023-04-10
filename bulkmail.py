import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email login credentials
sender_email = "Your Email Id"
sender_password = "Your Email Password"

# Email message
message = MIMEMultipart()
message["From"] = "shubhanshu"
message["Subject"] = "Bulk Email Test"

# Read CSV file
with open('C:\\Users\\shubh\\Downloads\\mail.csv') as file:
    reader = csv.reader(file)
    next(reader) # skip header row
    for name, email in reader:
        # Add recipient to message
        message["To"] = email
        
        # Email body
        body = f"Dear {name},\n\nThis is a test email sent in bulk using Python.\n\nBest regards,\nshubhanshu"
        message.attach(MIMEText(body, "plain"))
        
        try:
            # Send email
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, email, message.as_string())
                print(f"Email sent to {name} ({email})")
        except smtplib.SMTPAuthenticationError:
            print("Unable to authenticate. Please check your email address and password.")

#For more details read the readme file