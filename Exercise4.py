import re


access_template = ['switchport mode access','switchport access vlan {}','switchport nonegotiate','spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q','switchport mode trunk', 'switchport trunk allowed vlan {}']
x=input("Enter interface mode (access/trunk):")

y=input("Enter interface type and number: ")


if x=='access':
    z=input("Enter VLAN number: ")
    print ("Interface",y)
    
    access_template = [w.replace('{}', z) for w in access_template]   
   
    for line in access_template:
        print(line)
elif x=='trunk':
    a=input("Enter allowed VLANs:")
    trunk_template = [w.replace('{}', a) for w in trunk_template] 
    print ("Interface",y)

    for line in trunk_template:
        print (line)
else:
    print("sorry there was an error in your entry. Please try again")


