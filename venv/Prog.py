print("Введите количество программистов")
num=int(input())
word="программист"
end_a="а"
end_ov="ов"
if num==0 or num%10==0 or 5<=num<=20 or 5<=num%10<=20 or 5<=num%100<=20:
    print(num,word+end_ov)
if num%10==1 and (num-11)%100!=0:
    print(num,word)
if (num%10==2 and (num-12)%100!=0) or (num%10==3 and (num-13)%100!=0) or (num%10==4 and (num-14)%100!=0):
    print(num,word+end_a)
print("Для выхода нажмите любую клавишу")
quit()