def readfile(filename):
	a = []
	with open(filename,'r',encoding = 'UTF-8-sig') as f:
		for i in f:
			a.append(i.strip())
	return a
def handle(file):
	a_count = 0
	v_count = 0
	a_stic = 0
	a_img = 0
	v_stic = 0
	v_img = 0
	for i in file:
		s = i.split(' ')
		time = s[0]
		name = s[1]			
		if name == 'Allen':
			for j in s[2:]:
				if j == '貼圖' or j == '圖片':
					if j == '貼圖':
						a_stic += 1
					elif j == '圖片':
						a_img += 1
					continue
				a_count = a_count + len(j)
		elif name == 'Viki':
			for j in s[2:]:
				if j == '貼圖' or j == '圖片':
					if j == '貼圖':
						v_stic += 1
					elif j == '圖片':
						v_img += 1
					continue
				v_count = v_count + len(j)	
	print('allen說了:',a_count,'個字','傳了',a_stic,'個貼圖' ,'傳了',a_img,'張圖片' ,'\n','viki說了:',v_count,'個字','傳了',v_stic,'個貼圖' ,'傳了',v_img,'張圖片')

def writefile(filename ,new):
	with open(filename, 'w' ,encoding='utf-8') as f:
		for i in new:
			f.write(i+ '\n')
			 



def main():
	lines = readfile('-LINE-Viki.txt')
	new = handle(lines)
	#writefile('output.txt', new)
	#print(new)
main()