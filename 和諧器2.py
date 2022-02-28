import os, re
import random,readJSON
import time
import opencc

c_s2tw = opencc.OpenCC('s2tw')
c_t2s = opencc.OpenCC('t2s')

eng_letter_B = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
eng_letter_S = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
eng_letter_N = ["1","2","3","4","5","6","7","8","9","0","/",";","'","[","]","\\","1","!","@","#","$","%","^","&","*","(",")","+","{","}","|",":",'"',"<",">","?",",",".","_"]
to_charactor = '　'
to_letter_B = ' '
to_letter_S = ' '
to_letter_N = ' '

n_file1 = input()
n_file2 = input()
replace = int ( input() )
f_file1 = open(n_file1, "r", encoding = "utf-8")
f_file2 = open(n_file2, "w", encoding = "utf-8")
f_file = open("words.txt", "w", encoding = "utf-8")
data = readJSON.读JSON文件("data2.json")

def heXieReplace1(word, line):
	line_copy = line.lower()
	if replace == 1: # 英文、数字、中文
		for letter in word:
			if letter not in eng_letter_S and letter not in eng_letter_N:
				break
			else:
				error_num = 0
				while line_copy.find(word) != -1:
					error_num += 1
					if error_num > 20:
						break
					for i in range(line_copy.find(word), line_copy.find(word) + len(word)):
						line_list = list(line)
						if line_list[i] in eng_letter_B:
							line_list[i] = to_letter_B
						elif line_list[i] in eng_letter_S:
							line_list[i] = to_letter_S
						elif line_list[i] in to_letter_N:
							line_list[i] = to_letter_N
						line = ''.join(line_list)
						line_copy = line.lower()
		for charactor in word:
			if charactor not in eng_letter_B and charactor not in eng_letter_S and charactor not in eng_letter_N:
				line = line.replace(charactor, to_charactor)
	elif replace == 2: # 英文、无数字、中文
		for letter in word:
			if letter not in eng_letter_S and letter not in eng_letter_N:
				break
			else:
				error_num = 0
				while line_copy.find(word) != -1:
					error_num += 1
					if error_num > 20:
						break
					for i in range(line_copy.find(word), line_copy.find(word) + len(word)):
						line_list = list(line)
						if line_list[i] in eng_letter_B:
							line_list[i] = to_letter_B
						elif line_list[i] in eng_letter_S:
							line_list[i] = to_letter_S
						line = ''.join(line_list)
						line_copy = line.lower()
		for charactor in word:
			if charactor not in eng_letter_B and charactor not in eng_letter_S and charactor not in eng_letter_N:
				line = line.replace(charactor, to_charactor)
	elif replace == 3: # 无英文、无数字、中文
		for charactor in word:
			if charactor not in eng_letter_B and charactor not in eng_letter_S and charactor not in eng_letter_N:
				line = line.replace(charactor, to_charactor)
	return line

def heXieReplace2(word, line):
	if replace == 1: # 英文、数字、中文
		for charactor in word:
			if  charactor in eng_letter_S:
				line = line.replace(charactor.upper(), to_letter_B)
				line = line.replace(charactor, to_letter_S)
			elif charactor in eng_letter_N:
				line = line.replace(charactor, to_letter_N)
			else:
				line = line.replace(charactor, to_charactor)
	elif replace == 2: # 英文、无数字、中文
		for charactor in word:
			if  charactor in eng_letter_S:
				line = line.replace(charactor.upper(), to_letter_B)
				line = line.replace(charactor, to_letter_S)
			elif charactor in eng_letter_N:
				pass
			else:
				line = line.replace(charactor, to_charactor)
	elif replace == 3: # 无英文、无数字、中文
		for charactor in word:
			if charactor in eng_letter_S:
				pass
			elif charactor in eng_letter_N:
				pass
			else:
				line = line.replace(charactor, to_charactor)
	return line

def heXie1(line, line_copy, words_type):
# 简单脏话，一词连着出现
	words1 = data[words_type]
	for word1 in words1:
		if word1 in line_copy:
			f_file.write( word1 + " in " + line_copy)
			for charactor in word1:
				line = heXieReplace1(word1, line)
	return line

def heXie2(line, line_copy, words_type):
# 政治黄色暴恐相关，十字之八便被和谐
	words2 = data[words_type]
	for word2 in words2:
		word2_splited = list(set(list(word2)))
		rate = 0
		word2_splited_len = len(word2_splited)
		for charactor in word2_splited:
			if charactor in line_copy:
				rate += 1
		if rate / word2_splited_len >= 0.7777 or rate >= 7:
			f_file.write(str( rate / word2_splited_len * 100 ) + "% " + word2 + " in " + line_copy)
			for charactor in word2_splited:
				line = heXieReplace2(word2_splited, line)
	return line

file1_lines = f_file1.readlines()
file1_len = len(file1_lines)
read_lines = 0
t = int(time.time())
t_0 = t

for line in file1_lines:
	read_lines += 1
	if t != int(time.time()):
		t = int(time.time())
		print(format(read_lines / file1_len * 100, '.2f'), "% completed. The task will be completed in", int ( (t - t_0) / read_lines * (file1_len - read_lines) ), "second(s).")
	
	#if read_lines % 4 == 3:
	#	pass
	
	line_copy = line.lower()
	
	#line = c_s2tw.convert(line)
	#line_copy = c_s2tw.convert(line_copy)
	
	#line = c_t2s.convert(line)
	#line_copy = c_t2s.convert(line_copy)
	
	line = heXie1(line, line_copy, "粗鄙之语")
	line = heXie2(line, line_copy, "政治相关")
	line = heXie2(line, line_copy, "黄赌毒暴相关")
	line = heXie1(line, line_copy, "广告相关")
	line = heXie2(line, line_copy, "202105")
	line = heXie2(line, line_copy, "202106")
	line = heXie2(line, line_copy, "202107")
	line = heXie2(line, line_copy, "202108")
	line = heXie2(line, line_copy, "202109")
	line = heXie2(line, line_copy, "202110")
	line = heXie2(line, line_copy, "202111")
	line = heXie2(line, line_copy, "202112")
	line = heXie2(line, line_copy, "202201")
	line = heXie2(line, line_copy, "202202")
	#line = heXie2(line, line_copy, "202203")
	line = heXie1(line, line_copy, "英文粗鄙之语")
	line = heXie1(line, line_copy, "英文政治相关")
	#line = heXie1(line, line_copy, "英文广告相关")
	
	f_file2.write( line )


f_file1.close()
f_file2.close()
f_file.close()
input("Okay. ")
