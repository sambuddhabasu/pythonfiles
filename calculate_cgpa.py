import re
import mechanize
br = mechanize.Browser()
codes = ['01','02','16','25','30','31','56','64']
grades = ['A','A-','B','B-','C','C-','D','F']
names = []
marks = []
credits = []
global found
for codeCtr in range(0,len(codes)):
	code = codes[codeCtr]
	for gradeCtr in range(0,len(grades)):
		grade = grades[gradeCtr]
		br.open('https://isas.iiit.ac.in/grade/index1.php')
		br.select_form(nr=0)
		br['rno'] = '2013' + str(code)
		br['grade'] = grade
		br.submit()
		findPattern = re.compile('&lt;tr&gt;&lt;td&gt;(.+?)&lt;/td&gt;&lt;/tr&gt;')
		pageData = br.response().readlines()
		findPatPattern = re.findall(findPattern, pageData[9])
		findName = re.compile('2013.+?&lt;/td&gt;&lt;td&gt;(.+?)&lt;/td&gt;')
		for i in range(0,len(findPatPattern)):
			findPatName = re.findall(findName,findPatPattern[i])
			nameCtr = findPatName[0]
			found = 0
			for ctr in range(0,len(names)):
				if(names[ctr]==nameCtr):
					found = 1
					break
			if(found==0):
				names.append(nameCtr)
				marks.append(int(0))
				credits.append(int(0))
			if "Computer  Programming" in findPatPattern[i]:
				marks[names.index(nameCtr)]+=(10-gradeCtr)*5;
				credits[names.index(nameCtr)]+=5;
			if "Mathematics I" in findPatPattern[i]:
				marks[names.index(nameCtr)]+=(10-gradeCtr)*4;
				credits[names.index(nameCtr)]+=4;
			if "Digital Logic and Processors" in findPatPattern[i]:
				marks[names.index(nameCtr)]+=(10-gradeCtr)*5;
				credits[names.index(nameCtr)]+=5;
			if "IT  Workshop" in findPatPattern[i]:
				marks[names.index(nameCtr)]+=(10-gradeCtr)*3;
				credits[names.index(nameCtr)]+=3;
			if "Electrical Science" in findPatPattern[i]:
				marks[names.index(nameCtr)]+=(10-gradeCtr)*2;
				credits[names.index(nameCtr)]+=2;
			if "Creative" in findPatPattern[i]:
				marks[names.index(nameCtr)]+=(10-gradeCtr)*2;
				credits[names.index(nameCtr)]+=2;
			if "Art" in findPatPattern[i]:
				marks[names.index(nameCtr)]+=(10-gradeCtr)*2;
				credits[names.index(nameCtr)]+=2;
			if "General Physics" in findPatPattern[i]:
				marks[names.index(nameCtr)]+=(10-gradeCtr)*4;
				credits[names.index(nameCtr)]+=4;
			if "Introduction to Linguistics" in findPatPattern[i]:
				marks[names.index(nameCtr)]+=(10-gradeCtr)*4;
				credits[names.index(nameCtr)]+=4;
			if "Confluence of Humanities and CS" in findPatPattern[i]:
				marks[names.index(nameCtr)]+=(10-gradeCtr)*4;
				credits[names.index(nameCtr)]+=4;
			if "Sense of Past" in findPatPattern[i]:
				marks[names.index(nameCtr)]+=(10-gradeCtr)*4;
				credits[names.index(nameCtr)]+=4;
			if "Indian Habitat" in findPatPattern[i]:
				marks[names.index(nameCtr)]+=(10-gradeCtr)*4;
				credits[names.index(nameCtr)]+=4;
			if "English" in findPatPattern[i]:
				marks[names.index(nameCtr)]+=(10-gradeCtr)*2;
				credits[names.index(nameCtr)]+=2;
for i in range(0,len(marks)):
	print marks[i]/credits[i], names[i]
