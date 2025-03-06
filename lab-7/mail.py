import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Email server details (for example, Gmail's SMTP)
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "kalybaev_e@auca.kg"  # Replace with your email address
sender_password = "habu igpk blaa scvq"     # Replace with your email password or app-specific password
receiver_email = "erkalybaev@gmail.com"  # Replace with the recipient's email




# HTML email content
subject = "Payment request"
body = """
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Payment Gateway Notification</title>
   <style>
       body {
           font-family: Arial, sans-serif;
           margin: 0;
           padding: 0;
           background-color: #f4f4f4;
       }
       .container {
           max-width: 600px;
           margin: 0 auto;
           background-color: #ffffff;
           padding: 20px;
           border-radius: 10px;
           box-shadow: 0 4px 8px rgba(0,0,0,0.1);
       }
       .header {
           text-align: center;
           padding-bottom: 20px;
       }
       .header h2 {
           margin: 0;
           font-size: 24px;
           color: #333;
       }
       .content {
           font-size: 16px;
           color: #333;
           text-align: center;
       }
       .button {
           display: block;
           width: 200px;
           margin: 20px auto;
           padding: 12px;
           text-align: center;
           background-color: #28a745;
           color: white;
           text-decoration: none;
           border-radius: 5px;
           font-size: 16px;
       }
       .footer {
           text-align: center;
           margin-top: 20px;
           font-size: 14px;
           color: #888;
       }
   </style>
</head>
<body>
   <div class="container">
       <div class="header">
           <h2>Secure Payment Notification</h2>
       </div>
       <div class="content">
           <p>Dear Customer,</p>
           <p>We noticed that you have a pending payment. To complete your transaction, please click the button below:</p>
           <a href="http://your-payment-gateway.com/checkout" class="button">Proceed to Payment</a>
           <p>If you did not initiate this payment, please ignore this message.</p>
       </div>
       <div class="footer">
           <p>For any inquiries, contact our support team.</p>
           <p>&copy; 2025 Payment Gateway Inc.</p>
       </div>
   </div>
</body>
</html>
"""


# Set up the MIME
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject


# Attach the body with the HTML content
message.attach(MIMEText(body, "html"))


# Send the email
try:
   # Establish a secure session with the server
   server = smtplib.SMTP(smtp_server, smtp_port)
   server.starttls()  # Secure the connection
   server.login(sender_email, sender_password)  # Log into the email server
   text = message.as_string()
   server.sendmail(sender_email, receiver_email, text)  # Send the email
   print("Email sent successfully!")
except Exception as e:
   print(f"Error sending email: {e}")
finally:
   server.quit()  # Close the connection
