import re
import csv
import math
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
from astropy import units as u
from astropy.coordinates import SkyCoord
import copy
import os
# ข้อมูลชุด 1
#number = [5, 6, 14, 15, 23, 24, 32, 33]
# ข้อมูลชุด 2
# number = [12,13,16,17,21,22,25,26,30,31,34,35]
number= [24,25]
def main():
    g_data, r_data, i_data = file_controller()
    #key = read_key()
    ## print("key= ",key)
    # #Do G & R
    sample_g, sample_r, center_point_g_r = sample_collecting(g_data, r_data)
    # for i in range(len(sample_g)):
    #     print(i,len(sample_g[i]),len(sample_r[i]))
    all_delta_ra_dec_g_r = difference(sample_g, sample_r,"Sample R")
    data_shifting(r_data, all_delta_ra_dec_g_r)
    # # time to rotate
    GR = data_rotate(g_data, r_data, center_point_g_r, -0.40,"Sample R")
    ## print("GR = ",GR)
    #Do G & I
    sample_g, sample_i, center_point_g_i = sample_collecting(g_data, i_data)
    # for i in range(len(sample_g)):
    #     print(i,len(sample_g[i]),len(sample_i[i]))
    all_delta_ra_dec_g_i = difference(sample_g, sample_i,"Sample I")
    data_shifting(i_data, all_delta_ra_dec_g_i)
    # # time to rotate
    GI = data_rotate(g_data, i_data, center_point_g_i,  -0.40,"Sample I")
    ## print("GI = ",GI)

    match_data = matching_GI_GR(GR,GI)
    #print(match_data)
    for i in range(len(number)):
        print(number[i],len(match_data[i]))
    # # print(G)
    # matched = matching(key, G)
    # plot_key_data(G, key, 'The plot shows all G data and key')
    # # # print(matched)
    # plot_filnal(matched, 'The plot shows matched data and key')
    csv_export(match_data)

