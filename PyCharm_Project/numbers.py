#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("Введите четыре числа:")
first_number = float(input("Первое число: "))
second_number = float(input("Второе число: "))
third_number = float(input("Третье число: "))
fourth_number = float(input("Четвёртое число: "))
first_sum = first_number + second_number
second_sum = third_number + fourth_number
answer = first_sum/second_sum
print("Ответ: %.2f" %(answer))