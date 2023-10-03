import codecs 
import re
import string
import os
import math
import csv
import pandas as pd
import numpy as np
def main():
    data = pd.read_csv('unseen\\UnseenTagClass.csv',header=0)
    data_change = cat_to_reg(data)
    print(data_change)
    k=0
    for key in data_change:
        f = open("unseen\\"+str(key)+'Plot.txt', 'w')
        f.write('''# Region file format: DS9 version 4.1
    # global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1
    # fk5\n''')
        if k==6:
            break
        for i in data_change[key]:
            f.write(i+"\n")
        f.close()
        k+=1
    # data = pd.read_csv('Exp7 17 Feb\\EMIter100Result.csv',header=0)
    # data_change = cat_to_reg(data)
    # #print(data_change)
    # for key in data_change:
    #     f = open("Exp7 17 Feb\\"+key+'Plot.txt', 'w')
    #     f.write('''# Region file format: DS9 version 4.1
    # # global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1
    # # fk5\n''')
    #     for i in data_change[key]:
    #         f.write(i+"\n")
    #     f.close()
# def main():
#     for i in range(4,8):
#         nameFile="Density"+str(i)+".csv"
#         #nameFile="EM"+str(i)+".csv"
#         data = pd.read_csv('Exp5 9 Feb\\'+nameFile,header=0)
#         data_change = cat_to_reg(data)
#         nameExport="Exp5 9 Feb\\"+"Plot"+nameFile+".txt"
#         f = open(nameExport, 'w')
#         f.write('''# Region file format: DS9 version 4.1
#     # global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1
#     # fk5\n''')
#         for i in data_change:
#             f.write(i+"\n")
#         f.close()

def ra_convert(ra):
    h = int(ra//15)
    m = int(math.floor(((ra/15)-h)*60))
    s = ((((ra/15)-h)*60)-m)*60
    
    return str(h)+":"+str(m)+":"+'{:.4f}'.format(s)

def dec_convert(dec):
    d = int(math.floor(dec))
    arcmin = int(math.floor((dec-d)*60))
    arcsec =  (((dec-d)*60)-arcmin)*60
    return "+"+str(d)+":"+str(arcmin)+":"+'{:.3f}'.format(arcsec)

def cat_to_reg(data):
    list_ra_dec = []
    #ver1
    #cluster_color = {'cluster0':'cyan', 'cluster1':'green', 'cluster2':'red', 'cluster3':'yellow', 'cluster4':'magenta', 'cluster5':'white'}

    #ver2
    # cluster_color = {
    # 'cluster0':'#FF69B4',                       #rgb(255,105,180)   สีชมพู
    # 'cluster1':'#DC143C',                       #rgb(220,20,60)  สีแดงเลือดหมู
    # 'cluster2':'#DAA520',                       #rgb(218,165,32)    สีเหลืองแก่
    # 'cluster3':'#FF8C00',                       #rgb(255,140,0)     สีส้ม
    # 'cluster4':'#BA55D3',                       #rgb(186,85,211)    สีม่วงชมพู
    # 'cluster5':'#7B68EE',                       #rgb(123,104,238) 	สีม่วงคราม
    # 'cluster6':'#ADFF2F',                       #rgb(173,255,47) 	สีเขียวสด
    # 'cluster7':'#006400',                       #rgb(0,100,0) 	    สีเขียวแก่
    # 'cluster8':'#66CDAA',                       #rgb(102,205,170) 	สีเขียวทะเล
    # 'cluster9':'#00FFFF',                       #rgb(0,255,255) 	สีฟ้าสด
    # 'cluster10':'#B0C4DE',                      #rgb(176,196,222) 	สีฟ้าครึ้มเทา
    # 'cluster11':'#0000FF',                      #rgb(0,0,255) 	    สีน้ำเงิน
    # 'cluster12':'#778899',                      #rgb(119,136,153) 	สีเทา
    # 'cluster13':'#000000',                      #rgb(0,0,0) 	    สีดำ
    # 'cluster14':'#D3D3D3',                      #rgb(211, 211, 211) สีเทาขาวสว่าง
    # 'cluster15':'#8B4513',                      #rgb(139, 69, 19) 	สีน้ำตาล
    # 'cluster16':'#FFFFFF',                      #rgb(255,255,255) 	สีขาว
    # }
    # list_cluster = {
    #     "cluster0":[],
    #     "cluster1":[],
    #     "cluster2":[],
    #     "cluster3":[],
    #     "cluster4":[],
    #     "cluster5":[],
    #     "cluster6":[],
    #     "cluster7":[],
    #     "cluster8":[],
    #     "cluster9":[],
    #     "cluster10":[],
    #     "cluster11":[],
    #     "cluster12":[],
    #     "cluster13":[],
    #     "cluster14":[],
    #     "cluster15":[],
    #     "cluster16" :[]}

    g_color = {
    'g1':'#DC143C',                       #rgb(220,20,60)  สีแดงเลือดหมู
    'g2':'#DAA520',                       #rgb(218,165,32)    สีเหลืองแก่
    'g3':'#7B68EE',                       #rgb(123,104,238) 	สีม่วงคราม
    'g4':'#006400',                       #rgb(0,100,0) 	    สีเขียวแก่
    'g5':'#00FFFF',                       #rgb(0,255,255) 	สีฟ้าสด
    'g6':'#8B4513',                      #rgb(139, 69, 19) 	สีน้ำตาล
    }
    list_group = {
        "g1":[],
        "g2":[],
        "g3":[],
        "g4":[],
        "g5":[],
        "g6":[],
      }
    
    for i in range(len(data)):
        ra = ra_convert(data['ALPHAPEAK_J2000_I'][i])
        dec = dec_convert(data['DELTAPEAK_J2000_I'][i])
        cluster=data['Cluster'][i]
        string_to_add = "circle("+ra+","+dec+",2"+'"'+")" + "# color = " + g_color[cluster]
        empty= list_group[cluster]
        empty.append(string_to_add)
        list_group[g_color[cluster]] = empty

    return list_group


if __name__ == "__main__":
    main()