def file_controller():
    data_g, data_r, data_i = [], [], []
    rel_path = "dataset\\"
    # ข้อมูลชุด 1
    # g_file = [  'g5.cat', 'g6.cat', 'g14.cat', 'g15.cat', 'g23.cat', 'g24.cat', 'g32.cat', 'g33.cat']
    # r_file = [  'r5.cat', 'r6.cat', 'r14.cat', 'r15.cat', 'r23.cat', 'r24.cat', 'r32.cat', 'r33.cat']
    # i_file = [  'i5.cat', 'i6.cat', 'i14.cat', 'i15.cat', 'i23.cat', 'i24.cat', 'i32.cat', 'i33.cat']
    # ข้อมูลชุด การทดลอ ง10 [12,13,16,17,21,22,25,26,30,31,34,35]
    # g_file = [  'g12.cat', 'g13.cat', 'g16.cat', 'g17.cat', 'g21.cat', 'g22.cat', 'g25.cat', 'g26.cat', 'g30.cat', 'g31.cat', 'g34.cat', 'g35.cat']
    # r_file = [  'r12.cat', 'r13.cat', 'r16.cat', 'r17.cat', 'r21.cat', 'r22.cat', 'r25.cat', 'r26.cat', 'r30.cat', 'r31.cat', 'r34.cat', 'r35.cat']
    # i_file = [  'i12.cat', 'i13.cat', 'i16.cat', 'i17.cat', 'i21.cat', 'i22.cat', 'i25.cat', 'i26.cat', 'i30.cat', 'i31.cat', 'i34.cat', 'i35.cat']

    # ข้อมูลชุด การทดลอง สำหรับทดลองรัน

    g_file = [  'g24.cat', 'g25.cat']
    r_file = [  'r24.cat', 'r25.cat']
    i_file = [  'i24.cat', 'i25.cat']
    # g_file = [  'g1.cat', 'g2.cat', 'g3.cat', 'g4.cat', 'g5.cat', 'g6.cat', 
    #             'g7.cat', 'g8.cat', 'g9.cat', 'g10.cat', 'g11.cat', 'g12.cat', 
    #             'g13.cat', 'g14.cat', 'g15.cat', 'g16.cat', 'g17.cat', 'g18.cat', 
    #             'g19.cat', 'g20.cat', 'g21.cat', 'g22.cat', 'g23.cat', 'g24.cat', 
    #             'g25.cat', 'g26.cat', 'g27.cat', 'g28.cat', 'g29.cat', 'g30.cat', 
    #             'g31.cat', 'g32.cat', 'g33.cat', 'g34.cat', 'g35.cat', 'g36.cat']
    
    # r_file = [  'r1.cat', 'r2.cat', 'r3.cat', 'r4.cat', 'r5.cat', 'r6.cat', 
    #             'r7.cat', 'r8.cat', 'r9.cat', 'r10.cat', 'r11.cat', 'r12.cat', 
    #             'r13.cat', 'r14.cat', 'r15.cat', 'r16.cat', 'r17.cat', 'r18.cat', 
    #             'r19.cat', 'r20.cat', 'r21.cat', 'r22.cat', 'r23.cat', 'r24.cat', 
    #             'r25.cat', 'r26.cat', 'r27.cat', 'r28.cat', 'r29.cat', 'r30.cat', 
    #             'r31.cat', 'r32.cat', 'r33.cat', 'r34.cat', 'r35.cat', 'r36.cat']
    
    # i_file = [  'i1.cat', 'i2.cat', 'i3.cat', 'i4.cat', 'i5.cat', 'i6.cat', 
    #             'i7.cat', 'i8.cat', 'i9.cat', 'i10.cat', 'i11.cat', 'i12.cat', 
    #             'i13.cat', 'i14.cat', 'i15.cat', 'i16.cat', 'i17.cat', 'i18.cat', 
    #             'i19.cat', 'i20.cat', 'i21.cat', 'i22.cat', 'i23.cat', 'i24.cat', 
    #             'i25.cat', 'i26.cat', 'i27.cat', 'i28.cat', 'i29.cat', 'i30.cat', 
    #             'i31.cat', 'i32.cat', 'i33.cat', 'i34.cat', 'i35.cat', 'i36.cat']
    
    # g_file = ['g5.cat', 'g14.cat', 'g23.cat', 'g32.cat']
    # r_file = ['r5.cat', 'r14.cat', 'r23.cat', 'r32.cat']
    # i_file = ['i5.cat', 'i14.cat', 'i23.cat', 'i32.cat']
    for i in range(len(g_file)):
        #script_dir = os.path.dirname(g_file[i])
        #abs_file_path = os.path.join(script_dir, rel_path)
        g_list = read_file(rel_path + g_file[i])
        r_list = read_file(rel_path + r_file[i])
        i_list = read_file(rel_path + i_file[i])
        # filter magnitude(g&r) in range 15 - 25 of filter G & R
        g_updated = filter_magnitude(g_list)
        r_updated = filter_magnitude(r_list)
        i_updated = filter_magnitude(i_list)
        data_g.append(g_updated)
        data_r.append(r_updated)
        data_i.append(i_updated)
    return data_g, data_r, data_i

def convert_to_mag(data):
    zeropoint = 26.5520
    exptime = 660.252
    result = float(data) + zeropoint + 2.5*(math.log(exptime, 10))
    return result

def convert_RA(h,m,s):
    return (h+(m/60)+(s/3600))*15

def convert_Dec(d,arcmin,arcsec):
    return d+(arcmin/60)+(arcsec/3600)

def read_file(filename):
    data = []
    myfile = open(filename)
    info = myfile.readlines()
    for i in range(len(info)):
        info[i].rstrip('\n')
        a = re.findall(r"\S+", info[i])
        if(a[0] != '#'):
            temp = []
            temp.append(float(a[12]))   # 0: RA
            temp.append(float(a[13]))   # 1: DEC
            temp.append(float(a[1]))    # 2: MAG_APER
            temp.append(filename)       # 3: file name
            temp.append(int(a[0]))           # 4: Object number
            temp.append(float(a[14]))   # 5: X
            temp.append(float(a[15]))   # 6: Y
            data.append(temp)
        myfile.close()
    return data

