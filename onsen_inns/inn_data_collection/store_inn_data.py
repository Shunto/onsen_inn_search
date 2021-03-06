'''
storing inn data we get

input : none

function : 
1: to call the function from jaran_onsen_api.py at each area id and get the data of all inns existing within that area.  
2: to store all the inns' data we get into our database by mapping the all inns' data to our onsen inn model

output : none
'''

import os
import sys, getopt
import urllib.request
from bs4 import BeautifulSoup
from xml.dom.minidom import parseString
import random
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from scrape_onsen_html import scrapeOnsenHtml
#from scrape_onsen_html_sub import scrapeOnsenHtml

sys.path.append("..")
sys.path.append("../..")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onsen_inn_search.setting\
s')
import django
django.setup()

from onsen_inns.models import Onsen, OnsenInn
inn_count = 0
onsen_inn_error_list = []

def main():
    #onsens = Onsen.objects.all()
    #onsen = onsens[3]
    #onsen_area_id = onsen.onsen_area_id
    #url = "https://www.jalan.net/onsen/OSN_" + str(onsen_area_id) + ".html"
    '''url = "https://www.jalan.net/onsen/OSN_50137.html"
    print(url)
    inn_data = scrapeOnsenHtml(url)
    print(onsen.onsen_name)
    storeInnData(onsen, inn_data)'''
    try:
        onsens = Onsen.objects.all()
        for onsen in onsens:
            inn_data = []
            onsen_area_id = onsen.onsen_area_id

            if onsen_area_id is None:
                continue

            url = "https://www.jalan.net/onsen/OSN_" + str(onsen_area_id) + ".html"
            print(url)
            inn_data = scrapeOnsenHtml(url)
            print(onsen.onsen_name)
            print(inn_data)
            storeInnData(onsen, inn_data)
    except urllib.error.HTTPError as error:
        print(error)
    except Exception as e:
        print("Error URL:" + url)
        print("Error Message(store_inn_data.py): ", e)

def storeInnData(onsen, inn_data):
    #global inn_count
    global onsen_inn_error_list
    
    try:
        for data in inn_data:
            if not OnsenInn.objects.filter(inn_id=data[0]).exists():
                onsen_inn = OnsenInn()
                onsen_inn.inn_id = data[0]
                onsen_inn.inn_name = data[1]
                saveInnImage(onsen_inn, data[2])
                onsen_inn.inn_min_price = data[3]
                onsen_inn.review_room = data[4]
                onsen_inn.review_bath = data[5]            
                onsen_inn.review_breakfast = data[6]
                onsen_inn.review_dinner = data[7]
                onsen_inn.review_service = data[8]
                onsen_inn.review_cleaness = data[9]
                onsen_inn.rooms_total = data[10]
                onsen_inn.baths_total = data[11]

                onsen_inn.service_leisure = data[12]

                onsen_inn.free_wifi = data[13]
                onsen_inn.convenience_store = data[14]

                onsen_inn.hand_towel = data[15]
                onsen_inn.body_wash = data[16]
                onsen_inn.hairdryer = data[17]
                onsen_inn.onsui_toilet = data[18]

                onsen_inn.dental_amenities = data[19]
                onsen_inn.bar_soap = data[20]
                onsen_inn.duvet = data[21]
                onsen_inn.hair_brush = data[22]

                onsen_inn.bath_towel = data[23]
                onsen_inn.yukata = data[24]
                onsen_inn.razor = data[25]

                onsen_inn.shampoo = data[26]
                onsen_inn.pajamas = data[27]
                onsen_inn.shower_cap = data[28]

                onsen_inn.conditioner = data[29]
                onsen_inn.bathrobe = data[30]
                onsen_inn.cotton_swab = data[31]
                onsen_inn.vote_score = 0
                onsen_inn.num_vote_up = 0
                onsen_inn.num_vote_down = 0
                #onsen_inn.category = data[32]
                onsen_inn.onsen = onsen
                onsen_inn.save()
            #inn_count+=1

    except Exception as e:
        onsen_inn_error = [onsen_inn.inn_name, onsen_inn.inn_id]
        onsen_inn_error_list.append(onsen_inn_error)
        print("Error Onsen Inn:", onsen_inn_error)
        print("All Error Onsen Inn So Far:", onsen_inn_error_list)
        print("Error Message(store_inn_data.py, storeInnData): ", e)


def saveInnImage(model, url):
    #try:
    img_tmp = NamedTemporaryFile(delete = True)
    img_tmp.write(urllib.request.urlopen(url).read())
    img_tmp.flush()
    #model.inn_photo = "/images/inn_image_"+str(model.inn_id)+".jpg"
    model.inn_photo.save("inn_image_"+str(model.inn_id)+".jpg", File(img_tmp), save=False)
    #model.inn_photo.save("inn_image_"+str(model.inn_id)+".jpg", File(img_tmp), save=True)
    #except urllib.error.HTTPError as error:
    #    pass
    #except Exception as e:
    #    print("Error(store_inn_data.py, saveInnImage) URL:" + url)

if __name__ == "__main__":

    main()
    print("onsen_inn_error_list", len(onsen_inn_error_list) onsen_inn_error_list)
