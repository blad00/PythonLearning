from dataclasses import dataclass
import smtplib
from email.message import EmailMessage


def _create_message(sender: str, reciever: str, subject: str, content: str) -> EmailMessage:
    msg = EmailMessage()
    msg['Subject'] = subject
    msg["From"] = sender
    msg["To"] = reciever
    msg.set_content(content)
    return msg


@dataclass
class Email:
    host: str = "10.10.10.10"  # SMTP host used within rz
    port: int = 25   # port used within RZ

    def send(self, sender: str, reciever: str, subject: str, content) -> None :
        """ sends email"""
        msg = _create_message(sender, reciever, subject, content)
        with smtplib.SMTP(self.host, self.port) as smtp:
            smtp.send_message(msg)


if __name__ == "__main__":
    # if you use a different host, call like this: 
    # email = Email(host="smtp.gmail.com", port=425)  
    # remember, there is no authorisation in this simple class yet as it's not necessary within RZ
    # so above will not work
    email = Email() # using defaults

    content_text = """This is a 
multiline, plain text
body for the email"""

    email.send(
        sender="d.cruz@rijkzwaan.nl",
        reciever="d.cruz@rijkzwaan.nl",
        subject="test of email class", 
        content=content_text)
