from random import *
def prov(point,slogn,penalty):#кол-во кубиков и сложность. Сделать необязательный аргумент Штраф.'
    success=0#набранные успехи
    fail=0#набранные провалы
    a=0#значение кубика
    if(penalty == '!' or penalty>=point):
        print("Штраф ревосходит кол-во кубиков")
        return '0'
    for i in range(point-penalty):
        a=randint(1,10)
        if(a>=slogn):
            success+=1
        elif(a==1):
            fail+=1
        print(a)
    if(success>=1 and success>fail):
        return '+'*(success-fail)
    elif(success==0 and fail>=1):
        return '-'
    else:
        return '0' 

#
#Броски, где провал невозможен
#
def no_fail_prov(point,slogn,penalty):
    success=0#набранные успехи
    a=0#значение кубика
    if(penalty>=point):
        print("Штраф ревосходит кол-во кубиков")
        return 0
    for i in range(point-penalty):
        a=randint(1,10)
        if(a>=slogn):
            success+=1
    return success

#
#Множественное действие
#
def c_prov(point,slogn,penalty,time,c_slogn):
    seccess = 0
    for i in range(time):
        a=prov(point,slogn,penalty)
        if(a=='-'):
            print("ПРОВАЛ")
            return '-'
        elif(a!='-' and a!='0'):
            seccess+=len(a)
            if(seccess>=c_slogn):
                print("Длительное действите успешно выполнено за",i,"ходов")
                return seccess-c_slogn
    print("Длительное действие не выполнено за данный промежуток времени")
    return '0'