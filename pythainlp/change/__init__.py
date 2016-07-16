# เขียนโดย วรรณพงษ์  ภัททิยไพบูลย์
# เขียนโดย วรรณพงษ์  ภัททิยไพบูลย์
from __future__ import absolute_import
from __future__ import print_function
dictdata={'Z':'(','z':'ผ','X':')','x':'ป','C':'ฉ','c':'แ','V':'ฮ','v':'อ','B':'ฺ','b':'ิ','N':'์','n':'ื','M':'?','m':'ท','<':'ฒ',',':'ม','>':'ฬ','.':'ใ','?':'ฦ','/':'ฝ',
'A':'ฤ','a':'ฟ','S':'ฆ','s':'ห','D':'ฏ','d':'ก','F':'โ','f':'ด','G':'ฌ','g':'เ','H':'็','h':'้','J':'๋','j':'j','K':'ษ','k':'า','L':'ศ','l':'ส',':':'ซ','"':'.',"'":"ง",':':'ซ',';':'ว',
'Q':'๐','q':'ๆ','W':'"','w':'ไ','E':'ฎ','e':'ำ','R':'ฑ','r':'พ','T':'ธ','t':'ะ','Y':'ํ','y':'ั','U':'๊','u':'ี','I':'ณ','i':'ร','O':'ฯ','o':'น','P':'ญ','p':'ย','{':'ฐ','[':'บ','}':',',']':'ล','|':'ฅ',']':'ฃ',
'~':'%','`':'_','@':'๑','2':'/','#':'๒','3':'-','$':'๓','4':'ภ','%':'๔','5':'ถ','^':'ู','6':'ุ','&':'฿','7':'ึ','*':'๕','8':'ค','(':'๖','9':'ต',')':'๗','0':'จ','_':'๘','-':'ข','+':'๙','=':'ช'}

def texttothai(data):
	data = list(data)
	data2 = ""
	for a in data:
		try:
			a = dictdata[a]
		except:
			a = a
		data2+=a
	return data2
def texttoeng(data):
	data = list(data)
	data2 = ""
	dictdataeng= {v: k for k, v in dictdata.items()}
	for a in data:
		try:
			a = dictdataeng[a]
		except:
			a = a
		data2+=a
	return data2
if __name__ == "__main__":
	a="l;ylfu8iy["
	a=texttothai(a)
	a=texttothai(a)
	b="นามรสนอำันี"
	b=texttoeng(b)
	print(a)
	print(b)