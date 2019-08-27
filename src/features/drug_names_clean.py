initial_drug_list = []

with open("drug_names","r") as fid:
    for line in fid:
       initial_drug_list.append(line)

cleaned_drug_list = list(set(initial_drug_list))

with open("cleaned_list","w") as fid:
    for item in cleaned_drug_list:
        fid.write('"' + item.strip() + '" : ""')
        fid.write("\n")