def read_key():
    filename = 'aj403657t2_mrt.txt'
    header = "F:\\Narit-Internship\\Python\\"
    myfile = open(header + filename)
    info = myfile.readlines()
    key_splited = []
    for j in range(len(info)):
        temp = []
        if(j >= 5):  # start at line 5 [you can change parameter here.]
            info[j] = info[j].rstrip('\n')
            info[j] = re.findall(r'\S+', info[j])
            if filename == 'aj341087t2_ascii.txt':
                temp.append(info[j][4])  # get RA
                temp.append(info[j][5])  # get Dec
            elif filename == 'aj403657t2_mrt.txt':
                ra = info[j][1] + ':' + info[j][2] + ':' + info[j][3]
                dec = info[j][4] + ':' + info[j][5] + ':' + info[j][6]
                temp.append(ra)  # get RA
                temp.append(dec)  # get DEC
            # temp.append(info[j][0])  # get No.
            # temp.append(info[j][2])  # get PR95
            key_splited.append(temp)
            myfile.close()
    # convert RA and DEC to floating form
    key = convert_to_degree(key_splited)
    return key

def convert_to_degree(key_splited):
    for i in range(len(key_splited)):
        # use for file 'aj341087t2_ascii.txt' that RA and Dec have ':' between number
        ra = key_splited[i][0].split(':')
        dec = key_splited[i][1].split(':')
        # calculate HH:MM:SS to degree RA
        key_splited[i][0] = (float(ra[0]) + float(ra[1]) /
                             60 + float(ra[2])/3600)*15        # RA
        key_splited[i][1] = float(
            dec[0]) + float(dec[1])/60 + float(dec[2])/3600          # DEC

        # shift key condition
        key_splited[i][0] += 0.0113
        key_splited[i][1] -= 0.00276
        # key_splited[i][0] += 0.0
        # key_splited[i][1] -= 0.0
    return key_splited

def read_text(filename):
    data = []
    myfile = open(filename)
    info = myfile.readlines()
    for i in info:
        i.rstrip('\n')
        a = re.findall(r"\S+", i)
        if(a[0] != '#'):
            temp=[]
            temp.append(int (a[0]))
            temp.append(float (a[1]))
            temp.append(float (a[2]))
            temp.append(float (a[3]))
            temp.append(float (a[4]))
            temp.append(float (a[5]))
            temp.append(float (a[6]))
            data.append(temp)
    myfile.close()
    return data

def map_key_mag(ra_dec_K, vm):
    key_vmag = []
    for j in range(len(ra_dec_K)):
        temp = []
        for k in range(len(vm)):
            # if reference number are matched with ID of key file
            if vm[k][1] == ra_dec_K[j][2] or vm[k][2] == ra_dec_K[j][3]:
                # then add v_mag into key file in index at ID
                temp.append(ra_dec_K[j][0])  # RA
                temp.append(ra_dec_K[j][1])  # DEC
                temp.append(vm[k][3])   # V_mag
        if temp != []:
            key_vmag.append(temp)
    return key_vmag

def filter_magnitude(data):
    result = []
    for i in range(len(data)):
        # convert_mag_aper_to_gmagnitude
        data[i][2] = convert_to_mag(data[i][2])
        # if gmagnitude is in rangr (15-25)
        result.append(data[i])  # keep all data in set (RA,DEC,G_MAG)
    # sort the data by using magnitude. then select 30 first stars to the process
    sort_list = sorted(result, key=lambda l: l[2], reverse = False)
    ## print(len(sort_list))
    # select top 30 row that are sorted
    result = sort_list[0:600]
    ## print(len(result))
    return result


