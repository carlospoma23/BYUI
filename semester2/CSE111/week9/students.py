import csv

def main():
    number_student=0
    students_dic=read_dictionary("students.csv",number_student)

    i_number=input("Please enter an I-Number (xxxxxxxxx): ")

    if i_number in students_dic:
        value=students_dic[i_number]
        name=value[1]
        print(name)

    else:
        print("No such student")


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dic_students={}
    with open(filename, "rt") as file_students:

        reader=csv.reader(file_students)
        next(reader)
        for row_list in reader:
            key=row_list[key_column_index]
            dic_students[key]=row_list

    return dic_students

if __name__=="__main__":
    main()