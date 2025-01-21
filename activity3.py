def test( first):
    result={}
    for item in first:
        result= item[ 1 :]
        return result
    
students=[[1, 'Ali Ahmed','V'],[2, 'Raza Khan','VI'],[3, 'James Crooks','VII'],[4, 'Clark Kent','VIII'],[5,'Cornner Kent','XI'],[6,'Sana Jawad','X']]

print("\n Orignal list of lists : ")
print(students)
print('\n Converted lists to a dictionary : ')
print(test(students))