def sample_collecting(g_data, r_data):
    ## print(g_data)
    center_p_collect = []
    all_center_p_collect = []
    # collecting sample g&r by using PIXEL x = 1006-1106 and y = 2272-2372
    sample_g, sample_r = [], []
    for i in range(len(g_data)):
        center_point = []
        temp = []
        # min
        min_ra_g = min(g_data[i], key=lambda l: l[0])
        min_dec_g = min(g_data[i], key=lambda l: l[1])
        min_ra_r = min(r_data[i], key=lambda l: l[0])
        min_dec_r = min(r_data[i], key=lambda l: l[1])
        # max
        max_ra_g = max(g_data[i], key=lambda l: l[0])
        max_dec_g = max(g_data[i], key=lambda l: l[1])
        max_ra_r = max(r_data[i], key=lambda l: l[0])
        max_dec_r = max(r_data[i], key=lambda l: l[1])
        # set treshold
        ra_g_center = (max_ra_g[0] + min_ra_g[0])/2
        dec_g_center = (max_dec_g[1] + min_dec_g[1])/2
        ra_r_center = (max_ra_r[0] + min_ra_r[0])/2
        dec_r_center = (max_dec_r[1] + min_dec_r[1])/2
        temp.append(ra_g_center)
        temp.append(dec_g_center)
        temp.append(ra_r_center)
        temp.append(dec_r_center)
        all_center_p_collect.append(temp)
        # # print(ra_g_center, dec_g_center, ra_r_center, dec_r_center)
        # center_point_of_image_using_g_center
        center_point.append(ra_g_center)
        center_point.append(dec_g_center)
        center_p_collect.append(center_point)
        # print("Center Point is : ", center_point)

    for i in range(len(g_data)):
        temp_sample = []
        for j in range(len(g_data[i])):
            if g_data[i][j][0] >= all_center_p_collect[i][0]-0.05 and g_data[i][j][0] <= all_center_p_collect[i][0]+0.05 and g_data[i][j][1] >= all_center_p_collect[i][1]-0.05 and g_data[i][j][1] <= all_center_p_collect[i][1]+0.05:
                temp_sample.append(g_data[i][j])
        sample_g.append(temp_sample)
    for i in range(len(r_data)):
        temp_sample = []
        for j in range(len(r_data[i])):
            if r_data[i][j][0] >= all_center_p_collect[i][2]-0.05 and r_data[i][j][0] <= all_center_p_collect[i][2]+0.05 and r_data[i][j][1] >= all_center_p_collect[i][3]-0.05 and r_data[i][j][1] <= all_center_p_collect[i][3]+0.05:
                temp_sample.append(r_data[i][j])
        sample_r.append(temp_sample)
    return sample_g, sample_r, center_p_collect

def find_distance(sample_g, sample_r,num_max_aper):
    D_ra=0.000000000000     #set defualt value Distance of RA
    D_dec=0.000000000000    #set defualt value Distance of Dec
    nearest_dis_ra,box_ra=[],[]
    nearest_dis_dec,box_dec=[],[]
    for i in range(len(sample_g)):
        list_dis = []
        for j in range(len(sample_r)):
            box=[]
            D_ra=float(sample_r[j][0])-float(sample_g[i][0])        # find ra distance 
            D_dec=float(sample_r[j][1])-float(sample_g[i][1])       # find dec distance 
            result = (D_ra**2)+(D_dec**2)                           
            result = math.sqrt(result)                              # Co-ordinate Geometry to find distance between 2 point
            box.append(result)                                      # collect data 
            box.append(D_ra)
            box.append(D_dec)
            list_dis.append(box)
        sorted_list=sorted(list_dis,key=lambda i:i[0])              # Ascending order by distance 2 point
        # use 3 nearest of this G
        # pick up 3 ra in list data ra
        if num_max_aper>len(sample_r):
            num_max_aper=len(sample_r)
        for k in range(num_max_aper):
            box_ra.append(sorted_list[k][1])           
            box_dec.append(sorted_list[k][2])

    # use 3 nearest of each G
    nearest_dis_ra.extend(box_ra)
    nearest_dis_dec.extend(box_dec)
    #send data to find mode in ra and dec 
    ## print("find mode RA :")
    delta_ra=find_mode(nearest_dis_ra)
    ## print("find mode DEC :")
    delta_dec=find_mode(nearest_dis_dec)
    return delta_ra,delta_dec
    
