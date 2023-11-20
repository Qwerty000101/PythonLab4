#!/usr/bin/env python3
# -*- coding: utf-8 -*-
height = int(input("Введите длину первого ребра параллелепипеда: "))
first_width = int(input("Введите длину второго ребра параллелепипеда: "))
second_width = int(input("Введите длину третьего ребра параллелепипеда: "))
first_edge = height*first_width
second_edge = height*second_width
area = 2*(first_edge + second_edge)
volume = height*first_width*second_width
print("Площадь боковой поверхности параллелепипеда:\
%d\nОбъём параллелепипеда равен: %d "%(area,volume))