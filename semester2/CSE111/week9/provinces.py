def main():
    
    text_list=read_file("provinces.txt")

    for n in text_list:
        print(n)

    #removing the first element from the list:
    text_list.pop(0)
    #removing the last element from the list:
    text_list.pop(-1)

    print(text_list)

    for n in range(len(text_list)):
        if text_list[n]=="AB":
            text_list[n]="Alberta"
    
    print()
    print('***************************')
    print()

    for n in text_list:
        print(n)

    count=text_list.count("Alberta")

    print()
    print(count)

def read_file(filename):
    list=[]
    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_linea=line.strip()
            list.append(clean_linea)
    return list

if __name__=="__main__":
    main()