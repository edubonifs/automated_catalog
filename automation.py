import os

#Define host name in which the installation will be done
def write_host(hostame):
  with open('satellite.yml', 'r') as file:
    data = file.readlines()
    data[2] = "  hosts: " + hostname +"\n"
  with open('satellite.yml', 'w') as file:
    file.writelines( data )
  with open('inventory', 'r') as file:
    data = file.readlines()
    data[1] = "" + hostname +"\n"
  with open('inventory', 'w') as file:
    file.writelines( data )

#Write Version of satellite, whether you want to make partitions or not, if you want to subscribe your nodes, organization, location, admin username and password
def set_vars(version,parted,sub,name,passwd,org,loc,enable_repos):
  with open('roles/satellite/vars/main.yml', 'r') as file:
    data = file.readlines()
    data[1] = "version: " + version +"\n"
    data[2] = "parted: " + parted +"\n"
    data[3] = "sub: " + sub + "\n"
    data[4] = "admin: " + name  + "\n"
    data[5] = "passwd: " + passwd + "\n"
    data[6] = "organization: " + org + "\n"
    data[7] = "location: " + loc + "\n"
    data[8] = "enable_repos: " + enable_repos +"\n"
  with open('roles/satellite/vars/main.yml', 'w') as file:
    file.writelines( data )

#Set tower nodes' hostnames, database, passwords and ports
def set_tower_vars(hosts_list, hosts_size,database, admin_pass):
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
      if line == "[database]\n":
        line = line + database +"\n"
      if line == "admin_password=\'\'"
        out_file.write("admin_password=\'" + admin_pass + '\n")
      if line == "pg_host=\'\'"
        out_file.write("pg_host=\'" + database + "\'\n")
      if line == "pg_port=\'\'"
        out_file.write("pg_host=\'5432\'\n")
      out_file.write(line)


product = input("Which product would you like to choose?\n1-Satellite\n2-Tower\n3-OCP\n4-IDM\n")
if product == 1:
  print("You chosed Satellite")
  action = input("Which action would you like to take?\n1-Satellite installation\n2-Capsule Installation \n3-Satellite Upgrade \n4-Capsule Upgrade\n")
  if action == 1:
    print("You chosed Satellite installation\n")
    hostname = raw_input("Enter the hostname of the Satellite\n")  
    write_host(hostname)
    ask_version = raw_input("Enter the version of Satellite you would like to install\n1-6.6\n2-6.7\n")
    if ask_version == "1":
      version = "6.6"
    else:
      version = "6.7"
    ask_parted = raw_input("Do you want to make partitions for /dev/vdb and /dev/vdc?\n(Recommended for quicklab installations)\n1-Yes\n2-No\n")
    if ask_parted == "1":
      parted = "true"
    else:
      parted = "false"
    ask_sub= raw_input("Do you want to subscribe the node?\n1-Yes\n2-No\n")
    if ask_sub == "1":
      sub = "true"
    else:
      sub = "false"
    ask_enabled= raw_input("Do you want to enable the repos?\n1-Yes\n2-No\n")
    if ask_enabled == "1":
      enable_repos = "true"
    else:
      enable_repos = "false"
    name = raw_input("Enter the admin username\n")
    passwd = raw_input("Enter the password of the admin\n")
    org = raw_input("Enter Organization name\n")
    loc = raw_input("Enter Location name\n")
    set_vars(version,parted,sub,name,passwd,org,loc,enable_repos)
    os.system('ansible-playbook satellite.yml --ask-vault-pass')
  elif action == 2:
    print("You chosed Capsule Installation")
    hostname = raw_input("Enter the hostname of the Capsule\n")
    write_host(hostname)
    ask_version = raw_input("Enter the version of Capsule you would like to install\n1-6.6\n2-6.7\n")
    if ask_version == "1":
      version = "6.6"
    else:
      version = "6.7"
  elif action == 3:
    print("You chosed Satellite Upgrade")
  else:
    print("You chosed Capsule Upgrade")
elif product == 2:
  print("You chosed Tower")
  ask_sub= raw_input("Do you want to subscribe the node?\n1-Yes\n2-No\n")
  if ask_sub == "1":
    sub = "true"
  else:
    sub = "false"
  ask_nodes= input("How many tower nodes do you want?\nEnter a number\n")
  nodes = {}
  i = 1
  while i <= ask_nodes:
    print "Enter the hostname of node number", i
    print "(Please enter the hostnames of each one in the same format)"
    node_fqdn = raw_input()
    nodes[i-1] = node_fqdn
    i += 1
  ask_dat = input("Do you want a database?\n1-Yes\n2-No\n")
  if ask_dat == 1:
    database = raw_imput("Enter the hostname of the database\n")
  admin_pass = raw_input("Enter the password of the admin\n")
  set_tower_vars(nodes,ask_nodes,database,admin_pass)
elif product == 3:
  print("You chosed OCP")
else:
  print("You chosed IDM")
