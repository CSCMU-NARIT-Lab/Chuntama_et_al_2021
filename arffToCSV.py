#coding=utf-8
import pandas as pd

def arff_to_csv(fpath):
    #Read arff data

    nameFile="HierarN6Complete"
    #nameFile="EM"+str(i)
    f = open(fpath+nameFile+'.arff')
    lines = f.readlines()
    content = []
    for l in lines:
        if l[0]!="@" and l[0]!="\n":
            content.append(l)
    datas = []
    for c in content:
        c=c.rstrip("\n")
        cs = c.split(',')
        datas.append(cs)
    list_columns=['ELLIPTICITY_G','FWHM_IMAGE_G','CLASS_STAR_G','MAG_APER_G','ELLIPTICITY_R','FWHM_IMAGE_R','CLASS_STAR_R','ELLIPTICITY_I','FWHM_IMAGE_I','CLASS_STAR_I','DELTA_MAG_G_R','DELTA_MAG_R_I','ALPHAPEAK_J2000_I','DELTAPEAK_J2000_I','Cluster']
    #list_columns=['ELLIPTICITY_G','FWHM_IMAGE_G','CLASS_STAR_G','MAG_APER_G','ELLIPTICITY_R','FWHM_IMAGE_R','CLASS_STAR_R','MAG_APER_R','ELLIPTICITY_I','FWHM_IMAGE_I','CLASS_STAR_I','MAG_APER_I','DELTA_MAG_G_R','DELTA_MAG_R_I','ALPHAPEAK_J2000_I','DELTAPEAK_J2000_I','Cluster']
    #Save the data in a csv file
    df = pd.DataFrame(data=datas,index=None,columns=None)
    filename = fpath +nameFile+ '.csv'
    df=df.drop(df.columns[0], axis=1)
    df.columns = list_columns
    df.to_csv(filename,index=None,columns= list_columns)
    f.close()

arff_to_csv("Clustering\\")

    # #Read arff data Density Loop

    # for i in range(4,8):
    #     nameFile="Density"+str(i)
    #     #nameFile="EM"+str(i)
    #     f = open(fpath+nameFile+".arff")
    #     lines = f.readlines()
    #     content = []
    #     for l in lines:
    #         if l[0]!="@" and l[0]!="\n":
    #             content.append(l)
    #     datas = []
    #     for c in content:
    #         c=c.rstrip("\n")
    #         cs = c.split(',')
    #         datas.append(cs)
    #     list_columns=['ELLIPTICITY_G','FWHM_IMAGE_G','CLASS_STAR_G','MAG_APER_G','ELLIPTICITY_R','FWHM_IMAGE_R','CLASS_STAR_R','ELLIPTICITY_I','FWHM_IMAGE_I','CLASS_STAR_I','DELTA_MAG_G_R','DELTA_MAG_R_I','ALPHAPEAK_J2000_I','DELTAPEAK_J2000_I','Cluster']
    #     #list_columns=['ELLIPTICITY_G','FWHM_IMAGE_G','CLASS_STAR_G','MAG_APER_G','ELLIPTICITY_R','FWHM_IMAGE_R','CLASS_STAR_R','MAG_APER_R','ELLIPTICITY_I','FWHM_IMAGE_I','CLASS_STAR_I','MAG_APER_I','DELTA_MAG_G_R','DELTA_MAG_R_I','ALPHAPEAK_J2000_I','DELTAPEAK_J2000_I','Cluster']
    #     #Save the data in a csv file
    #     df = pd.DataFrame(data=datas,index=None,columns=None)
    #     filename = "Exp5 9 Feb\\" +nameFile+ '.csv'
    #     df=df.drop(df.columns[0], axis=1)
    #     df.columns = list_columns
    #     df.to_csv(filename,index=None,columns= list_columns)
    #     f.close()