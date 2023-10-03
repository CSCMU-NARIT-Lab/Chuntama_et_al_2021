import pandas as pd
import os
import csv
import numpy as np
def main():
    gri_data = pd.read_csv('dataGRImatchLast.csv',header=0)
    #Version1
    # gri_data = gri_data.drop(columns=['NUMBER_I','NUMBER_R','NUMBER_G'])
    # gri_data = gri_data.drop(columns=['X_IMAGE_I','Y_IMAGE_I','X_IMAGE_R','Y_IMAGE_R','X_IMAGE_G','Y_IMAGE_G'])
    # gri_data = gri_data.drop(columns=['FILE_NAME_I','FILE_NAME_R','FILE_NAME_G'])
    # gri_data = gri_data.drop(columns=['MAG_BEST_I','MAG_BEST_R','MAG_BEST_G'])
    # gri_data = gri_data.drop(columns=['THRESHOLD_I','THRESHOLD_R','THRESHOLD_G'])
    # gri_data = gri_data.drop(columns=['MAGERR_APER_I','MAGERR_APER_R','MAGERR_APER_G','MAGERR_AUTO_I','MAGERR_AUTO_R','MAGERR_AUTO_G','MAGERR_BEST_I','MAGERR_BEST_R','MAGERR_BEST_G'])
    # gri_data = gri_data.drop(columns=['ISOAREA_IMAGE_I','ISOAREA_IMAGE_R','ISOAREA_IMAGE_G'])
    # gri_data = gri_data.drop(columns=['FWHM_WORLD_I','FWHM_WORLD_R','FWHM_WORLD_G'])
    # # gri_data = gri_data.drop(columns=['ALPHAPEAK_J2000_I','ALPHAPEAK_J2000_R','ALPHAPEAK_J2000_G'])
    # # gri_data = gri_data.drop(columns=['DELTAPEAK_J2000_I','DELTAPEAK_J2000_R','DELTAPEAK_J2000_G'])
    # gri_data = gri_data.drop(columns=['ALPHAPEAK_J2000_R','ALPHAPEAK_J2000_G'])
    # gri_data = gri_data.drop(columns=['DELTAPEAK_J2000_R','DELTAPEAK_J2000_G'])
    # gri_data["DIFFERENT_MAG_I"]=gri_data['MAG_AUTO_I']-gri_data['MAG_APER_I']
    # gri_data["DIFFERENT_MAG_R"]=gri_data['MAG_AUTO_R']-gri_data['MAG_APER_R']
    # gri_data["DIFFERENT_MAG_G"]=gri_data['MAG_AUTO_G']-gri_data['MAG_APER_G']
    # gri_data["DELTA_MAG_G_R"]=gri_data['MAG_APER_G']-gri_data['MAG_APER_R']
    # gri_data["DELTA_MAG_G_I"]=gri_data['MAG_APER_G']-gri_data['MAG_APER_I']
    # gri_data["DELTA_MAG_I_R"]=gri_data['MAG_APER_I']-gri_data['MAG_APER_R']
    # gri_data.to_csv("dataGRI1_ToClusteringVer1.csv.csv",index = False)


    #Version2
    # gri_data["DELTA_MAG_G_R"]=gri_data['MAG_APER_G']-gri_data['MAG_APER_R']
    # gri_data["DELTA_MAG_R_I"]=gri_data['MAG_APER_R']-gri_data['MAG_APER_I']
    # gri_data = gri_data.drop(columns=['MAG_APER_I','MAG_APER_R'])
    # new = gri_data.filter(['ELLIPTICITY_G','FWHM_IMAGE_G','CLASS_STAR_G','MAG_APER_G','DELTA_MAG_G_R','DELTA_MAG_R_I','ALPHAPEAK_J2000_I','DELTAPEAK_J2000_I'], axis=1)
    # new.to_csv("dataGRI1_ToClusteringVer2.csv",index = False)


    # #Version3
    # gri_data["DELTA_MAG_G_R"]=gri_data['MAG_APER_G']-gri_data['MAG_APER_R']
    # gri_data["DELTA_MAG_R_I"]=gri_data['MAG_APER_R']-gri_data['MAG_APER_I']
    # gri_data = gri_data[gri_data.FWHM_IMAGE_G >= 4.51]
    # gri_data = gri_data[gri_data.FWHM_IMAGE_R >= 4.015]
    # gri_data = gri_data[gri_data.FWHM_IMAGE_I >= 3.16]
    # gri_data = gri_data[gri_data.FWHM_IMAGE_G <=100]
    # gri_data = gri_data[gri_data.FWHM_IMAGE_R <=100]
    # gri_data = gri_data[gri_data.FWHM_IMAGE_I <=100]
    # new = gri_data.filter(['ELLIPTICITY_G','FWHM_IMAGE_G','CLASS_STAR_G','MAG_APER_G','ELLIPTICITY_R','FWHM_IMAGE_R','CLASS_STAR_R','MAG_APER_R','ELLIPTICITY_I','FWHM_IMAGE_I','CLASS_STAR_I','MAG_APER_I','DELTA_MAG_G_R','DELTA_MAG_R_I','ALPHAPEAK_J2000_I','DELTAPEAK_J2000_I'], axis=1)
    # new.to_csv("dataGRI1_ToClusteringVer3.csv",index = False)

    #Version4
    # gri_data["DELTA_MAG_G_R"]=gri_data['MAG_APER_G']-gri_data['MAG_APER_R']
    # gri_data["DELTA_MAG_R_I"]=gri_data['MAG_APER_R']-gri_data['MAG_APER_I']
    # gri_data = gri_data[gri_data.FWHM_IMAGE_G >= 4.51]
    # gri_data = gri_data[gri_data.FWHM_IMAGE_R >= 4.015]
    # gri_data = gri_data[gri_data.FWHM_IMAGE_I >= 3.16]
    # gri_data = gri_data[gri_data.FWHM_IMAGE_I <=100]
    # gri_data = gri_data.drop(columns=['MAG_APER_I','MAG_APER_R'])
    # new = gri_data.filter(['ELLIPTICITY_G','FWHM_IMAGE_G','CLASS_STAR_G','MAG_APER_G','ELLIPTICITY_R','FWHM_IMAGE_R','CLASS_STAR_R','ELLIPTICITY_I','FWHM_IMAGE_I','CLASS_STAR_I','DELTA_MAG_G_R','DELTA_MAG_R_I','ALPHAPEAK_J2000_I','DELTAPEAK_J2000_I'], axis=1)
    # new.to_csv("dataGRI1_ToClusteringVer4.csv",index = False)

    # #Version5 the last version to prepare train test Data Set
    gri_data["DELTA_MAG_G_R"]=gri_data['MAG_APER_G']-gri_data['MAG_APER_R']
    gri_data["DELTA_MAG_R_I"]=gri_data['MAG_APER_R']-gri_data['MAG_APER_I']
    gri_data = gri_data[gri_data.FWHM_IMAGE_G >= 4.51]
    gri_data = gri_data[gri_data.FWHM_IMAGE_R >= 4.015]
    gri_data = gri_data[gri_data.FWHM_IMAGE_I >= 3.16]
    gri_data = gri_data[gri_data.FWHM_IMAGE_G <=100]
    gri_data = gri_data[gri_data.FWHM_IMAGE_R <=100]
    gri_data = gri_data[gri_data.FWHM_IMAGE_I <=100]
    new = gri_data.filter(['ELLIPTICITY_G','FWHM_IMAGE_G','CLASS_STAR_G','MAG_APER_G','ELLIPTICITY_R','FWHM_IMAGE_R','CLASS_STAR_R','MAG_APER_R','ELLIPTICITY_I','FWHM_IMAGE_I','CLASS_STAR_I','MAG_APER_I','DELTA_MAG_G_R','DELTA_MAG_R_I','ALPHAPEAK_J2000_I','DELTAPEAK_J2000_I'], axis=1)
    new.to_csv("dataGRILast_ToClusteringVer5.csv",index = False)

    #Unseen with file name
    # list_choice= ['g1','g2','g3','g4','g5','g6']
    # gri_data = pd.read_csv('unseen EXP3\\dataGRImatchUnseenDataset2.csv',header=0)
    # gri_data["DELTA_MAG_G_R"]=gri_data['MAG_APER_G']-gri_data['MAG_APER_R']
    # gri_data["DELTA_MAG_R_I"]=gri_data['MAG_APER_R']-gri_data['MAG_APER_I']
    # gri_data = gri_data[gri_data.FWHM_IMAGE_G >= 4.51]
    # gri_data = gri_data[gri_data.FWHM_IMAGE_R >= 4.015]
    # gri_data = gri_data[gri_data.FWHM_IMAGE_I >= 3.16]
    # gri_data = gri_data[gri_data.FWHM_IMAGE_G <=100]
    # gri_data = gri_data[gri_data.FWHM_IMAGE_R <=100]
    # gri_data = gri_data[gri_data.FWHM_IMAGE_I <=100]
    # new = gri_data.filter(['ELLIPTICITY_G','FWHM_IMAGE_G','CLASS_STAR_G','MAG_APER_G','ELLIPTICITY_R','FWHM_IMAGE_R','CLASS_STAR_R','MAG_APER_R','ELLIPTICITY_I','FWHM_IMAGE_I','CLASS_STAR_I','MAG_APER_I','DELTA_MAG_G_R','DELTA_MAG_R_I','ALPHAPEAK_J2000_I','DELTAPEAK_J2000_I','FILE_NAME_I'], axis=1)
    # new["Cluster"]=np.random.choice(list_choice, size=len(new))
    # new.to_csv("unseen EXP3\\UnseenDataFilename2.csv",index = False)
    
    return 0

if __name__ == "__main__":
    main()