class dress:
    def __init__ (self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
    def show(self):
        print('Details:',self.name,self.color,self.price)
    def specifications(self):
        print('good dress')
    def designer(Self):
        print('asiya chapri designer')
class kanmanifreesize:
    def __init__(self,kan):
        self.kan=kan
    def showkan(self):    
        print("kanmani dress is very chapri dont buy hahahah")
d=dress('asiya chapri dress','colour chapri','0')
d.show()
d.specifications()
d.designer()
c=kanmanifreesize("hahah")
c.showkan()
