import flask
from flask import request, jsonify
import smtplib, ssl
from email.mime.text import MIMEText

app = flask.Flask(__name__)
app.config["DEBUG"] = False

def send_email(recipient, subject, body):
  fromx = 'projekt.weby2@gmail.com'
  to  = recipient
  password = "<<here paste the password>>"
  msg = MIMEText(body)
  msg['Subject'] = subject
  msg['From'] = fromx
  msg['To'] = to

  server = smtplib.SMTP('smtp.gmail.com:587')
  server.starttls()
  server.ehlo()
  server.login(fromx, password)
  server.sendmail(fromx, to, msg.as_string())
  server.quit()

  return "Success: requested email has been sent"

@app.route('/sendemail', methods = ['POST'])
def send_email_handler():
    content = request.get_json()
    recipient = content['recipient']
    subject = content['subject']
    body = content['body']
    response = send_email(recipient, subject, body)
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=33302, debug=True)
