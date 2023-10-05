# Chuntama_et_al_2021
Classification_of_Astronomical_Objects_in_the_Galaxy_M81_using_Machine_Learning_Techniques_II._An_Application_of_Clustering_in_Data_Pre-processing-1

Software Version
Weka 3.8.4 

Libary install
- pip install pandas
- pip install -U scikit-learn


1. ทำการ map data g,r,i filter with MatchGRI.py ทั้งข้อมูลชุดที่จะนำไป clustering ก่อนที่จะนำข้อมูลไปจัดกลุ่มเพื่อ classification และข้อมูลกลุ่ม Unseen dataset

2. ทำการเพิ่ม Feature DELTA_MAG_G_R, DELTA_MAG_R_I ใน dataset โดยใช้ EditGRI.py

3. arffToCSV.py คือไฟล์ที่ใช้สำหรับการแปลง ผลการ Clustering ที่เป็นไฟล์นามสกุล .arff แปลงเป็น .csv 

4. CsvToReg.py คือไฟล์ที่ใช้ในการ Convert ไฟล์ที่ได้จาก ข้อ 3 ไปเป็น file .reg เพื่อนำไปใช้ในโปรแกรม SAOImageDS9 (เป็นขั้นตอนการ visualize จัดกลุ่มข้อมูลว่าเป็นวัตถุทางดาราศาสตร์คลาสใด)

5. GroupCluster.py คือไฟล์ที่ใช้ในการ  Group cluster ของกลุ่มวัตถุทางดาราศาสตร์ ที่นักดาราศาสตร์จากสถาบันวิจัยดาราศาสตร์แห่งชาติ(NARIT) เห็นว่ามีความใกล้เคียงกัน

6. CsvToRegEachClass.py คือไฟล์ที่ใช้ในการ Convert ไฟล์ที่ได้จากการทำนาย Unseen data จาก Classification Model ไปเป็น file .reg เพื่อใช้ในการวิเคราะห์ผลจากการทำนาย

7. randomDATAtoModel.py คือไฟล์ที่ใช้ในการแบ่ง train test data

Model ที่ถูก train แล้ว ถูกจัดเก็บอยู่ใน folder model

Source test file => model\test.csv.arff สามารถใช้ .arff เพื่อรันใน weka ได้เลย

หากนำ Code หรือ ข้อมูลไปใช้ กรุณาอ้างอิง paper :  
T. Chuntama, C. Suwannajak, P. Techa-Angkoon, B. Panyangam and N. Tanakul, 
"Classification of Astronomical Objects in the Galaxy M81 using Machine Learning Techniques II. An Application of Clustering in Data Pre-processing," 
2021 18th International Joint Conference on Computer Science and Software Engineering (JCSSE), 
Lampang, Thailand, pp. 1-6, Jul 2021.
