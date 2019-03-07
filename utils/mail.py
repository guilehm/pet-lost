import requests
from django.template.loader import render_to_string

from petLost.settings import DEFAULT_FROM_EMAIL, MAILGUN_API_KEY, MAILGUN_API_URL


def send_mail(
    to,
    subject,
    template='base',
    from_email=DEFAULT_FROM_EMAIL,
    cc=None,
    bcc=None,
    context=None,
):

    html_message = render_to_string(f'email/{template}.html', context)

    if MAILGUN_API_KEY:
        return requests.post(
            MAILGUN_API_URL + "/messages",
            auth=("api", MAILGUN_API_KEY),
            data={
                "from": from_email,
                "to": to,
                "cc": cc,
                "bcc": bcc,
                "subject": subject,
                "html": html_message,
            }
        )
