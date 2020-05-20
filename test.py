def set_tower_vars(hosts_list, hosts_size):
  with open('roles/tower/files/tower-setup/inventory', 'r') as file:
    data = file.readlines()
    i = 0
    while i < hosts_size:
      data[1] = ""+ hosts_list[i] +"\n"
  with open('roles/tower/files/tower-setup/inventory', 'w') as file:
    file.writelines( data )

ask_nodes= input("How many tower nodes do you want?\nEnter a number\n")
nodes = {}
i = 1
while i <= ask_nodes:
  print "Enter the fqdn of node number ", i
  node_fqdn = raw_input()
  nodes[i-1] = node_fqdn
  i += 1
set_tower_vars(nodes,ask_nodes)
