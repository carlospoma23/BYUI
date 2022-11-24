with open("/Users/carlos/Library/CloudStorage/OneDrive-Personal/Carlos Poma/PERFIL PROFESIONAL/BYUIDAHO/vscodebyui1/semester1/ces110/week11/hr_system.txt") as hr_file:
    for line in hr_file:
        line=line.strip()
        employe=line.split(" ")
        name=employe[0]
        id=employe[1]
        profesion=employe[2]
        salary=float(employe[3])/24
        
        if profesion.lower()=="engineer":
            salary_final=salary+1000
        else:
            salary_final=salary
        print(f'{name} (ID: {id} ), {profesion} - {salary_final:.2f}')
