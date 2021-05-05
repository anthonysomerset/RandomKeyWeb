#views - handles the relevant individual views
from flask import render_template,request
from strgen import StringGenerator as SG
import base64
from array import *

def ip_address():
    return request.remote_addr

def decent_pass():
    return SG(fr"[\d\u\c]{{10}}").render()

def strong_pass():
    return SG(fr"[\d\u\c\p]{{15}}").render()

def ftknox_pass():
    return SG(fr"[\d\u\c\p]{{30}}").render()

def ci_key():
    return SG(fr"[\d\u\c]{{33}}").render()

def wpa_160_key():
    return SG(fr"[\d\u\c\p]{{33}}").render()

def wpa_504_key():
    return SG(fr"[\d\u\c\p]{{63}}").render()

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
    decent_passes = list_encoder(SG(fr"[\d\u\c]{{10}}").render_set(3))
    strong_passes = list_encoder(SG(fr"[\d\u\c\p]{{15}}").render_set(3))
    ftknox_passes = list_encoder(SG(fr"[\d\u\c\p]{{30}}").render_set(3))
    ci_key_passes = list_encoder(SG(fr"[\d\u\c]{{33}}").render_set(3))
    wpa_160_passes = list_encoder(SG(fr"[\d\u\c\p]{{33}}").render_set(3))
    wpa_504_passes = list_encoder(SG(fr"[\d\u\c\p]{{63}}").render_set(3))

    return render_template('base.html', ip=ip_address(),decent=decent_passes,strong=strong_passes,ftknox=ftknox_passes,ci_key=ci_key_passes,wpa_160=wpa_160_passes,wpa_504=wpa_504_passes)