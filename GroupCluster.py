import codecs 
import re
import string
import os
import math
import csv
import pandas as pd
import numpy as np
def main():

    data = pd.read_csv('EMIter100Result.csv',header=0)

    # cluster_color = {'cluster0':'#FF69B4',      #rgb(255,105,180)     สีชมพู          g2
    # 'cluster1':'#DC143C',                       #rgbrgb(220,20,60)    สีแดงเลือดหมู    g1
    # 'cluster2':'#DAA520',                       #rgb(218,165,32)      สีเหลืองแก่      g3
    # 'cluster3':'#FF8C00',                       #rgb(255,140,0)       สีส้ม             gother
    # 'cluster4':'#BA55D3',                       #rgb(186,85,211)      สีม่วงชมพู       gother
    # 'cluster5':'#7B68EE',                       #rgb(123,104,238) 	สีม่วงคราม       g2
    # 'cluster6':'#ADFF2F',                       #rgb(173,255,47) 	    สีเขียวสด        g2
    # 'cluster7':'#006400',                       #rgb(0,100,0) 	    สีเขียวแก่        g3
    # 'cluster8':'#66CDAA',                       #rgb(102,205,170) 	สีเขียวทะเล      g2
    # 'cluster9':'#00FFFF',                       #rgb(0,255,255) 	    สีฟ้าสด         g2  
    # 'cluster10':'#B0C4DE',                      #rgb(176,196,222) 	สีฟ้าครึ้มเทา       
    # 'cluster11':'#0000FF',                      #rgb(0,0,255) 	    สีน้ำเงิน       g4
    # 'cluster12':'#778899',                      #rgb(119,136,153) 	สีเทา        g4
    # 'cluster13':'#000000'                       #rgb(0,0,0) 	        สีดำ          gother
    # }

    cluster_color = {'cluster0':'#FF69B4',      #rgb(255,105,180)   สีชมพู
    'cluster1':'#DC143C',                       #rgbrgb(220,20,60)  สีแดงเลือดหมู
    'cluster2':'#DAA520',                       #rgb(218,165,32)    สีเหลืองแก่
    'cluster3':'#FF8C00',                       #rgb(255,140,0)     สีส้ม
    'cluster4':'#BA55D3',                       #rgb(186,85,211)    สีม่วงชมพู
    'cluster5':'#7B68EE',                       #rgb(123,104,238) 	สีม่วงคราม
    'cluster6':'#ADFF2F',                       #rgb(173,255,47) 	สีเขียวสด
    'cluster7':'#006400',                       #rgb(0,100,0) 	    สีเขียวแก่
    'cluster8':'#66CDAA',                       #rgb(102,205,170) 	สีเขียวทะเล
    'cluster9':'#00FFFF',                       #rgb(0,255,255) 	สีฟ้าสด
    'cluster10':'#B0C4DE',                      #rgb(176,196,222) 	สีฟ้าครึ้มเทา
    'cluster11':'#0000FF',                      #rgb(0,0,255) 	    สีน้ำเงิน
    'cluster12':'#778899',                      #rgb(119,136,153) 	สีเทา
    'cluster13':'#000000',                      #rgb(0,0,0) 	    สีดำ
    'cluster14':'#D3D3D3',                      #rgb(211, 211, 211) สีเทาขาวสว่าง
    'cluster15':'#8B4513',                      #rgb(139, 69, 19) 	สีน้ำตาล
    'cluster16':'#FFFFFF'                       #rgb(255,255,255) 	สีขาว
    }

    #group1
    data.loc[data['Cluster'] == 'cluster3', 'Cluster'] ='g1'

    #group2
    data.loc[data['Cluster'] == 'cluster9', 'Cluster'] ='g2'

    
    #group3
    data.loc[data['Cluster'] == 'cluster4', 'Cluster'] ='g3'
    data.loc[data['Cluster'] == 'cluster11', 'Cluster'] ='g3'

    #group4
    data.loc[data['Cluster'] == 'cluster1', 'Cluster'] ='g4'
    data.loc[data['Cluster'] == 'cluster2', 'Cluster'] ='g4'

    #group5
    data.loc[data['Cluster'] == 'cluster0', 'Cluster'] ='g5'
    data.loc[data['Cluster'] == 'cluster8', 'Cluster'] ='g5'
    data.loc[data['Cluster'] == 'cluster10', 'Cluster'] ='g5'    


    #group6
    data.loc[data['Cluster'] == 'cluster5', 'Cluster'] ='g6'
    data.loc[data['Cluster'] == 'cluster6', 'Cluster'] ='g6'
    # #delete group 7
    data = data.drop(data[data.Cluster =='cluster7'].index)


    data.to_csv("Exp9 2 mar\\Exp9Cluster6_cluster7_to2Group.csv",index = False)

if __name__ == "__main__":
    main()