import yagmail
from plyer import notification
import winsound

EMAIL = "your_email@gmail.com"
PASSWORD = "app_password"
TO_EMAIL = "receiver@gmail.com"


def send_email(alerts):

    yag = yagmail.SMTP(EMAIL, PASSWORD)

    subject = "SERVER ALERT"

    body = "\n".join(alerts)

    yag.send(TO_EMAIL, subject, body)


def desktop_alert(alerts):

    notification.notify(

        title="System Alert",

        message="\n".join(alerts),

        timeout=5

    )


def alarm():

    duration = 1000   # milliseconds

    freq = 1000       # Hz

    winsound.Beep(freq, duration)