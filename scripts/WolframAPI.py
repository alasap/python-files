# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 22:52:01 2019

@author: Austin
*"""
from skimage import io
import wolframalpha
#from urllib.request import urlopen
client=wolframalpha.Client('JH6UR5-5PXRTPHKH9')
#query=str(input('Query: '))
#i=0
#while i<9999:
    #i=i+1
#for i in range(1):
query=str(input('Query:'+'\n'))
images=str(input('Do you want images?'+'\n'))
res=client.query(query)
try:
        output=(res)
        p=output['pod']
        a0=p[0]
        b0=a0['subpod']
        c0=b0['plaintext']
        e0=b0['img']
        f0=e0['@src']
        a1=p[1]
        b1=a1['subpod']
        c1=b1['plaintext']
        e1=b1['img']
        f1=e1['@src']
        a2=p[2]
        b2=a2['subpod']
        c2=b2['plaintext']
        e2=b2['img']
        f2=e2['@src']
        a3=p[3]
        b3=a3['subpod']
        c3=b3['plaintext']
        e3=b3['img']
        f3=e3['@src']
        a4=p[4]
        b4=a4['subpod']
        c4=b4['plaintext']
        e4=b4['img']
        f4=e4['@src']
        a5=p[5]
        b5=a5['subpod']
        c5=b5['plaintext']
        e5=b5['img']
        f5=e5['@src']
        a6=p[6]
        b6=a6['subpod']
        c6=b6['plaintext']
        e6=b6['img']
        f6=e6['@src']
        a7=p[7]
        b7=a7['subpod']
        c7=b7['plaintext']
        e7=b7['img']
        f7=e7['@src']
        t7=str(a7['@title'])
        if str(c7)!=str('None' and '1'):print(c7+'\n')
except:''
try:
        a0=p[0]
        b0=a0['subpod']
        c0=b0['plaintext']
        e0=b0['img']
        f0=e0['@src']
        a1=p[1]
        b1=a1['subpod']
        c1=b1['plaintext']
        e1=b1['img']
        f1=e1['@src']
        a2=p[2]
        b2=a2['subpod']
        c2=b2['plaintext']
        e2=b2['img']
        f2=e2['@src']
        a3=p[3]
        b3=a3['subpod']
        c3=b3['plaintext']
        e3=b3['img']
        f3=e3['@src']
        a4=p[4]
        b4=a4['subpod']
        c4=b4['plaintext']
        e4=b4['img']
        f4=e4['@src']
        a5=p[5]
        b5=a5['subpod']
        c5=b5['plaintext']
        e5=b5['img']
        f5=e5['@src']
        a6=p[6]
        b6=a6['subpod']
        c6=b6['plaintext']
        e6=b6['img']
        f6=e6['@src']
        t6=str(a6['@title'])
        if str(c6)!=str('None' and '1'):print(c6+'\n')
except:''
try:
        a0=p[0]
        b0=a0['subpod']
        c0=b0['plaintext']
        e0=b0['img']
        f0=e0['@src']
        a1=p[1]
        b1=a1['subpod']
        c1=b1['plaintext']
        e1=b1['img']
        f1=e1['@src']
        a2=p[2]
        b2=a2['subpod']
        c2=b2['plaintext']
        e2=b2['img']
        f2=e2['@src']
        a3=p[3]
        b3=a3['subpod']
        c3=b3['plaintext']
        e3=b3['img']
        f3=e3['@src']
        a4=p[4]
        b4=a4['subpod']
        c4=b4['plaintext']
        e4=b4['img']
        f4=e4['@src']
        a5=p[5]
        b5=a5['subpod']
        c5=b5['plaintext']
        e5=b5['img']
        f5=e5['@src']
        t5=str(a5['@title'])
        if str(c5)!=str('None' and '1'): print(c5+'\n')
except:''
try:
        a0=p[0]
        b0=a0['subpod']
        c0=b0['plaintext']
        e0=b0['img']
        f0=e0['@src']
        a1=p[1]
        b1=a1['subpod']
        c1=b1['plaintext']
        e1=b1['img']
        f1=e1['@src']
        a2=p[2]
        b2=a2['subpod']
        c2=b2['plaintext']
        e2=b2['img']
        f2=e2['@src']
        a3=p[3]
        b3=a3['subpod']
        c3=b3['plaintext']
        e3=b3['img']
        f3=e3['@src']
        a4=p[4]
        b4=a4['subpod']
        c4=b4['plaintext']
        e4=b4['img']
        f4=e4['@src']
        t4=str(a4['@title'])
        if str(c4)!=str('None' and '1'):print(c4+'\n')
except:''
try:
        a0=p[0]
        b0=a0['subpod']
        c0=b0['plaintext']
        e0=b0['img']
        f0=e0['@src']
        a1=p[1]
        b1=a1['subpod']
        c1=b1['plaintext']
        e1=b1['img']
        f1=e1['@src']
        a2=p[2]
        b2=a2['subpod']
        c2=b2['plaintext']
        e2=b2['img']
        f2=e2['@src']
        a3=p[3]
        b3=a3['subpod']
        c3=b3['plaintext']
        e3=b3['img']
        f3=e3['@src']
        t3=str(a3['@title'])
        if str(c3)!=str('None' and '1'):print(c3+'\n')
except:''
try:
        a0=p[0]
        b0=a0['subpod']
        c0=b0['plaintext']
        e0=b0['img']
        f0=e0['@src']
        a1=p[1]
        b1=a1['subpod']
        c1=b1['plaintext']
        e1=b1['img']
        f1=e1['@src']
        a2=p[2]
        b2=a2['subpod']
        c2=b2['plaintext']
        e2=b2['img']
        f2=e2['@src']
        t2=str(a2['@title'])
        if str(c2)!=str('None' and '1'):print(c2+'\n')
except:''
try:
        a0=p[0]
        b0=a0['subpod']
        c0=b0['plaintext']
        e0=b0['img']
        f0=e0['@src']
        t0=b0['@title']
        a1=p[1]
        b1=a1['subpod']
        c1=b1['plaintext']
        e1=b1['img']
        f1=e1['@src']
        t1=str(a1['@title'])
        if str(c1)!=str('None' and '1'):print(c1+'\n')
except:''
try:
        a0=p[0]
        b0=a0['subpod']
        c0=b0['plaintext']
        e0=b0['img']
        f0=e0['@src']
        t0=str(a0['@title'])
        if str(c0)!=str('None' and '1'):print(c0+'\n')
except:print('wtf none worked?')
    # import the necessary packages

import cv2

    # METHOD #2: scikit-image

if str('yes' or 'Yes' or 'y' or 'Y')==str(images):
    sc=input('What scaling factor for the figures?(in percent)'+'\n')
    scs=str(sc)
    sci=int(scs)
    scale_percent=(sci)
    try:
            image1 = io.imread(f0)
            image2 = io.imread(f1)
            image3 = io.imread(f2)
            image4 = io.imread(f3)
            image5 = io.imread(f4)
            image6 = io.imread(f5)
            image7 = io.imread(f6)
            image8 = io.imread(f7)
            width = int(image8.shape[1] * scale_percent / 100)
            height = int(image8.shape[0] * scale_percent / 100)
            dim = (width, height)
            resized8 = cv2.resize(image8, dim, interpolation = cv2.INTER_AREA)
            cv2.imshow(t7,cv2.cvtColor(resized8, cv2.COLOR_BGR2RGB))
            cv2.waitKey(0)
    except:''
    try:
            image1 = io.imread(f0)
            image2 = io.imread(f1)
            image3 = io.imread(f2)
            image4 = io.imread(f3)
            image5 = io.imread(f4)
            image6 = io.imread(f5)
            image7 = io.imread(f6)
            width = int(image7.shape[1] * scale_percent / 100)
            height = int(image7.shape[0] * scale_percent / 100)
            dim = (width, height)
            resized7 = cv2.resize(image7, dim, interpolation = cv2.INTER_AREA)
            cv2.imshow(t6,cv2.cvtColor(resized7, cv2.COLOR_BGR2RGB))
            cv2.waitKey(0)
    except:''
    try:
            image1 = io.imread(f0)
            image2 = io.imread(f1)
            image3 = io.imread(f2)
            image4 = io.imread(f3)
            image5 = io.imread(f4)
            image6 = io.imread(f5)
            width = int(image6.shape[1] * scale_percent / 100)
            height = int(image6.shape[0] * scale_percent / 100)
            dim = (width, height)
            resized6 = cv2.resize(image6, dim, interpolation = cv2.INTER_AREA)
            cv2.imshow(t5,cv2.cvtColor(resized6, cv2.COLOR_BGR2RGB))
            cv2.waitKey(0)
    except:''
    try:
            image1 = io.imread(f0)
            image2 = io.imread(f1)
            image3 = io.imread(f2)
            image4 = io.imread(f3)
            image5 = io.imread(f4)
            width = int(image5.shape[1] * scale_percent / 100)
            height = int(image5.shape[0] * scale_percent / 100)
            dim = (width, height)
            resized5 = cv2.resize(image5, dim, interpolation = cv2.INTER_AREA)
            cv2.imshow(t4,cv2.cvtColor(resized5, cv2.COLOR_BGR2RGB))
            cv2.waitKey(0)
    except:''
    try:
        image1 = io.imread(f0)
        image2 = io.imread(f1)
        image3 = io.imread(f2)
        image4 = io.imread(f3)
        width = int(image4.shape[1] * scale_percent / 100)
        height = int(image4.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized4 = cv2.resize(image4, dim, interpolation = cv2.INTER_AREA)
        cv2.imshow(t3,cv2.cvtColor(resized4, cv2.COLOR_BGR2RGB))
        cv2.waitKey(0)
    except:''
    try:
        image1 = io.imread(f0)
        image2 = io.imread(f1)
        image3 = io.imread(f2)
        width = int(image3.shape[1] * scale_percent / 100)
        height = int(image3.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized3 = cv2.resize(image3, dim, interpolation = cv2.INTER_AREA)
        cv2.imshow(t2,cv2.cvtColor(resized3, cv2.COLOR_BGR2RGB))
        cv2.waitKey(0)
    except:''
    try:
        image1 = io.imread(f0)
        image2 = io.imread(f1)
        width = int(image2.shape[1] * scale_percent / 100)
        height = int(image2.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized2 = cv2.resize(image2, dim, interpolation = cv2.INTER_AREA)
        cv2.imshow(t1,cv2.cvtColor(resized2, cv2.COLOR_BGR2RGB))
        cv2.waitKey(1)
    except:''
    try:
        image1 = io.imread(f0)
        width = int(image1.shape[1] * scale_percent / 100)
        height = int(image1.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized1 = cv2.resize(image1, dim, interpolation = cv2.INTER_AREA)
        cv2.imshow(t0,cv2.cvtColor(resized1, cv2.COLOR_BGR2RGB))
        cv2.waitKey(1)
    except:""

