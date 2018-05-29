#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 00:14:12 2018

@author: djibrilsall
"""

import numpy as np

import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')


img = cv.imread('ibou.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)