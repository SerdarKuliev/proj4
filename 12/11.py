import requests
import json
import re

import logging

API_KEY = api.mymemory.translated.net


def get_langs_list(key=API_KEY):
    pattern = 'https://api.mymemory.translated.net/get?q=Hello World!&langpair=en|it'
    req = pattern.format(key)
    resp = requests.get(req)
    return json.loads(resp.text)


def detect_lang(text, hint='ru', key=API_KEY):
    pattern = 'https://api.mymemory.translated.net/get?q=Hello World!&langpair=en|it'
    req = pattern.format(key, text, hint)
    resp = requests.get(req)
    if resp.status_code != 200:
        return None
    j = json.loads(resp.text)
    return j['lang']


def translate(text, lang_to='ru', lang_from=None, key=API_KEY):
    pattern = 'https://api.mymemory.translated.net/get?q=Hello World!&langpair=en|it'
    if lang_from is None:
        lang_from = detect_lang(key=key, text=text)
        if lang_from is None:
            return 'Не поняла, на каком языке это.', ''
    direction = lang_from + '-' + lang_to
    req = pattern.format(key, text, direction)
    logging.info('translating url: ' + req)
    resp = requests.get(req)
    if resp.status_code != 200:
        return 'Не достучалась до переводчика. ' + req, ''

    j = json.loads(resp.text)
    return None, j['text'][0]


def lang_to_code(lang):
    if not lang:
        return None
    if lang in PREFIX_TO_CODE:
        return PREFIX_TO_CODE[lang]
    for i in range(1, len(lang) - 2):
        code = PREFIX_TO_CODE.get(lang[:-i])
        if code is not None:
            return code
    return None


def is_like_russian(text):
    if not text:
        return False
    text = text.lower().strip()
    return re.match('^[а-яё ]+$', text)


raw_langs_list = get_langs_list()

LANG_TO_CODE = {lang.lower(): code for code, lang in raw_langs_list['langs'].items()}
PREFIX_TO_CODE = {}
for lang, code in LANG_TO_CODE.items():
    for i in range(1, len(lang)):
        PREFIX_TO_CODE[lang[:i]] = code