import os
import json
import cloudant

keys = json.load(open('cloudant.json','rb'))

# connect to your account
USERNAME = keys['cloudant']["username"]
password = keys['cloudant']["password"]
# in this case, https://garbados.cloudant.com

account = cloudant.Account(USERNAME)

# login, so we can make changes
login = account.login(USERNAME, password)
assert login.status_code == 200
db = account.database('lycaeum_forums')

initial_drug_list = []

with open("drug_names","r") as fid:
    for line in fid:
        drug = line[0:-1]
        initial_drug_list.append(drug)

cleaned_drug_list = list(set(initial_drug_list)) #remake drug list
posts_with_no_drugs = 0
# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("forums"):
    path = root.split('/')
    
    full_drug_experience = ""
    for file in files:            
        Title = os.path.basename(root)
        substance_mentioned = []
        cool = "forums/" + os.path.basename(root) + "/" + file
        with open(cool,"r") as fid:
            #print file_experience
            file_experience = fid.read().replace('\n', '')
        for word in file_experience.split():
            if word in cleaned_drug_list :
                if word not in substance_mentioned:
                    substance_mentioned.append(word)
        if len(substance_mentioned) == 0:
            posts_with_no_drugs += 1
        doc = db.document(file[0:-4])
        resp = doc.put(params={
        'posts': file_experience.lower(),#using .lower() because all drug names are lower case
        'discussion_title': Title,
        'substances' : substance_mentioned
        })
print posts_with_no_drugs