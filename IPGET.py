
# Python3 code to display hostname and 
# IP address 

# Importing socket library 
import socket, os, time

#This code is conributed by "Sharad_Bhardwaj". 
# Function to display hostname and 
# IP address 
def get_Host_name_IP(): 
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("Hostname :  ",host_name) 
        print("IP : ",host_ip)
        return(host_ip)
    except: 
        print("Unable to get Hostname and IP")
        #no host is 0
        return(0)
    
  
# Driver code 
ip = get_Host_name_IP() #Function call
os.system("cd /tmp/test/")
file = open("IPadress.txt",'w')
file.write(ip)
file.close()


os.system("cd /tmp/test/")
os.system("git clone https://github.com/Quiltic/Rasberi-Pi-Stuffs.git")
print("cloned")
timestamp = "git commit -m 'Updating the IP Timestamp: %s'" % time.localtime
os.system(timestamp)
os.system("git push")