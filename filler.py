import requests
import re
text = input()
url = 'https://www.animefillerlist.com/search/node/'+text
r = requests.get(url, allow_redirects=True)
str = r.content.decode("utf-8")
#print(str)
start = 0
i = 0 
link = []
title = []
while True :
  start = str.find('class="search-result"',start,len(str))
  if(start == -1):
    break
  start = str.find('<a href=',start,len(str))
  end = str.find('>',start,len(str))
  link.append(str[start+9:end-1])
  start = str.find('</a>',start,len(str))
  title.append(str[end:start])
for i in range(0,len(link)):
  print(i+1 ,title[i])
print('select from 1 to ',len(link))
selection = int(input())
if(selection >=len(link)):
  print('invalid selection')
if(selection >=len(link)):
  selection = 1
url = link[selection-1]
r = requests.get(url, allow_redirects=True)
str = r.content.decode("utf-8")
start = str.find('<tbody>', 0,len(str))
end = str.find('</tbody>', 0,len(str))
str2 = str[start:end]
# 0 manga_canon, 1 anime_canon, 2 mixed_canon, 3 filler
anime_list = [29]
#print(str2)
start = str2.find('<tr class="', 0,len(str2))
while True :
  if(str2[start+11:start+13]=='ma'):
    anime_list.append(0)
  elif(str2[start+11:start+13]=='an'):
    anime_list.append(1)
  elif(str2[start+11:start+13]=='mi'):
    anime_list.append(2)
  elif(str2[start+11:start+13]=='fi'):
    anime_list.append(3)
  start = str2.find('<tr class="', start+1 ,len(str2))
  if(start == -1):
    break
#print(anime_list)
print('total episodes count :',len(anime_list)-1)
now = int(input('From where you will count?? '))
anime_ep_count = [0,0,0,0]
i = now
while i < len(anime_list):
  anime_ep_count[anime_list[i]]+=1
  i+=1
print('manga canon remaining :  ',anime_ep_count[0])
print('anime canon remaining :  ',anime_ep_count[1])
print('mixed canon remaining :  ',anime_ep_count[2])
print('fillers canon remaining :  ',anime_ep_count[3])
print('')
print('if you watch manga canon only then you just need to watch ',(anime_ep_count[0]+anime_ep_count[2]),' episodes')
print('if you watch anime & manga canon then you just need to watch ', (anime_ep_count[0]+anime_ep_count[1]+anime_ep_count[2]),' episodes')

9
