class jenkins_test:
    def hello_world(self):
        return 'Hello World'
    
    def add_two(self):
        num1 = 5
        num2 = 3
        return num1 + num2

x = jenkins_test()
print(x.hello_world())