def find_mode(data_list):
    #set size of Frequency distribution table
    n=100
    dis_max=max(data_list)
    ## print("dis_max",dis_max)
    dis_min=min(data_list)
    ## print("dis_min",dis_min)
    #r is range 
    r=dis_max-dis_min
    ## print("r = ",r)
    # I_size is Width of each raw
    I_size=r/n
    ## print("I_size = ",I_size)
    frequency_of_data=[0]*n
    upper_lower_boud=[]
    # make upper lower bound of each raw
    lower=dis_min
    for i in range(n):
        upper=lower+I_size
        upper_lower_boud.append([lower,upper])
        lower=upper
    ## print("upper lower is ",upper_lower_boud)
    # count frequency data one by one
    for i in range(len(data_list)):
        for j in range(n):
            if upper_lower_boud[j][0]<=data_list[i]<=upper_lower_boud[j][1]:
                frequency_of_data[j]+=1
                break
    ## print(frequency_of_data)
    max_frequency=max(frequency_of_data)
    index_f=frequency_of_data.index(max_frequency)
    # set d1 & d2 in condition
    # d1 is distance between frequency of mode and frequeency of before mode
    # d1 is distance between frequency of mode and frequeency of after mode
    if(index_f==0):
        d1=frequency_of_data[index_f]
        d2=frequency_of_data[index_f]-frequency_of_data[index_f+1]
    elif(index_f==n-1):
        d1=frequency_of_data[index_f]-frequency_of_data[index_f-1]
        d2=frequency_of_data[index_f]
    else:
        d1=frequency_of_data[index_f]-frequency_of_data[index_f-1]
        d2=frequency_of_data[index_f]-frequency_of_data[index_f+1]
    Mo=upper_lower_boud[index_f][0]+I_size*(d1)/(d1+d2)
    ## print("Mode is ",Mo)
    #init value defualt
    distance=1000
    closed=-1
    #find nearest between data and mode
    for i in range(len(data_list)):
        if abs(data_list[i]-Mo)<distance:
            closed=i
            distance=abs(data_list[i]-Mo)
    ## print("nearest Mo is ",data_list[closed])
    ## print("distance is ",distance)
    return data_list[closed]

def difference(sample_g, sample_r, IorR):
    
    num_max_aper = 30
    #number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    all_delta_ra_dec = []
    if IorR == "Sample R":
        type_sample=" R "
    else : 
        type_sample=" I "
    for i in range(len(sample_g)):
        text = "The plot shows sample of coordiante in G &" + type_sample + str(number[i])
        plot_sample(sample_g[i], sample_r[i], text, IorR)
        # print(text)
        store_temp=[]
        # # print("***** Enter the Coordinate (RA0 and DEC0) of Sample G",
        #       number[i], "*****")
        # ra0, dec0 = input().split()
        # # print("***** Enter the Coordinate (RA0 and DEC0) of Sample R",
        #       number[i], "*****")
        # ra, dec = input().split()
        # ra, ra0, dec, dec0 = float(ra), float(ra0), float(dec), float(dec0)
        # # find the delta of each RA, DEC
        # # print(ra, ra0, dec, dec0)
        # delta_ra = ra - ra0
        # delta_dec = dec - dec0
        # # print("Delta_RA: ", delta_ra)
        # # print("Delta_DEC: ", delta_dec)
        # # convert to shift constant
        # delta_ra = delta_ra*(-1)
        # delta_dec = delta_dec*(-1)
        # code in line 349 - 364 is old code write by Benz and my code start 366-368 , function find_distance in line 251 , function find_mode in line 285
        # save match data and pick max match data
        for star in range(1,num_max_aper,2):
            ## print("using k = ",star)
            temp = []   
            if type_sample==" R ":
                delta_ra, delta_dec = find_distance(sample_g[i],sample_r[i],star)
                delta_ra = delta_ra*(-1)
                delta_dec = delta_dec*(-1)
            else:
                delta_ra, delta_dec = find_distance(sample_r[i],sample_g[i],star)
            ## print("Delta_RA: ", delta_ra)
            ## print("Delta_DEC: ", delta_dec) 
            new_list_r = [[[0 for i in range(7)] for j in range(
                len(sample_r[i]))] for k in range(len(sample_r))]
            for j in range(len(sample_r[i])):
                # plus shift constant for coordinate ra of sample r
                new_list_r[i][j][0] = new_list_r[i][j][0] + \
                    sample_r[i][j][0] + delta_ra
                # plus shift constant for coordinate dec of sample r
                new_list_r[i][j][1] = new_list_r[i][j][1] + \
                    sample_r[i][j][1] + delta_dec
                new_list_r[i][j][2] = sample_r[i][j][2]
                new_list_r[i][j][3] = sample_r[i][j][3]
                new_list_r[i][j][4] = sample_r[i][j][4]
                new_list_r[i][j][5] += sample_r[i][j][5]
                new_list_r[i][j][6] += sample_r[i][j][6]
            # plot check
            text2 = "The plot shows shifted sample in G &"+ type_sample + str(number[i]) + " using by k nearest point = "+str(star)
            plot_sample(sample_g[i], new_list_r[i], text2 , IorR)

            count = 0
            G, R = [], []
            for j in range(len(sample_g[i])):
                for k in range(len(new_list_r[i])):
                    if math.sqrt((sample_g[i][j][0] - new_list_r[i][k][0])**2 + (sample_g[i][j][1] - new_list_r[i][k][1])**2) <= 0.0009:
                        if new_list_r[i][k] in R:
                            count += 1
                        G.append(sample_g[i][j])
                        R.append(new_list_r[i][k])
            ## print("Length of matched sample is ", len(G))
            ## print("Number of duplicate match sample in each pairs is", count)
            text3 = "The plot shows noise filtered sample in G &" + type_sample + str(number[i]) + " using by k nearest point = "+str(star)
            plot_sample(G, R, text3, IorR)
            ## print("\n")
            temp.append(len(G))
            temp.append(delta_ra)
            temp.append(delta_dec)
            temp.append(star)
            store_temp.append(temp)
        sorted_store_temp=sorted(store_temp,key=lambda i:i[0],reverse=True) # Decending order by count pair
        ## print("use k = ",sorted_store_temp[0][0])
        max_of_pair=[sorted_store_temp[0][1],sorted_store_temp[0][2]]
        print(sorted_store_temp[0][1],sorted_store_temp[0][2],sorted_store_temp[0][0],sorted_store_temp[0][3])
        all_delta_ra_dec.append(max_of_pair)
    return all_delta_ra_dec

