import sys
def check_ip(ip_add_split):
    if len(ip_add_split)!=4: return 0
    else:
        for i in range(0,4):
            if ip_add_split[i] > 255 : return 0
        return 1


def classify_ip(ip_add_split):
    x = ip_add_split[0]
    if x >= 0 and x<=127: return 'A'
    elif x>127 and x<=191: return 'B'
    elif x>191 and x<=223: return 'C'
    elif x>223 and x<=239: return 'D'
    elif x>239 and x<=255: return 'E'
    else: return 'null'

ip_add : str
ip_add_split : list
def onboarding():
    global ip_add
    global ip_add_split
    ip_add = input("Enter a valid IP Address: ")
    ip_add_split = list(map(int,ip_add.split(".")))

def subnet_mask(ip_class):
    if ip_class == 'A':
        return [255,0,0,0]
    elif ip_class == 'B':
        return [255,255,0,0]
    elif ip_class == 'C':
        return [255,255,255,0]

def remove_zero(x):
    while 0 in x:
        x.remove(0)
    return x

def print_net_id(net_id):
    n = ""
    for i in net_id:
        n = n + str(i) + "."
    n = n[0:(len(n)-1)]
    print(f"Net ID is {n}")

def print_host_id(host_id):
    n = ""
    for i in host_id:
        n = n + "." + str(i)
    
    print(f"Host ID is {n}")

# main
onboarding()
while(not check_ip(ip_add_split)):
    print("Invalid IP Address")
    onboarding()

ip_class = classify_ip(ip_add_split)

print(f"This IP Address belongs to Class {ip_class}")
if ip_class=='D' or ip_class=='E':
    print("This is a reserved IP Address.")
    sys.exit()

net_id = [x & y  for x,y in zip(ip_add_split, subnet_mask(ip_class))]
host_id = [x & (y ^ 255) for x,y in zip(ip_add_split, subnet_mask(ip_class))]  # y^255 -> 1's complement

net_id = remove_zero(net_id)
host_id = remove_zero(host_id)  

print_net_id(net_id)
print_host_id(host_id)
    
