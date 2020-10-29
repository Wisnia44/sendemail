import flask
from sparkpost import SparkPost
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = False

def send_email(recipient, subject, body):
    #here paste the received sparkpost configuration key
    sp = SparkPost('<<here paste the key>>')
    response = sp.transmissions.send(
        use_sandbox=True,
        recipients=[recipient],
        html=body,
        from_email='projekt.weby2@sparkpostbox.com',
        subject=subject
    )
    return response

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
