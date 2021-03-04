

from os import listdir
from os.path import isfile, join
import codecs
mypath='.'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
from bs4 import BeautifulSoup

def isgrammar(s):
    
    try:
        a = s.split('-')
        int(a[0])
        return True
    except:
        return False
        
gram = []
for i in onlyfiles:
    if isgrammar(i):
        gram.append(i)
        
        
point = []


def transfo_level(s):
    try:    
        return (s.split('>')[1][6])
    except: 
        return None
        
def transfo_exemple(s):
    if  "<span class=\"kanji\">" in s or  "<br><br>" in s or s=='\n' or s=='    </span><br>\n':
        return None
    text = BeautifulSoup(s).get_text()
    vocab =  BeautifulSoup(s).findAll('span', class_="gloss")
    
    g=[]
    for i in vocab:
        g.append(str(i).replace("<span class=\"rouge\">",'').replace("<span class=\"gloss\" title=\"",'\n').replace("</span>",'').replace("\">",' : ').replace('\t','').replace('\n','').split(' : '))
    if text or g :
        return [text.replace('\t','').replace('\n',''),g]
        
for i in gram:
    s =  codecs.open(i, encoding='utf-8')
    
    lines = s.readlines()
    
    
    for j in range(len(lines)):
        if "JLPT N" in lines[j]:
            level = transfo_level(lines[j])
        
        if "grammaire_nom" in lines[j]:
            nom = ''
            k=1
            while not "/div" in lines[j+k]:
                nom+=(lines[j+k]) 
                k+=1
        
        if "grammaire_description" in lines[j]:
            description = ''
            k=1
            while not "/div" in lines[j+k]:
                description+=lines[j+k]
                k+=1
            
        if "grammaire_construction" in lines[j]:
            construction = ''
            k=1
            while not "/div" in lines[j+k]:
                construction+=(lines[j+k]) 
                k+=1
        
        if "grammaire_exemples" in lines[j]:
            exemples = []

            k=1
            while not "/div" in lines[j+k]:
                o = transfo_exemple(lines[j+k])
                if o :
                    exemples.append(o )

                k+=1
    nom = BeautifulSoup(nom).get_text().replace('\t','').replace('\n','<br>')
    description = BeautifulSoup(description).get_text().replace('\t','').replace('\n','<br>')
    construction = BeautifulSoup(construction).get_text().replace('\t','').replace('\n','<br>')
    
    ex1 = []
    for k in exemples:
        if k!=['',[]]:
            ex1.append(k)
    
    ex  =[]
    for k in range(len(ex1)//2):
        
        ex.append([ex1[2*k][0],ex1[2*k+1][0],ex1[2*k][1]])
    
    pp = dict()
    
    pp['level'] = level
    pp['gram_jp'],pp['gram_fr'] = nom.split(':')
    pp['descr'] = description
    pp['construction'] = construction
    pp['exemple'] = ex
    point.append(pp)


