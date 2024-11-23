import time

class Friend:
    def __init__(self,nickname):
        self.nickname=nickname

    def Display(self):
        print(f'{self.nickname}')    

    def __del__(self):
        print(f'Object Destroid....!')    

MyFriend=Friend('Rani')        
BestFriend=MyFriend
MyFriend.Display()  

del MyFriend    #Optional 

time.sleep(5)
print("After Sleep")
BestFriend.Display()