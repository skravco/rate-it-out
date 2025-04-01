import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send_mail(customer, project, rating, comments):
    # Retrieve environment variables
    smtp_server = os.getenv('SMTP_SERVER')  # Mailtrap SMTP server
    port = int(os.getenv('SMTP_PORT', 2525))  # Mailtrap port (default: 2525)
    login = os.getenv('MAILTRAP_USERNAME')  # Mailtrap username
    password = os.getenv('MAILTRAP_PASSWORD')  # Mailtrap password
    
    # Email template content
    message = f"""
    <h3>New Feedback Submission</h3>
    <ul>
        <li><strong>Customer:</strong> {customer}</li>
        <li><strong>Project:</strong> {project}</li>
        <li><strong>Rating:</strong> {rating}</li>
        <li><strong>Comments:</strong> {comments}</li>
    </ul>
    """

    sender_email = os.getenv('SENDER_EMAIL')  # Sender email (from .env)
    receiver_email = os.getenv('RECEIVER_EMAIL')  # Receiver email (from .env)

    # Create the MIMEText object for HTML email
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'New Feedback Submission'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send the email using Mailtrap SMTP server
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Secure the connection
            server.login(login, password)  # Login to the Mailtrap SMTP server
            server.sendmail(sender_email, receiver_email, msg.as_string())  # Send the email
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")


