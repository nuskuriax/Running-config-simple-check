#variables to check
passwordauth=0
passrecovery=0
exectimeout=0
memoryres=0
auth=0
ntp=0
log=0
#othervariables
repeat0=0
repeat1=0
a=input("File name(with extention): ")
file1 = open(a, 'r') 
Lines = file1.readlines() 
count = 1
for line in Lines: 
    b=("{}".format(line.strip()))
    if (("hostname" in line.strip())& (repeat0==0)):
        b=b.replace("hostname ", "")
        print("Hostname: ",b)
        repeat0=1
    elif (("domain-name" in line.strip()) & (repeat1==0)):
        b=b.replace("domain-name ", "")
        print("Domain: ",b)
        repeat1=1
    elif ("ASA Version" in line.strip()):
        b=b.replace("ASA Version ", "")
        b=b.replace("(", "")
        b=b.replace(")", "")
        if ((float(b) < 9.1) | (float(b) == 9.3) | (float(b) == 9.5)):
            print("(!)WARNING outdated ASA version")
        else:
            print("ASA version OK")
    elif ("no service password-recovery" in line.strip()):
        passrecovery=1
    elif ("exec-timeout" in line.strip()):
        exectimeout=1
    elif ("memory reserve critical" in line.strip()):
        memoryres=1
    elif (("aaa-authentication" in line.strip()) | ("aaa-server" in line.strip())):
        auth=1
    elif (("ntp authenticate" in line.strip()) & ("ntp" in Lines)):
        ntp=1
    elif (("permit" in line.strip()) & ("any any" in line.strip())):
        print("(!)WARNING Permisive rule found")
        print("Check line: {}".format(count))
    elif (("permit" in line.strip()) & (("eq 22" in line.strip()) | ("eq 80" in line.strip()) | ("eq 21" in line.strip()) | ("eq 23" in line.strip()) | ("eq ssh" in line.strip()) | ("eq http" in line.strip()) | ("eq telnet" in line.strip()))):
        print("(!)WARNING Plaintext comunication rule found")
        print("Check line: {}".format(count))
    elif (("logging enable" in line.strip()) & ("ntp" in Lines)):
        log=1
    
    
    
    
    
    else:
        c=1 #nothing
    count=count+1
if passwordauth==0:
    print("(!)WARNING Device password authentication missing")
if passrecovery==0:
    print("(!)WARNING Password recovery service not disabled")
if auth==0:
    print("(!)WARNING No authentication configured")
if exectimeout==0:
    print("(!)WARNING No NTP authentication configured")
if exectimeout==0:
    print("(!)WARNING No console execution timeout configured")
if log==0:
    print("(!)WARNING Logging is not enabled")
if memoryres==0:
    print("(!)WARNING No memory reservation configured") #check https://www.cisco.com/en/US/docs/ios/12_3t/12_3t4/feature/guide/gt_memnt.html" - agregar?
