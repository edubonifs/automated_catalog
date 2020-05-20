def set_tower_vars(hosts_list, hosts_size):
  with open("roles/tower/files/tower-setup/inventory", "r") as in_file:
    buf = in_file.readlines()
    buf[1] = ""
  #with open('inventory', 'w') as file:
   # file.writelines( data ) 
  with open("roles/tower/files/tower-setup/inventory", "w") as out_file:
    i = 0
    for line in buf:
      if line == "[tower]\n":
        while  i < hosts_size:
          line = line + hosts_list[i] + "\n"
          i += 1
      out_file.write(line)

ask_nodes= input("How many tower nodes do you want?\nEnter a number\n")
nodes = {}
i = 1
while i <= ask_nodes:
  print "Enter the fqdn of node number ", i
  node_fqdn = raw_input()
  nodes[i-1] = node_fqdn
  i += 1
set_tower_vars(nodes,ask_nodes)
