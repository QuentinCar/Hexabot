#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 09:37:55 2020

@author: porlanax
"""

import cv2
import numpy as np

# Chargement de l'image
img = cv2.imread('neurones-et-dendrites.jpg') 

# Affichage de l'image
cv2.imshow('image', img)  

# Conversion de l'image en niveau de gris
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray', gray)  

# Création de l'élément structurant
element_structurant=np.array([[0,1,0],[1,1,1],[0,1,0]])
element_structurant2=np.uint8(element_structurant)

# Ouverture sur l'image avec l'élément structurant : sélectionne les boules
opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, element_structurant2)

cv2.imshow('opening', opening)  

# Image finale avec seulement les lignes (image - les boules)
finale = gray - opening

cv2.imshow('finale', finale)  



###### APPLICATION SUR IMAGE DE LA GROTTE ######

img_fissure1 = cv2.imread('fissure1.png') 
cv2.imshow('fissure1', img_fissure1) 

img_fissure2 = cv2.imread('fissure2.png') 
cv2.imshow('fissure2', img_fissure2) 

gray_fissure1 = cv2.cvtColor(img_fissure1, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_fissure1', gray_fissure1)  

element_structurant=np.array([[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[1,1,1,1,1,1,1],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0]])
element_structurant2=np.uint8(element_structurant)

opening1 = cv2.morphologyEx(gray_fissure1, cv2.MORPH_OPEN, element_structurant2)

cv2.imshow('opening1', opening1)  

# Image finale avec seulement les lignes (image - les boules)
finale1 = -(gray_fissure1 - opening1)

cv2.imshow('finale1', finale1)  


### TEST 2
img_fissure1 = cv2.imread('fissure1.png') 
gray_fissure1 = cv2.cvtColor(img_fissure1, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_fissure1', gray_fissure1) 

gray_fissure2 = cv2.cvtColor(img_fissure2, cv2.COLOR_BGR2GRAY)


edge_grille= cv2.Canny(img_fissure2,6,150)
edge_tout=cv2.Canny(img_fissure2,9,16)
edge_fissure=edge_tout-edge_grille

cv2.imshow('edge_tout', edge_tout)
cv2.imshow('edge_grille', edge_grille)
cv2.imshow('edge_fissure', edge_fissure)


edges6= cv2.Canny(img_fissure2,6,16)

 
edge_grotte=cv2.Canny(gray_fissure2,20,30)
cv2.imshow('edge_grotte', edge_grotte)

edge_grille2= cv2.Canny(gray_fissure2,6,150)
cv2.imshow('edge grille', edge_grille2)


def traitement_image(image):
    img = cv2.imread(image) 
    edge = cv2.Canny(img,6,16)
    cv2.imshow('contours_fissures', edge)
    return edge

def traitement_image2(image):
    img = cv2.imread(image) 
    edge = cv2.Canny(img,6,16)
    cv2.imshow('contours_fissures', edge)
    return edge


img_fissure2 = cv2.imread('fissure2.png') 
gray_fissure2 = cv2.cvtColor(img_fissure2, cv2.COLOR_BGR2GRAY)
for i in range(len(gray_fissure2[0])):
    for j in range(len(gray_fissure2[1])):
        if gray_fissure2[i,j]>15:
            gray_fissure2[i,j]=254
edge = cv2.Canny(img,6,16) 

def detection_fissure(img):
    a=np.amax(img)
    if a ==255:
        return True
    else :
        return False
    
    
### test supplémentaire
struct_close=np.array([[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]])
closing = cv2.morphologyEx(edge_tout, cv2.MORPH_CLOSE, struct_close)
cv2.imshow("closing",closing)

struct_open=np.array([[1,1,1],[1,1,1],[1,1,1]])
open2 = cv2.morphologyEx(closing, cv2.MORPH_OPEN, struct_open)
cv2.imshow("open2",open2)
