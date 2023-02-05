def ImplementAPI(logs):
    regUser = {}
    loginUser = {}
    res = []
    for i in logs:
        temp = i.split(" ")
        if(temp[0] == "register"):
            if(temp[1] in regUser):
                res.append("Username already exists")
                
            else:
                regUser[temp[1]] = temp[2]
                res.append("Registered Successfully")
        
        elif(temp[0] == "login"):
            if(temp[1] in regUser and temp[1] not in loginUser):
                if(regUser[temp[1]] == temp[2]):
                    loginUser[temp[1]] = temp[2]
                    res.append("Logged In Successfully")
                else:
                    res.append("Login Unsuccessful")
            else:
                res.append("Login Unsuccessful")
                    
        elif(temp[0] == "logout"):
            if(temp[1] in loginUser):
                loginUser.pop(temp[1])
                res.append("Logged Out Successfully")
            else:
                res.append("Logout Unsuccessful")
    return res
