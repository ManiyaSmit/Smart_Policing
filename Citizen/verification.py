import yagmail
import random

admin_email = "jsamurai946@gmail.com"  
admin_password = "atnj hdvj fyzf btrk"  

verification_code = str(random.randint(100000, 999999))

def send_verification_email(firstname, lastname, email):
    subject = "SafeCity Account Verification Code"
    message = f"Hello {firstname + ' ' + lastname},\nThank you for registering with SafeCity. Your safety and security are our top priorities.\nTo complete your registration, please use the following verification code:\nVerification Code: {verification_code}\nPlease ensure that you keep this code private and do not share it with others. It is essential for your account security.\nThank you!"
    try:
        yag = yagmail.SMTP(admin_email, admin_password)
        yag.send(
            to = email,
            subject = subject,
            contents = message,
        )
        return f"Verification code has been sent via email to {email}.", True, verification_code
    except Exception as e:
        return f"There was an error sending email: {str(e)}", False, 0


'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

verification_code = str(random.randint(100000, 999999))

sender_email = "jeetbherwani2004@gmail.com"  
sender_password = "okdok1334" 
recipient_email = "jsamurai946@gmail.com"
subject = "Verify the registeration"
message = f"You recently registered to create a new account for SafeCity, your verification code is {str(verification_code)}"

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject

msg.attach(MIMEText(message, "plain"))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)  # Use the appropriate SMTP server and port (e.g., for Gmail)
    server.starttls()  # Use TLS encryption
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()
    print("Email sent successfully.")
except Exception as e:
    print(f"Error sending email: {str(e)}")

    
'''