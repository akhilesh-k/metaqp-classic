import os
import json

data=[]
def recur(cwd,tag):

	ls_elem=os.listdir(cwd)
	for elem in ls_elem:
		if(os.path.isdir(cwd+"/"+elem)):
			tag.append(elem)
			recur(cwd+"/"+elem,tag)
			tag.pop()
		else:
			if(elem[0]!="."):
				if(elem.find("(")!=-1):
					course=elem[:elem.find("(")]
					sem=elem[ elem.find("(",elem.find("(")+1)+1:elem.find(")",elem.find(")")+1) ]
					if(len(sem)!=5):
						sem=-1
					x={}
					if(tag!=[]):
						tag_len=len(tag)
						try:
							if(sem==-1):
								x={"subject":course,"exam":tag[tag_len-2],"sem":"","department":tag[tag_len-1]}
							else:
								x={"subject":course,"exam":tag[tag_len-2],"sem":sem,"department":tag[tag_len-1]}
						except:
							print("FILE ERROR : {}".format(elem))
							print("Tag->{}".format(tag))
					data.append(x)
				

				

def main():
	cwd=os.getcwd()
	tag=[]
	recur(cwd,tag)
	t=json.dumps(data)
	print(t)

main()






# def recur(cwd):

# 	ls_elem=os.listdir(cwd)
# 	for elem in ls_elem:
# 		if(os.path.isfile(elem)):
# 			print (elem)
# 		else:
# 			recur(cwd+"/"+elem)
			