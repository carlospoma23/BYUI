print('Program to determinate whether to loan money')
print('')
large=int(input('How large is the loan? '))
credit=int(input('How good is your credit history? '))
income=int(input('How high is your income? '))
down_pay=int(input('How large is your down payment? '))
print('')
#conditions

if large>=5:
    if(credit>=7 and income>=7):
        result=True
    elif(credit>=7 or income>=7):
        if(down_pay>=5):
            result=True
        else:
            result=False
    else:
        result=False
else:
    if(credit<4):
        result=False
    elif(income>=7 or down_pay>=7):
        result=True
    elif(income>=4 and down_pay>=4):
        result=False
    else:
        result=False

if(result):
    decision="yes"
else:
    decision="no"
print()

print(f'Decision: {decision}')