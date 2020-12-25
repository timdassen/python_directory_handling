# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 18:06:11 2019

@author: chris.lynch
"""


import os
import shutil

BASE_FOLDER_NAME = '/p/_CodePS_internal_projects/CRS/99_Projects/CRS1902_my_little_foamy/testing/04_Repeatability'
#FOLDER_NAMES = ['CAFI_H0642_M000_002','REFI_H0010_M1325_001','REFI_H0201_M1760_001','REFI_H0302_M2112_003','REFI_H0500_M1501_007','CAFI_H0528_M000_001','CAFI_H0642_M000_003','REFI_H0010_M1414_001','REFI_H0201_M1934_001','REFI_H0349_M2112_004','REFI_H0555_M1501_008','CAFI_H0528_M000_002','CAFI_H0642_M000_004','REFI_H0201_M1501_001','REFI_H0201_M2112_001','REFI_H0447_M1501_006','REFI_H0642_M1501_009','CAFI_H0642_M000_001','REFI_H0201_M1587_001','REFI_H0249_M2112_002','REFI_H0447_M2112_005']
FOLDER_NAMES = ['REFI_H1133_M0529_004','REFI_H1133_M0529_009','REFI_H1133_M0529_014','REFI_H1133_M0529_035','REFI_H1133_M0529_060','REFI_H1133_M0529_085','REFI_H1133_M0529_000','REFI_H1133_M0529_005','REFI_H1133_M0529_010','REFI_H1133_M0529_015','REFI_H1133_M0529_040','REFI_H1133_M0529_065','REFI_H1133_M0529_090','REFI_H1133_M0529_001','REFI_H1133_M0529_006','REFI_H1133_M0529_011','REFI_H1133_M0529_020','REFI_H1133_M0529_045','REFI_H1133_M0529_070','REFI_H1133_M0529_095','REFI_H1133_M0529_002','REFI_H1133_M0529_007','REFI_H1133_M0529_012','REFI_H1133_M0529_025','REFI_H1133_M0529_050','REFI_H1133_M0529_075','REFI_H1133_M0529_100','REFI_H1133_M0529_003','REFI_H1133_M0529_008','REFI_H1133_M0529_013','REFI_H1133_M0529_030','REFI_H1133_M0529_055','REFI_H1133_M0529_080']
for fold in FOLDER_NAMES:
    files=os.listdir(os.path.join(BASE_FOLDER_NAME,fold))
    images= [x for x in files if x.endswith('.bmp')]
    acc= [x for x in files if x.endswith('.csv')]
    
    if not 'camera' in files and len(images)>0:
#        txt = input("%s: "% (os.path.join(BASE_FOLDER_NAME,fold)) )
#        if txt is 'y'
        os.makedirs(os.path.join(BASE_FOLDER_NAME,fold,'camera'),exist_ok=True) 
        for img in images:
            shutil.move(os.path.join(BASE_FOLDER_NAME,fold,img),os.path.join(BASE_FOLDER_NAME,fold,'camera',img))
        
        if len(acc)>0:
            os.makedirs(os.path.join(BASE_FOLDER_NAME,fold,'accelerometer'),exist_ok=True) 
            for ac in acc:
                shutil.move(os.path.join(BASE_FOLDER_NAME,fold,ac),os.path.join(BASE_FOLDER_NAME,fold,'accelerometer',ac))
                
            