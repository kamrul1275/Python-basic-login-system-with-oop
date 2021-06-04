class user:
    name = ''
    email = ''
    password = ''
    login = False
    
    def __init__(self,name,email,password) -> None:
         self.name = name
         self.email = email
         self.password = password
         
    def login(self):
        email = input("Enter your email :")
        password = input ("Enter your password :")

        if email == self.email and password == self.password:
            login=True
            print("login succesfully")
        else:
            print("login faill!")

    def logout(self):      
        login =False
        print ("logged outt")


    def isloggedIn(self):

        if self.login :
            return True
        else :
            return False

    def profile (self):

        if self.isloggedIn():
            print (self.name, "-" , self.email)

        else: print("user not login")    

user1 = user('kamrul hassan','kamrulhassan5343@gmail.com','998877')

user1.login()
user1.profile()



