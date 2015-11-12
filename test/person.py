class person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def giveraise(self, procente): #Подъём зарплаты в долях
        self.pay=int(self.pay*(1+procente))
    def lastname(self): #Возврат Фамилии
        return self.name.split()[-1]
    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay) #Строка для вывода
"""if __name__ == '__main__':
    bob = person('Bob test', 'Developer', 100)
    sue = person('Sue test')
    print(bob)
    print(bob.job)
    print(bob.pay)
    print(sue.name)"""#Тестирование