def data_shifting(r_data, delta):
     # --------------------------------all data shift section------------------------------------------
    for i in range(len(r_data)):
        for j in range(len(r_data[i])):
            r_data[i][j][0] = r_data[i][j][0] + delta[i][0]
            r_data[i][j][1] = r_data[i][j][1] + delta[i][1]

def data_rotate(g_data, r_data, center_point, theta, IorR):
    # print("*****Rotating Section*****")
    #number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    G, R = [], []
    all_data = []
    if IorR == "Sample R":
        type_sample=" R "
    else : 
        type_sample=" I "
    for i in range(len(r_data)):
        # visualize before rotate
        text = "The plot shows data before rotate in G &"+ type_sample + str(number[i])
        plot_sample(g_data[i], r_data[i], text, IorR)
        # print('Rotating',IorR , number[i])
        # change all points to origin of picture center
        for j in range(len(r_data[i])):
            r_data[i][j][0] -= center_point[i][0]
            r_data[i][j][1] -= center_point[i][1]
            x = r_data[i][j][0]
            y = r_data[i][j][1]
        # convert the cartesian coordinate to polar coordinate (r,theta)
            r_data[i][j][0] = (x ** 2 + y ** 2) ** .5
            r_data[i][j][1] = math.degrees(math.atan2(y, x))
        # change parameter >> Theta <<
            r_data[i][j][1] += theta
            r = r_data[i][j][0]
            t = r_data[i][j][1]
        # convert polar coordinate to cartesian coordination
            r_data[i][j][0] = r*math.cos(math.radians(t))
            r_data[i][j][1] = r*math.sin(math.radians(t))
        # back to original
        for k in range(len(r_data[i])):
            r_data[i][k][0] += center_point[i][0]
            r_data[i][k][1] += center_point[i][1]
        # visualize after rotate the image
        text2 = "The plot shows rotated data in G &"+ type_sample + str(number[i])
        plot_sample(g_data[i], r_data[i], text2, IorR)

        # data filtering for noiseless
        temp_G = []
        temp_R = []
        temp_all = []
        count = 0
        for m in range(len(g_data[i])):
            for n in range(len(r_data[i])):
                if math.sqrt((g_data[i][m][0] - r_data[i][n][0])**2 + (g_data[i][m][1] - r_data[i][n][1])**2) <= 0.00110:
                    if r_data[i][n] in temp_R:
                        count += 1
                    pair = [g_data[i][m],r_data[i][n]]
                    temp_G.append(g_data[i][m])
                    temp_R.append(r_data[i][n])
                    temp_all.append(pair)
        ## print("temp all ****************** = ",temp_all)
        all_data.append(temp_all)
        G.append(temp_G)
        R.append(temp_R)
        ## print("Length of matched data rotation is ", len(G[i]))
        ## print("Number of duplicate match data in each pairs is", count)
        # # print(G[i])
        text3 = "The plot shows filtered data in G &"+ type_sample  + str(number[i])
        plot_sample(G[i], R[i], text3, IorR)
    return all_data

