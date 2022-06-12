itemdict={
    '아이시스':600,
    '레몬워터':1500,
    '옥수수수염차':1300,
    '콘트라베이스':2000,
    '트레비':1000,
    '밀키스':800,
    '펩시':800,
    '핫식스':1000,
    '칠성사이다':1000,
    '코코리치망고':1000,
    '립톤':1000,
    '트로피카나사과':1000,
    '트로피카나포도':1000,
    '가나초코':600,
    '레쓰비':600,
    '칸타타':1000,
    '레쓰비카페타임':1000,
    '게토레이':800,
    '코코포도':800,
    '잔치집식혜':800
    }

class won:
    def __init__(self,rest):
        self.won_rest=rest
    def checking_won(self):
        print(str(self.won_rest)+'개')
    def __str__(self):
        sum=str(self.won_rest)
        return(sum)
    
class Choosing_item():
    
    def __init__(self,name,price,rest=100): #음료등록용
        self.name=name
        self.price=price
        self.rest=rest
    def __str__(self):
        sum=self.name +','+ str(self.price) +','+ str(self.rest)
        return(sum)
    def get_drink(name):
        amount=int(input('원하시는 개수를 입력하세요 : [  ]개\n:'))
        global money
        if name.rest<amount:
            print('재고가 부족합니다. 다른 음료를 선택해주세요.')
        else:    
            if (name.price)*amount <= money :
                print('%s %d개가 나왔습니다. 자판기 하단에서 수령하세요.\n' % (respon2,amount))
                name.rest-=amount
                money-=(name.price)*amount
            else:
                 print('돈이 부족합니다. ')
        
    def changes(): 
        global money
        rest_money=money
        _1000won=rest_money//1000
        rest_money -= 1000*_1000won
        _500wons=rest_money//500
        rest_money -= 500*_500wons
        _100wons=(rest_money)//100
        if _500won.won_rest<_500wons or _100won.won_rest<_100wons:
            print('잔돈이 부족합니다. 관리자에게 연락하세요. 01000000000')
        else:
            rest_money=money
            print("-"*20+'\n')
            if rest_money//1000>=1:
                #_1000won=rest_money//1000
                print('1000원 %d장을 반환합니다.\n ' % _1000won)
                #rest_money -= 1000*_1000won
                #_500wons=rest_money//500
                #rest_money -= 500*_500wons
                #_100wons=(rest_money)//100
                print('500원 %d개 , 100원 %d개를 반환합니다.\n' % (_500wons,_100wons))
                _500won.won_rest-=_500wons
                _100won.won_rest-=_100wons
            else:
                _500wons=rest_money//500
                rest_money -= 500*_500wons
                _100wons=(rest_money)//100
                print('500원 %d개 , 100원 %d개를 반환합니다.\n' % (_500wons,_100wons))
                _500won.won_rest-=_500wons
                _100won.won_rest-=_100wons
            rest_money=0
            money=0
            print('잔돈을 수령하세요. \n')
        

    def get_money(money): # 돈 받기
        money=money
    def get_instance(respon2):
        
        item_index=list_index.index(respon2)
        return list[item_index]
    def operate():
        
        print('500원 잔고 500개로 채우기 : "500up"\n100원 잔고 500개로 채우기 : "100up')
        respon4=input('500원 개수 확인 : "500" 입력\n100원 개수 확인 : "100" 입력\n음료 재고 확인 : "drink" 입력\n')
        if respon4=='500up':
            _500won.rest=500
        if respon4=='100up':
            _100won.rest=500
        if respon4=='500':
            _500won.checking_won()
        elif respon4=='100':
            _100won.checking_won()
        elif respon4=='drink':
            check_drink=input('재고를 확인할 음료 이름을 정확히 입력하세요.\n전체 음료의 재고를 확인 하려면 "all"을 입력하세요.\n: ')
            if check_drink=='all':
                for i in list:
                    print('%s , 남은 수량 %d 개' % (i.name,i.rest))
            elif check_drink in list_index:
                N=Choosing_item.get_instance(check_drink)
                print('%s , 남은 수량 %d 개' % (check_drink,N.rest))
                T=input('잔량을 채우시겠습니까?(+[  ]개/N(n))')
                if T=='n' or T=='N':
                    print()
                else:
                    N.rest+=int(T)
                    print('%s , 남은 수량 %d 개' % (check_drink,N.rest))
                                

def except1():
    if respon1=='q':          
        Choosing_item.changes()
        print('자판기를 종료합니다')
             
    elif respon1=='o':
        
        Choosing_item.operate()
                 
_500won=won(500)
_100won=won(500)
money=0

list=[]
list_index=[]
for name,price in itemdict.items():
    print(name)
    name=Choosing_item(name,price)
    list.append(name)
    list_index.append(name.name)

print('-'*20)
print('안내:"q"를 누르시면 종료 후 잔금을 반환합니다\n     "o"를 입력하시면 관리자 모드로 전환합니다\n')
print('돈을 먼저 입력하세요.(100원단위로 입력해주세요/5000원 이상의 지폐는 사용 불가합니다.)\n')
print('100원 미만 단위까지 입력했을 경우 100원 미만의 잔돈은 반환되지 않으니 주의해주세요.\n')
print('음료명을 정확히 입력하세요.(*음료이름에 띄어쓰기는 없습니다*)\n')


while True:
            
            #try:
                respon1=input("[    ]원\n")
                
                if respon1=='q' or respon1=='o' :
                    
                    except1()
                    break
                    
                respon2=input('["   "]\n')
                int(respon1)
            
                if respon2=='q':
                    
                    Choosing_item.changes()
                    print('자판기를 종료합니다')
                    break
                
                elif respon2=='o':
                    #관리자 모드 남은 수량,잔돈 재고
                    
                    Choosing_item.operate()
                    respon5=input('자판기를 다시 이용하시겠습니까? (Y(y)/N(n))')
                    if respon5 =='Y' or respon5 =='y':
                        continue
                    elif respon5 =='N' or respon5 =='n':
                        Choosing_item.changes()
                        print('자판기를 종료합니다')
                    
                elif int(respon1)>0 :
                    money+=int(respon1)
                    Choosing_item.get_money(money)
                
                if respon2 in itemdict.keys():
                    item_name=Choosing_item.get_instance(respon2)
                    Choosing_item.get_drink(item_name)
                    respon3=input('자판기를 다시 이용하시겠습니까? (Y(y)/N(n))')
                    if respon3 =='Y' or respon3 =='y':
                        continue
                    elif respon3 =='N' or respon3 =='n':
                        Choosing_item.changes()
                        print('자판기를 종료합니다')
                        break
                else: 
                    print('잘못입력하셨습니다. 자판기를 다시 실행합니다.')
                    
            #except :
                #print('죄송합니다. 오류가 발생했습니다. 자판기를 다시 실행합니다.')
                
                    
       
           
                    

            

