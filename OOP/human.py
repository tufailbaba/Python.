class Human():
    def __init__(self,name,occupation):
        self.name = name
        self.occ  =occupation
    def do_work(self):
        if self.occ == "footballer":
            print(self.name, "is a footballer")
        elif self.occ == "cricketer":
            print(self.name, " is a cricketer")
    def speaks (self):
        print(self.name,'Hi')
        
person = Human("Babar Azam","cricketer" )
person.do_work()
person.speaks()        
               
                