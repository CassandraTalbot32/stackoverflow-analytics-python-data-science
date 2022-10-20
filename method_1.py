import csv

# Open file and read using csv library
with open ('panda_data/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)

    yes_count = 0
    no_count = 0

# Iterate over lines in csv to categorise  
    for line in csv_reader:
        if line['Hobbyist'] == 'Yes':
            yes_count += 1
        elif line['Hobbyist'] == 'No':
            no_count += 1

total = yes_count + no_count

# Output percenbtages of yes and no
yes_pct = (yes_count / total) * 100
yes_pct = round(yes_pct, 2)

no_pct = (no_count / total) * 100
no_pct = round(no_pct, 2)

# Print results
print(f'Yes: {yes_pct}%')
print(f'No: {no_pct}%')


        

