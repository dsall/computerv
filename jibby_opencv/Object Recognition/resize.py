#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 23:01:56 2018

@author: djibrilsall
"""

import cv2
import numpy as np
import os

img = cv2.imread('ment_1.jpg')
            # should be larger than samples / pos pic (so we can place our image on it)
resized_image = cv2.resize(img, (50, 50))
cv2.imwrite("ment_50_50.jpg",resized_image)
