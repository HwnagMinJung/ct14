import requests
r = requests.get('https://www.vox.com/2018/9/25/17901082/trump-un-2018-speech-full-text')
r.encoding = 'utf8'
data=str(r.text)
begin=data.find('Madam President')
end=data.rfind('Thank you very much. Thank you. (Applause.)')
end=end+len('Thank you very much.Thank you. (Applause.)')
d=data[begin:end]
d=d.upper()
d=d.replace('</P>','')
d=d.replace("’",'')
d=d.replace('>','')
d=d.replace('<','')
d=d.replace("'",'')
d=d.replace('''"''','')
d=d.replace('-','')
d=d.replace('{','')
d=d.replace("}",'')
d=d.replace("(",'')
d=d.replace(")",'')
d=d.replace('$','')
d=d.replace('<P','')
d=d.replace('-','')
d=d.replace('/','')

k=d.split()
mydict={}
for w in k:
    if w in mydict:
        mydict[w]+=1
    else:
        mydict[w]=1

for k in sorted(mydict, key=mydict.__getitem__, reverse=True):
    if mydict[k]>=24:
        print(k, mydict[k])
