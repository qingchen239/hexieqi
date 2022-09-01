#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re
import random,readJSON

nword = input()

和諧詞 = ''

if nword == "1":
	data = readJSON.读JSON文件("data1.json")
else:
	data = readJSON.读JSON文件("data2.json")

敏感詞 = data["words"]

n粗鄙 = input()
n和諧 = input()

f粗鄙 = open(n粗鄙, "r", encoding = "utf-8")
f和諧 = open(n和諧, "w", encoding = "utf-8")
# 和諧 = open("words.txt", "w", encoding = "utf-8")

lines = f粗鄙.readlines()

s = len(lines)
x = 0


for i in lines:

	x += 1
	print(x / s * 100, "%")

	for j in 敏感詞:
		if "&&" in j:
			if nword == 1:
				tempj = j.split("&&")
			else:
				tempj = j.split("")
			s_tempj = len(tempj)
			x_tempj = 0
			for k in tempj:
				if k in i:
					x_tempj += 1
			# f和諧.write( " \n" )
			# 和諧.write( j + " in " + i )
			# break
			if x_tempj / s_tempj > 0.75:
				for k in tempj:
					i = i.replace(k, 和諧詞 * len(k))
		elif j in i:
			# f和諧.write( " \n" )
			# 和諧.write( j + " in " + i )
			# break
			i = i.replace(j, 和諧詞 * len(j))
	f和諧.write( i )

f粗鄙.close()
f和諧.close()
# 和諧.close()
