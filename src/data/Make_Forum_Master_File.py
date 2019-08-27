import os
#Write a Master File
Master_File = open("Master_File_Forums.txt","a") 
# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("forums"):
    path = root.split('/')
        
    full_drug_experience = ""
    for file in files:
        cool = "forums/" + os.path.basename(root) + "/" + file
        with open(cool,"r") as fid:
            file_experience = fid.read().replace('\n', '')
            #Remove some unnecessary punctuation. Also fixes some poor spelling
            file_experience = file_experience.replace('.', ' ')
            file_experience = file_experience.replace('?', ' ')
            file_experience = file_experience.replace('!', ' ')
            file_experience = file_experience.replace(';', ' ')
            file_experience = file_experience.replace(':', ' ')
            
            full_drug_experience += file_experience
            full_drug_experience += " " #add spacing

    Master_File.write(full_drug_experience)
    Master_File.write("\n")
    
Master_File.close()

#Use made Master File to create dictionary


    
    
    
    
