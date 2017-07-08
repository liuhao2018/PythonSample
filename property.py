class Person(object):
    def __init__(self, name, age, sex):
        self.__name = name
        self.__age = age
        self.__sex = sex

    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getSex(self):
        return self.__sex

    def setName(self,name):
        self.__name = name
    def setAge(self,age):
        self.__age = age
    def setSex(self,sex):
        self.__sex = sex
    name = property(getName,setName)

person = Person('xiaoming',18,0);
print person.getName()

