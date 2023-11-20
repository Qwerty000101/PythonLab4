#!/usr/bin/env python3
# -*- coding: utf-8 -*-
h = int(input("Количество часов: "))
m = int(input("Количество минут: "))
s = int(input("Количество секунд: "))
sum = h*3600 + m*60 + s
print("Угол равен %.3f градуса(ов)"%(abs(sum/120 - 360*round(sum/(360*120)))))