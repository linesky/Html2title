a:int=0
titless=True
scripts=True
triggers=False
filename="my.html"
print("\x1bc\x1b[41;30m")
f1=open(filename,"r")
files=f1.read()
f1.close()
splits=files.split(">")
counter=0
for n in splits:
    tags=n.split("<")
    triggers=False
    counter=0
    if len(tags)==2 and len(tags[0])>0:
        triggers=True
        
    for ta in tags:
        ta=ta.strip()
        if counter==0:
            if len(ta)>0:
               if ta=="title" or ta=="TITLE":
                   titless=False
               if ta=="script" or ta=="SCRIPT":
                   scripts=False
               if not(titless):
                   
                   print(ta,end="")
                   
               if ta=="/title" or ta=="/TITLE":
                   titless=True
               if ta=="/script" or ta=="/SCRIPT":
                   scripts=True
        else:
            varsn=ta.split(" ")
            for varn in varsn:
                varn=varn.strip()
                if len(varn)>0:
                    if ta=="title" or ta=="TITLE":
                        titless=False
                    if ta=="script" or ta=="SCRIPT":
                        scripts=False
                    if not(titless): 
                        print(varn)
                    if ta=="/title" or ta=="/TITLE":
                        titless=True
                    if ta=="/script" or ta=="/SCRIPT":
                        scripts=True
                   

        
        counter+=1
        
    