#coding:utf-8
import hashlib
import time
import os
filename = 'schedule' #储存当前的破解进度
resultname = 'result' #最终的破解结果
order = 0
print "----------------------------------------"
cipher = input("What is the SHA1 Key?: ")
print"-----------------------------------------"
dic = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#dic = ['0','1','2','3','4','5','6','7','8','9'] #破解时使用的字典，此处为所有的0-9数字组合。上面一行是所有的字母数字组合，根据需要进行注释调整。

def generateText(order): #根据order从dic字典中生成尝试破解的明文
	text = ''
	if order == 0:
		return '0'
	while order != 0:
		text = dic[order % len(dic)] + text
		order /= len(dic)
	return text
def main():
	global order
	if os.path.isfile(filename):
		fp = open(filename,'r+')
		order = fp.readline()
		order = int(order)
		fp.close()
	try:
		run()
	except:
		pass
	finally: #如果程序异常终止，如用户输入了ctrl+c中断，则将当前的破解进度存入"filename"文件中，以便之后从该处重启
		if os.path.isfile(filename):
			os.remove(filename)
		fp = open(filename,'w')
		fp.write(str(order-1))
		fp.close()

def run():
	global order
	found = False
	start = time.time()
	thistime = time.time()
	thisorder = order
	print 'start from %s' %order
	while found == False:
		text = str(order)
		order += 1
		if hashlib.sha1(text).hexdigest() == cipher: #此行为该破解算法的核心，检测明文"text"的SHA1哈希值是否与CIPHER相等
			print text
			print "found!"
			if os.path.isfile(resultname):
				os.remove(resultname)
			fp = open(resultname,'w')
			fp.write(text)
			fp.close()
			found = True
		if time.time() - thistime > 1: 
		        print '[%s items per second] currently trying: %s ' % (((order - thisorder) // (time.time() - thistime)), text)
			thistime = time.time()
			thisorder = order


if __name__ == '__main__':
	main()