def matching(key, data_G):
    # # print("The number of key is: ",len(key))
    # # print(key)
    # # print(data_G)
    count = 0
    duplicate_check = []
    check = []
    matched_list = []
    for i in range(len(key)):
        for j in range(len(data_G)):
            for k in range(len(data_G[j])): 
                if(abs(key[i][0] - data_G[j][k][0]) <= 0.003 and abs(key[i][1] - data_G[j][k][1]) <= 0.003):
                    temp = []
                    temp1 = []
                    temp.append(float(data_G[j][k][0]))  # RA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                    temp.append(float(data_G[j][k][1]))  # DEC
                    temp.append(float(key[i][0])) #R.A. key
                    temp.append(float(key[i][1])) # Dec. key
                    temp.append(float(data_G[j][k][2]))  # MAG_APER
                    temp.append(data_G[j][k][3])  # filename
                    temp.append(data_G[j][k][4])  # object_number
                    matched_list.append(temp)
                    temp1.append(key[i][0])
                    temp1.append(key[i][1])
                    if(temp1 in duplicate_check):
                        count += 1
                        check.append(temp1)
                    else:
                        duplicate_check.append(temp1)
    # print("Length of key is ", len(key))
    # print("Length of matched list is ", len(matched_list))
    # print("Length of duplicate matched list is ", count)
    # print(check) 
    return matched_list

def matching_GI_GR(GR,GI):
    ## print(" GI data = ",GI)
    ## print(" GR data = ",GR)
    ## print("len first ",len(GI),len(GR))
    ## print("len second ",len(GI[0][0]),len(GR[0][0]))
    storeData = []
    for i in range(len(GR)):
        dataMatched=[]
        for j in range(len(GI[i])):
            for k in range(len(GR[i])):
                temp = []
                if GI[i][j][0]==GR[i][k][0] :
                    temp.append(GI[i][j][1][3])
                    temp.append(GI[i][j][1][4])
                    temp.append(GR[i][k][1][3])
                    temp.append(GR[i][k][1][4])
                    temp.append(GI[i][j][0][3])
                    temp.append(GI[i][j][0][4])
                    dataMatched.append(temp)
                    break
        storeData.append(dataMatched)
    
    return storeData 

# splitter for split datasest in format of 'gX.txt' file only.
def splitter(g_file):
    splited = []
    myfile = open(g_file)
    info = myfile.readlines()
    for text in info:
        if(text[0] != '#'):
            text = text.rstrip('\n')
            text = re.findall(r'\S+', text)
            text.append(g_file)
            splited.append(text)
            myfile.close()
    return splited

