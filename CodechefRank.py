from bs4 import BeautifulSoup
import requests


print("\t \t \t \t \t \t \t \t \t \t \t WELCOME TO CODECHEF ...!!!!")
url = "https://www.codechef.com/users/"
user1 = input('Enter Codechef username of first person : ')
user2 = input('Enter Codechef username of second person : ')

user1url = url+user1
user2url = url+user2

    # Extracting information for user1

source1 = requests.get(user1url)
soup1 = BeautifulSoup(source1.content,"html.parser")  # content or text anything can be used

user1ranks = []
user1dict = {}
data = soup1.find_all("table",{"class":"rating-table"})
try:                                                         # To handle exception if content is not found in <tr> tag
	alltr = data[0].find_all('tr')
	for i in range(1,len(alltr)):
		for j in alltr[i].contents:
			if(j != '\n'):
				user1ranks.append(j.text)
	temp =''
	r=0		
	for k in range(len(user1ranks)):
		if(k==0):
			temp = 'Long'
			r+=1
			user1dict[temp]={}
		elif(k==3):
			temp = 'Short'
			r+=1
			user1dict[temp]={}
		elif(k==6):
			temp = 'LunchTime'
			r+=1
			user1dict[temp]={}	
		else:
			l = user1ranks[k].split('/')
			for t in l:
				if '?' in t:
					p = t.split(".")
					user1dict[temp]['Rank'+str(r)] = p[0]
				else:
					user1dict[temp]['Rank'+str(r)] = t
					r+=1	
except:
	pass
    # Extracting information for user2

source2 = requests.get(user2url)
soup2 = BeautifulSoup(source2.content,"html.parser")

user2ranks = []
user2dict = {}
data = soup2.find_all("table",{"class":"rating-table"})
try:                                                     # To handle exception if content is not found in <tr> tag
	alltr = data[0].find_all('tr')
	for i in range(1,len(alltr)):
		for j in alltr[i].contents:
			if(j != '\n'):
				user2ranks.append(j.text)
	temp =''
	r=0		
	for k in range(len(user2ranks)):
		if(k==0):
			temp = 'Long'
			r+=1
			user2dict[temp]={}
		elif(k==3):
			temp = 'Short'
			r+=1
			user2dict[temp]={}
		elif(k==6):
			temp = 'LunchTime'
			r+=1
			user2dict[temp]={}	
		else:
			l = user2ranks[k].split('/')
			for t in l:
				if '?' in t:
					p = t.split(".")
					user2dict[temp]['Rank'+str(r)] = p[0]
				else:
					user2dict[temp]['Rank'+str(r)] = t
					r+=1   
except:
	pass					
print()
print()
try: # if content is not found then dictionary will not create
	print('\t {0} :'.format(user1))
	print("\t \t \t \t \t \t GLOBAL RANK \t \t \t INDIAN RANK \t \t \t RATING")
	print('\t \t \t LONG: \t \t \t \t {0} \t \t \t {1} \t \t \t \t {2}'.format(user1dict['Long']['Rank1'],user1dict['Long']['Rank2'],user1dict['Long']['Rank3']))
	print('\t \t \t SHORT: \t \t \t {0} \t \t \t {1} \t \t \t \t {2}'.format(user1dict['Short']['Rank4'],user1dict['Short']['Rank5'],user1dict['Short']['Rank6']))
	print('\t \t \t LUNCH_TIME: \t \t \t {0} \t \t \t {1} \t \t \t \t {2}'.format(user1dict['LunchTime']['Rank7'],user1dict['LunchTime']['Rank8'],user1dict['LunchTime']['Rank9']))
except:
	pass

print()
print()
try: # if content is not found then dictionary will not create
	print('\t {0} :'.format(user2))
	print("\t \t \t \t \t \t GLOBAL RANK \t \t \t INDIAN RANK \t \t \t RATING")
	print('\t \t \t LONG: \t \t \t \t {0} \t \t \t {1} \t \t \t \t {2}'.format(user2dict['Long']['Rank1'],user2dict['Long']['Rank2'],user2dict['Long']['Rank3']))
	print('\t \t \t SHORT: \t \t \t {0} \t \t \t {1} \t \t \t \t {2}'.format(user2dict['Short']['Rank4'],user2dict['Short']['Rank5'],user2dict['Short']['Rank6']))
	print('\t \t \t LUNCH_TIME: \t \t \t {0} \t \t \t {1} \t \t \t \t {2}'.format(user2dict['LunchTime']['Rank7'],user2dict['LunchTime']['Rank8'],user2dict['LunchTime']['Rank9']))
except:
	pass