# Background worker for task queue

import os
import requests
import jinja2
from dotenv import load_dotenv

load_dotenv()
domain = os.getenv("MAILGUN_DOMAIN")
api_key = os.getenv("MAILGUN_API_KEY")

template_loader = jinja2.FileSystemLoader("templates")
template_env = jinja2.Environment(loader=template_loader)


def render_template(template_filename, **context):
    return template_env.get_template(template_filename).render(**context)


def send_simple_message(to: str, subject: str, body: str, html):

    if not api_key:
        raise RuntimeError("MAILGUN_API_KEY must be provided")
    if not domain:
        raise RuntimeError("MAILGUN_DOMAIN must be provided")
    return requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", api_key),
        data={
            "from": f"<postmaster@{domain}>",
            "to": [to],
            "subject": subject,
            "text": body,
            "html": html,
        },
    )


def send_user_registration_message(email: str):
    send_simple_message(
        to=email,
        subject="Succesfully signed up!",
        body="Welcome to our app!",
        html=render_template("email/action.html"),
    )
