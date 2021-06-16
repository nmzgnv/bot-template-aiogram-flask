from database.models import Texts
from database.loader import db
import logging
import re


base_texts = {
    "start_text": 'Это {}. Привет!',
    'require_channel_subscribe_text': 'Для продолжения подпишитесь на {}',
}

cached_texts = {}


def format_text_to_send(message_text):
    """
    :param message_text: text with html tags
    :return: clean text for sending in telegram
    """
    message_text = re.sub("(?s)<div(?: [^>]*)?>.*?</div>", "", message_text)  # removing divs with content
    message_text = re.sub("<br>|<br />|<br/>|</p>", '\n', message_text)
    message_text = re.sub("<p>|</p>|<ul>|</ul>|<li>|</li>|<ol>|</ol>|<div>|</div>|&nbsp;", "", message_text)
    return message_text


def caсhe_texts():
    global cached_texts
    db.create_all()

    if Texts.query.count() != len(base_texts.keys()):
        # filling database by base texts
        deleted_rows_num = db.session.query(Texts).delete()
        logging.info(f"Was deleted: {deleted_rows_num} rows from Texts table")

        for name, value in base_texts.items():
            text = Texts(name, value)
            cached_texts[name] = format_text_to_send(value)
            db.session.add(text)

        db.session.commit()
    else:
        for item in Texts.query.all():
            cached_texts[item.name] = format_text_to_send(item.value)


caсhe_texts()
cached_keys = cached_texts.keys()


def _(text_name):
    global cached_texts, cached_keys
    assert text_name in cached_keys, f'Text with name "{text_name}" not found'
    return cached_texts[text_name]
