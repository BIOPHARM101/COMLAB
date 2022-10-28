def run():
    cho_sol = input("เลือกเฉลยทีขอร้อง :")
    cho_ex = input('เลือกคำตอบนะ :')
    cho_sol = open(cho_sol,'r')
    cho_ex = open(cho_ex,'r')
    student_score = []
    question =[]
    minn =[]
    maxx =[]
    cho_sol = cho_sol.readline().split()
    cho_ex = cho_ex.readlines()
    n = 0
    numbera = 0
    for i in range(0,8):
        for j in range(0,10):
            if cho_sol[j] == cho_ex[i].split()[j]:
                n += 1
        student_score.append(n)
        n =0
    for i in range(0,8):
        for j in range(0,10):
            for h in range(0,8):
                if cho_sol[j] == cho_ex[h].split()[j]:
                    n +=1 
            if numbera <10:
                question.append(n/8)
                n=0
                numbera +=1
    print('Student score :',student_score)
    print('')
    for i in range(1,11):
        print('Question',i,':',question[i-1])
    print('')
    n=0
    for i in range(0,10):
        n+=1
        if max(question) == question[i]:
            maxx.append(n)
        elif min(question) == question[i]:
            minn.append(n)
    print('Hardest : ',end='')
    for i in minn:
        print(i,'',end='')
    print('')
    print("Easiest : ",end='')
    for i in maxx:
        print(i,'', end='')
run()