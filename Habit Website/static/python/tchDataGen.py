import pandas as pd
import random

allnames = ['Harsh', 'Bali', 'Smit', 'Sid']
alldates = ['6/14/20', '6/15/20', '6/16/20', '6/17/20', '6/18/20', '6/19/20', '6/20/20']
alllocs = ['Bombay', 'Delhi', 'Chennai', 'Hydrabad']
alltypes = ['Food', 'Gas', 'ATM', 'Rest', 'Other']
namelist = []
trucklist = []
datelist = []
loclist = []
typelist = []
amountlist = []

for name in allnames:
	for tnum in range(10):
		for k in range(20):
			namelist.append(name)
			trucklist.append('truck ' + str(tnum+1))
			datelist.append(alldates[random.randint(0,6)])
			loclist.append(alllocs[random.randint(0,3)])
			typelist.append(alltypes[random.randint(0,4)])
			amountlist.append(random.randint(1,500))
datasum = {'name': namelist, 'truck':trucklist, 'date': datelist, 'location': loclist, 'type': typelist, 'amount': amountlist}
df = pd.DataFrame(datasum)
df.to_csv('TychonUsers.csv')