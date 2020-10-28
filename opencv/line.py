#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-10-28 19:37:50
# Author : zijing (zijing412@163.com)
###################################################
import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

green = (0, 255, 0)
red = (0, 0, 255)

cv2.line(canvas, (0, 0), (300, 300), green)
cv2.line(canvas, (300, 0), (0, 300), red, 3)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
