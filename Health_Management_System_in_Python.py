
# Health Management System

client_list = {1:'Kamlesh', 2:'Ridhima', 3:'Kavi'}      # this is Dictionary
log_list = {1:'Exercise', 2:'Diet'}

def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("Select the Client Name")
    for key,value in client_list.items():
        print("Press",key, "for",value,"\n",end='')
    client_name = int(input())
    print("Selected Client : ",client_list[client_name])

    print("Press 1 for Log")
    print("Press 2 for Retrive")
    op = int(input())

    if op == 1:
        for Key,Value in log_list.items():
            print("Select",Key,"for",Value,"\n",end='')
        log_name = int(input())
        print("Selected Job is : ",log_list[log_name])
        f = open(client_list[client_name] + "_" + log_list[log_name] + ".txt","a")

        k='y'
        while k != 'n':
            print("Enter",log_list[log_name])
            mytext = input()
            f.write("["+ str(getdate()) + "]" + mytext + "")
            k = input("ADD MORE ? y/n:")
            continue
        f.close()
    elif op == 2:
        for Key,Value in log_list.items():
            print("Select",Key,"for",Value,"\n",end='')
        log_name = int(input())
        print("Selected Job is : ",log_list[log_name])
        print(client_list[client_name] +"_"+ log_list[log_name],"Report : \n", end='')
        f = open(client_list[client_name]+"_"+log_list[log_name] +".text",'r')
        contents = f.readlines()

        for data in contents:
            print(data,end='')
        f.close()
    else:
        print("Invalid Input !!!")

except Exception as e:
    print("Wrong input !!!")
    
