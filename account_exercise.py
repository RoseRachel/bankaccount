class BankAccount:
  def __init__(self,first_name, last_name,bank,phone_number):
     self.first_name=first_name self.last_name=last_name
     self.bank=bank  
     self.deposits=[]
     self.balance=0
     self.phone_number=phone_number
     self.withdrawal=[]
     self.loans=0
    
  def account_name(self):
    name="{} the user {} {}".format(self.bank, self.first_name, self.last_name )
    return name

  def deposit(self, amount):
        self.balance +=amount
        print("You have deposited {} to your account".(format(amount)))   
  
  def withdraw(self, amount):
      if amount > 0 :
      print("Insufficient funds in your account to purchase the order.",)
      else:
    self.balance -=amount
    print("You have withdrawn {} "" Ksh from your account".(format (amount))
    
  def withdrawalstatement(self):
      withdrawal=withdrawal.append(withdraw())
      return withdraw
  
  def loangiven(self,amount):
      print("You have received a loan amount of Ksh {}:".format(amount))
      self.loans= self.loans + amount
      
  def loanrepayed(self,amount):
      if amount >=1:
          self.repay=self.loansamount
          print("You have repayed Ksh {}".format(amount))
          print("Your loan balance is: {}".format(self.repay))
          
acc1=BankAccount("Rose", "Rachel")
acc2=BankAccount("Athman","Athman")
acc3=BankAccount("Sheilla","Simpanoi")
 
acc1.deposit (2000)
acc2.deposit (3000)
acc3.deposit(90000)

acc1.withdraw(30400)
acc2.withdraw(80000)
acc3.withdraw(890000)     

print(acc1.withdrawalstatement())
print(acc2.withdrawalstatement())
print(acc3.withdrawalstatement())

print(acc1.loangiven())

print(acc1.loanrepayed())
 
 