import pandas as pd

usernames = ['Harsh', 'Sid', 'Smit', 'Divyanshu']
passwords = ['Sharma', 'Kannan', 'Choksi', 'Bali']
identity = ['Harsh', 'Sid', 'Smit', 'Bali']

creds = {'user': usernames, 'pass': passwords, 'id':identity}
df = pd.DataFrame(creds)
df.to_csv('TychonCreds.csv')