def csv_key_export(key_list):
    with open('key_02.csv', 'w', newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        data = [['RA', 'DEC', 'Vmag']]
        a.writerows(data)
        for i in range(len(key_list)):
            data = [[key_list[i][0], key_list[i][1], key_list[i][2]]]
            a.writerows(data)

def csv_export(matched_list):
    print("start write")
    with open('dataGRImatchLast.csv', 'w', newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        data_head = [['NUMBER_I', 'MAG_APER_I', 'MAGERR_APER_I', 'MAG_AUTO_I', 'MAGERR_AUTO_I', 'MAG_BEST_I', 'MAGERR_BEST_I', 'KRON_RADIUS_I', 'BACKGROUND_I', 'THRESHOLD_I', 'ISOAREA_IMAGE_I', 'ISOAREAF_IMAGE_I', 'ALPHAPEAK_J2000_I',
                 'DELTAPEAK_J2000_I', 'X_IMAGE_I', 'Y_IMAGE_I', 'FWHM_IMAGE_I', 'FWHM_WORLD_I', 'ELONGATION_I', 'ELLIPTICITY_I', 'CLASS_STAR_I', 'FLUX_RADIUS_I', 'FILE_NAME_I','NUMBER_R', 'MAG_APER_R', 'MAGERR_APER_R', 'MAG_AUTO_R', 'MAGERR_AUTO_R', 'MAG_BEST_R', 'MAGERR_BEST_R', 'KRON_RADIUS_R', 'BACKGROUND_R', 'THRESHOLD_R', 'ISOAREA_IMAGE_R', 'ISOAREAF_IMAGE_R', 'ALPHAPEAK_J2000_R',
                 'DELTAPEAK_J2000_R', 'X_IMAGE_R', 'Y_IMAGE_R', 'FWHM_IMAGE_R', 'FWHM_WORLD_R', 'ELONGATION_R', 'ELLIPTICITY_R', 'CLASS_STAR_R', 'FLUX_RADIUS_R', 'FILE_NAME_R','NUMBER_G', 'MAG_APER_G', 'MAGERR_APER_G', 'MAG_AUTO_G', 'MAGERR_AUTO_G', 'MAG_BEST_G', 'MAGERR_BEST_G', 'KRON_RADIUS_G', 'BACKGROUND_G', 'THRESHOLD_G', 'ISOAREA_IMAGE_G', 'ISOAREAF_IMAGE_G', 'ALPHAPEAK_J2000_G',
                 'DELTAPEAK_J2000_G', 'X_IMAGE_G', 'Y_IMAGE_G', 'FWHM_IMAGE_G', 'FWHM_WORLD_G', 'ELONGATION_G', 'ELLIPTICITY_G', 'CLASS_STAR_G', 'FLUX_RADIUS_G', 'FILE_NAME_G']]
        a.writerows(data_head)
        for i in range(len(matched_list)):
            m = matched_list[i]
            for j in range(len(m)):
                data = []
                # use splitter function to split data in file name
                I_detail = splitter(m[j][0])
                r_detail = splitter(m[j][2])
                g_detail = splitter(m[j][4])
                # select obj num but use in order list -1 to data 
                data.extend(I_detail[m[j][1]-1])
                data.extend(r_detail[m[j][3]-1])
                data.extend(g_detail[m[j][5]-1])
                a.writerow(data)
    print("END PROCESS")

def histogram(matched_list):
    temp = []
    for i in range(len(matched_list)):
        temp.append(matched_list[i][2])
    plt.hist(temp, bins=20, ec='black')
    plt.title(
        'Histogram show visualization of luminosity function')
    plt.show()

def plot_sample(sample_g, sample_r, text, IorR):
    x_g, y_g, x_r, y_r = [], [], [], []
    for i in range(len(sample_g)):
        x_g.append(sample_g[i][0])
        y_g.append(sample_g[i][1])
    for j in range(len(sample_r)):
        x_r.append(sample_r[j][0])
        y_r.append(sample_r[j][1])
    plt.figure(figsize=(4.3, 10))

    plt.scatter(x_r, y_r, label=IorR, c='white',
                edgecolors='crimson', marker='o', s=5)
    plt.scatter(x_g, y_g, label='Sample G', c='forestgreen', marker='.', s=5)
    plt.title(text)
    plt.xlabel('Alpha', fontsize=12)
    plt.ylabel('Delta', fontsize=12)
    plt.legend(fontsize=12)
    
    #plt.savefig(text+'.png', bbox_inches='tight')
    #plt.show()
    plt.close()

def plot_key_data(matched, key, text):
    x_matched, y_matched, x_key, y_key = [], [], [], []
    for i in range(len(matched)):
        for j in range(len(matched[i])):
            x_matched.append(matched[i][j][0])
            y_matched.append(matched[i][j][1])

    for j in range(len(key)):
        x_key.append(key[j][0])
        y_key.append(key[j][1])
    plt.figure(figsize=(4.3, 10))
    plt.scatter(x_key, y_key, label="Key", c='white',
                edgecolors='orangered', marker='o', s=5)
    plt.scatter(x_matched, y_matched, label='Sample G',
                c='forestgreen', marker='.', s=10)
    plt.title(text)
    
    plt.savefig(text+'.png', bbox_inches='tight')
    #plt.show()
    #plt.close()

if __name__ == "__main__":
    main()
