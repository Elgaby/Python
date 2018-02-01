import re

vlan_pattern = re.compile('(s\w+)\s(t\w+.+)\s(\d.+)')

all_commands_dict = [] # this will be a list of commands in dict format 
command_info = {} # Create the inner dictionary of command info

# Read all lines of command information from file
file = open('commands.txt','r')
for line in file:
    command_info_list = line.strip().split('#') # Get command info into list

    

    # locate the VLANs and put it into command_info dictionary
    vlan = vlan_pattern.search(line)
    if vlan:
    	command = vlan.group(3)
    else:
    	continue

    # add the dictionary element to the all_commands list 
    all_commands_dict.append(command)
   
	
all_commands_dict= list(all_commands_dict)
all_commands_dict= ",".join(all_commands_dict)
all_commands_dict1= list(all_commands_dict)
all_commands_dict1=all_commands_dict.split(',')

list1= []
list2= []
for numb in all_commands_dict1:
    if all_commands_dict1.count(numb) > 2:
        
            list2.append(int(numb))
            list2=set(list2)
            list2=list(list2)
            list2.sort()
    
    elif all_commands_dict1.count(numb) == 1:
            list1.append(int(numb))
            list1.sort();
            
    else:
        continue

print ("Liste_1:", list1)

print ("Liste_2:", list2)
