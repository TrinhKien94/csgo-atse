import sys
import os
filename = "Jun 13, 2018-ef9d48124055e16ae95f35e63075d751e12849006c7ab20fd179ce9e8aacd656-0624221624"
f = open(filename,"r")
month = {'Jan' : 1,'Feb' : 2,'Mar' : 3,'Apr' : 4,'May' : 5,'Jun' : 6,'Jul' : 7,'Aug' : 8,'Sep' : 9, 'Oct' : 10,'Nov' : 11,'Dec' : 12}
filenameInfo = filename.split("-")
date = filenameInfo[0]
date = date.replace(',','')
dateInfo = date.split(' ')
monthNum = month[dateInfo[0]]
day = dateInfo[1]
year = dateInfo[2]
content = f.read()
content = content.replace("<div class=\"icon-box\">","")
content = content.replace("<div class=\"coin ","")
content = content.replace("<div class=\"round\">#","")
content = content.replace("- ","")
content = content.replace("</div>","")
content = content.replace("\">","")
content = content.replace("coin-t","1")
content = content.replace("coin-ct","2")
content = content.replace("coin-bonus","0")
content = content.replace("2\n","2 ")
content = content.replace("1\n","1 ")
content = content.replace("0\n","0 ")
content = content.replace("\n\n","\n")
content = content.replace("\n\n","\n")
content = content.replace("\n\n","\n")
content = os.linesep.join([s.strip()+' '+day+' '+str(monthNum)+' '+year+' '+filenameInfo[2] for s in content.splitlines() if s.strip()])
content = content.replace("  "," ")
content = content.replace(" 2 ","2 ")
content = content.replace(" 1 ","1 ")
content = content.replace(" 0 ","0 ")
sys.stdout.write(content)