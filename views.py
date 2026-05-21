#views - handles the relevant individual views
from flask import render_template,request
import base64
import secrets
import string
from array import *

ALNUM = string.digits + string.ascii_uppercase + string.ascii_lowercase
ALNUM_PUNCT = ALNUM + string.punctuation

def _gen(pool, length):
    return ''.join(secrets.choice(pool) for _ in range(length))

def _gen_many(pool, length, count):
    return [_gen(pool, length) for _ in range(count)]

def ip_address():
    return request.remote_addr

def decent_pass():
    return _gen(ALNUM, 10)

def strong_pass():
    return _gen(ALNUM_PUNCT, 15)

def ftknox_pass():
    return _gen(ALNUM_PUNCT, 30)

def ci_key():
    return _gen(ALNUM, 33)

def wpa_160_key():
    return _gen(ALNUM_PUNCT, 33)

def wpa_504_key():
    return _gen(ALNUM_PUNCT, 63)

def list_encoder(set):
    #convert to list
    set_to_list = list(set)
    #iterate over list to base64 encode
    for i in range(len(set_to_list)):
        #base64 encode via string to byte and back to string
        set_to_list[i] = base64.b64encode(set_to_list[i].encode("utf-8")).decode("utf-8")
    return set_to_list


def front_page():
    #decent
    #set of passes
    decent_passes = list_encoder(_gen_many(ALNUM, 10, 3))
    strong_passes = list_encoder(_gen_many(ALNUM_PUNCT, 15, 3))
    ftknox_passes = list_encoder(_gen_many(ALNUM_PUNCT, 30, 3))
    ci_key_passes = list_encoder(_gen_many(ALNUM, 33, 3))
    wpa_160_passes = list_encoder(_gen_many(ALNUM_PUNCT, 33, 3))
    wpa_504_passes = list_encoder(_gen_many(ALNUM_PUNCT, 63, 3))

    return render_template('base.html', ip=ip_address(),decent=decent_passes,strong=strong_passes,ftknox=ftknox_passes,ci_key=ci_key_passes,wpa_160=wpa_160_passes,wpa_504=wpa_504_passes)