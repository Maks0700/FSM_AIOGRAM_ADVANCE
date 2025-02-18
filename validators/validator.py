from aiogram.types import Message
from email_validator import validate_email,EmailNotValidError

def valid_email_filter(message:Message)->dict[str,str] | None:
    try:
        email=validate_email(message.text)
    except EmailNotValidError:
        return None
    return {"email":email.normalized}


def valid_email(text: str) -> str | None:
    try:
        email = validate_email(text)
    except EmailNotValidError:
        return None
    return email.normalized

# def valid_email_message_text(message: Message) -> str | None:
#     return valid_email(message.text)