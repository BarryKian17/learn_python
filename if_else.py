user = input("Your name? : ");
password = input("Create password : ");

print("Register success and you can login now");

loginName = input("User name:");
loginPw = input("password:");

if loginName == user and loginPw == password:
    print("login Successful");
else:
    print("incorrect credential");