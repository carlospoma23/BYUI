life_file = open("/Users/carlos/Library/CloudStorage/OneDrive-Personal/Carlos Poma/PERFIL PROFESIONAL/BYUIDAHO/vscodebyui1/semester1/ces110/week11/life-expectancy.csv")

input_user=input("Enter the year of interest :")
name_filter=[]
code_filter=[]
life_filter=[]
year_filter=[]
life_temp_list=[]
year_temp_list=[]
name_temp_list=[]
next(life_file)
for line in life_file:
    clean_line=line.strip()
    data_life=clean_line.split(",")
    name_entity=data_life[0]
    code_entity=data_life[1]
    year_data=data_life[2]
    life_exp=data_life[3]

    life_temp_list.append(life_exp)
    year_temp_list.append(year_data)
    name_temp_list.append(name_entity)

    if year_data.lower()==input_user:    
        name_filter.append(name_entity)
        code_filter.append(code_entity)
        life_filter.append(life_exp)
        year_filter.append(year_data)

       
#Lowest life expectancy in tha dataset
min_dataset=min(life_temp_list)
max_dataset=max(life_temp_list)

a=0
b=0
for line in life_temp_list:
    if line==min_dataset:
        index_min_ds=a
    if line==max_dataset:
        index_max_ds=b
    a+=1
    b+=1

print()

print(f'The overal max life expectancy is {max_dataset} from {name_temp_list[index_max_ds]} in {year_temp_list[index_max_ds]}' )
print(f'The overal min life expectancy is {min_dataset} from {name_temp_list[index_min_ds]} in {year_temp_list[index_min_ds]}' )


#Average life expectancy
sum=0
average=None
for i in life_filter:
    sum+=float(i)
average=sum/len(life_filter)

#minimun and maximum life expectancies
max_life=max(life_filter)
min_life=min(life_filter)
x=0
y=0
for line in life_filter:
    
    if line==min_life:
        index_min=x
    if line==max_life:
        index_max=y
    x+=1
    y+=1

print()
print(f'for the year {input_user}.')
print(f'the average life expectancy across all countries was {average:.2f}')
print(f'the max life expectancy was in {name_filter[index_max]} {max_life}')
print(f'the min life expectancy was in  {name_filter[index_min]} {min_life}')

    

life_file.close()