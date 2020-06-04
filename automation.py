import os


#Define host name in which the installation will be done
def write_host(hostame):
  #Open and write the host to satellite.yml playbook
  with open('satellite.yml', 'r') as file:
    data = file.readlines()
    data[2] = "  hosts: " + hostname +"\n"
  with open('satellite.yml', 'w') as file:
    file.writelines( data )
  #Open and write the host in the inventory file
  with open('inventory', 'r') as file:
    data = file.readlines()
    data[1] = "" + hostname +"\n"
  with open('inventory', 'w') as file:
    file.writelines( data )

#Define hostname in which IDM will be installed
  with open('idm.yml', 'r') as file:
    data = file.readlines()
    data[2] = "  hosts: " + hostname +"\n"
  with open('idm.yml', 'w') as file:
    file.writelines( data )
  #Open and write the host in the inventory file
  with open('inventory', 'r') as file:
    data = file.readlines()
    data[1] = "" + hostname +"\n"
  with open('inventory', 'w') as file:
    file.writelines( data )

#Define host name in which the installation will be done
def write_host_capsule(hostame,satellite,sub):
  #Open and write the host in the inventory file
  with open('inventory', 'r') as file:
    data = file.readlines()
    data[0] = "[capsule]\n"
    data[1] = "" + hostname +"\n"
    data[2] = "" + satellite +"\n"
  with open('inventory', 'w') as file:
    file.writelines( data )

#Function to write the host of OCP
def write_host_ocp(nodes,ask_nodes):
  #Open and write the host to ocp3.yml playbook
  with open('ocp3.yml', 'r') as file:
    data = file.readlines()
    data[2] = "  hosts: all\n"
  with open('tower.yml', 'w') as file:
    file.writelines( data )
  #Open and write the host in the inventory file
  with open('inventory', 'r') as file:
    data = file.readlines()
    i = 0
    while i < nodes_size:
      data[i] = nodes[i] +"\n"
      i += 1
  with open('inventory', 'w') as file:
    file.writelines( data )

#Function to write the hostname in different files for Tower installation
def write_host_tower(nodes,nodes_size,database,database_boolean):
  #Open and write the host to capsule.yml playbook
  with open('tower.yml', 'r') as file:
    data = file.readlines()
    data[2] = "  hosts: all\n"
  with open('tower.yml', 'w') as file:
    file.writelines( data )
  #Open and write the host in the inventory file
  with open('inventory', 'r') as file:
    data = file.readlines()
    i = 0
    while i < nodes_size:
      data[i] = nodes[i] +"\n"
      i += 1
    if database_boolean == "true":
      data[i] = database + "\n"
  with open('inventory', 'w') as file:
    file.writelines( data )


#Define host name in which the Satellite upgrade will be done
def  write_host_up_sat(sat_host):
  #Open and write the host in the inventory file
  with open('inventory', 'r') as file:
    data = file.readlines()
    data[1] = "" + sat_host +"\n"
  with open('inventory', 'w') as file:
    file.writelines( data )
  with open('upgrade-satellite.yml', 'r') as file:
    data = file.readlines()
    data[2] = "  hosts: " + sat_host +"\n"
  with open('upgrade-satellite.yml', 'w') as file:
    file.writelines( data )


#Define host name in which the Capsule upgrade will be done
def  write_host_up_cap(cap_host):
  #Open and write the host in the inventory file
  with open('inventory', 'r') as file:
    data = file.readlines()
    data[1] = "" + cap_host +"\n"
  with open('inventory', 'w') as file:
    file.writelines( data )
  with open('upgrade-capsule.yml', 'r') as file:
    data = file.readlines()
    data[2] = "  hosts: " + cap_host +"\n"
  with open('upgrade-capsule.yml', 'w') as file:
    file.writelines( data )


#Write the IDM host
def write_host_idm(hostname):
  #Open and write the host in the inventory file
  with open('inventory', 'r') as file:
    data = file.readlines()
    data[1] = "" + hostname +"\n"
  with open('inventory', 'w') as file:
    file.writelines( data )
  with open('idm.yml', 'r') as file:
    data = file.readlines()
    data[2] = "  hosts: " + hostname +"\n"
  with open('idm.yml', 'w') as file:
    file.writelines( data )
  with open('idm_no_sub.yml', 'r') as file:
    data = file.readlines()
    data[2] = "  hosts: " + hostname +"\n"
  with open('idm_no_sub.yml', 'w') as file:
    file.writelines( data )

#Function for setting the version in which to upgrade the satellite
def write_version_up_sat(sat_version):
  with open('roles/upgrade-satellite/vars/main.yml', 'r') as file:
    data = file.readlines()
    data[1] = "version: "+ sat_version +"\n"
  with open('roles/upgrade-satellite/vars/main.yml', 'w') as file:
    file.writelines( data )


#Function for setting the version in which to upgrade the capsule
def set_vars_up_cap(proxy):
  with open('roles/upgrade-capsule/vars/main.yml', 'r') as file:
    data = file.readlines()
    data[2] = "proxy: "+ proxy +"\n"
  with open('roles/upgrade-capsule/vars/main.yml', 'w') as file:
    file.writelines( data )


#Function for telling tower that the setup bundle has been downloaded
def set_downloaded(downloaded):
  with open('roles/tower/vars/main.yml', 'r') as file:
    data = file.readlines()
    data[3] = "downloaded: "+ downloaded +"\n"
  with open('roles/tower/vars/main.yml', 'w') as file:
    file.writelines( data )


#Function for telling tower that he can proceed with the installation
def set_install(install):
  with open('roles/tower/vars/main.yml', 'r') as file:
    data = file.readlines()
    data[4] = "install: "+ install +"\n"
  with open('roles/tower/vars/main.yml', 'w') as file:
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
    data[8] = "enable_repos: " + enable_repos + "\n"
  with open('roles/satellite/vars/main.yml', 'w') as file:
    file.writelines( data )


#Write admin user of satellite, admin_passwd, satellite hostname, if using load balancer or nor, the version of the capsule and wether you want to subscribe the node
def set_vars_capsule(admin,admin_passwd,satellite,lb,version,sub,enable_repos,hostname,sat_fqdn):
  with open('roles/capsule/vars/main.yml', 'r') as file:
    data = file.readlines()
    data[2] = "admin: " + admin +"\n"
    data[3] = "admin_passwd: " + admin_passwd +"\n"
    data[4] = "satellite: " + satellite + "\n"
    data[5] = "sub: " + sub + "\n"
    data[6] = "version: " + version + "\n"
    data[7] = "loadbalancer: " + lb + "\n"
    data[8] = "enable_repos: " + enable_repos + "\n"
    data[9] = "capsule: " + hostname + "\n"
    data[10] = "satellite_fqdn: " + sat_fqdn + "\n"
  with open('roles/capsule/vars/main.yml', 'w') as file:
    file.writelines( data )


#Function for asking wether you want to subscribe your node
def set_vars_tower(sub):
  with open('roles/tower/vars/main.yml', 'r') as file:
    data = file.readlines()
    data[2] = "sub: " + sub +"\n"
  with open('roles/tower/vars/main.yml', 'w') as file:
    file.writelines( data )

#Function for asking wether you want to subscribe your node
def set_vars_idm(sub,dns,reverse,realm,dm_passwd,ipa_passwd,ntp,forward,unattended):
  with open('roles/idm/vars/main.yml', 'r') as file:
    data = file.readlines()
    data[1] = "sub: " + sub +"\n"
    data[2] = "dns: " + dns +"\n"
    data[3] = "reverse: " + reverse +"\n"
    data[4] = "realm: " + realm +"\n"
    data[5] = "dm_passwd: " + dm_passwd +"\n"
    data[6] = "ipa_passwd: " + ipa_passwd +"\n"
    data[7] = "ntp: " + ntp +"\n"
    data[8] = "forward: " + forward +"\n"
    data[9] = "unattended: " + unattended +"\n"
  with open('roles/idm/vars/main.yml', 'w') as file:
    file.writelines( data )

#Set tower nodes, hostnames, database, passwords and ports
def set_tower_vars(hosts_list, hosts_size,database,database_bool,admin_pass,pg_passwd):
  with open("roles/tower/files/tower-setup/inventory", "r") as in_file:
    buf = in_file.readlines()
    buf[1] = ""
  with open("roles/tower/files/tower-setup/inventory", "w") as out_file:
    i = 0
    for line in buf:
      if line == "[tower]\n":
        while  i < hosts_size:
          line = line + hosts_list[i] + "\n"
          i += 1
      if line == "[database]\n":
        line = line + database +"\n"
      if line == "admin_password=''\n":
        out_file.write("admin_password="+"'"+ admin_pass + "'"+"\n")
      if line == "pg_host=''\n":
        if database_bool == "true":
          out_file.write("pg_host="+"'"+ database + "'"+"\n")
      if line == "pg_port=''\n":
        if database_bool == "true":
          out_file.write("pg_port="+"'"+"5432"+"'"+"\n")
      if line == "pg_password=''\n":
        out_file.write("pg_password="+"'"+pg_passwd+"'"+"\n")
      out_file.write(line)
  with open("roles/tower/files/tower-setup/inventory", 'r') as file:
    data = file.readlines()
    if database_bool == "true":
      data[7+hosts_size]=""
      data[10+hosts_size]=""
      data[12+hosts_size]=""
      data[17+hosts_size]=""
    else:
      data[4+hosts_size]=""
      data[7+hosts_size]=""
      data[15+hosts_size]=""
  with open("roles/tower/files/tower-setup/inventory", 'w') as file:
    file.writelines( data )


#We start with the program
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
    ask_parted = raw_input("Do you want to make partitions for /dev/vdb and /dev/vdc for having a 20GB SWAP?\n(Recommended for quicklab installations)\n1-Yes\n2-No\n")
    if ask_parted == "1":
      parted = "true"
    else:
      parted = "false"
    ask_sub= raw_input("Do you want to subscribe the node?\n1-Yes\n2-No\n")
    if ask_sub == "1":
      sub = "true"
    else:
      sub = "false"
    if sub == "false":
      ask_enabled= raw_input("Do you want to enable the repos?\n1-Yes\n2-No\n")
      if ask_enabled == "1":
        enable_repos = "true"
      else:
        enable_repos = "false"
    else:
      enable_repos = "true"
    name = raw_input("Enter the admin username\n")
    passwd = raw_input("Enter the password of the admin\n")
    org = raw_input("Enter Organization name\n")
    loc = raw_input("Enter Location name\n")
    set_vars(version,parted,sub,name,passwd,org,loc,enable_repos)
    os.system('ansible-playbook satellite.yml --ask-vault-pass')
  elif action == 2:
    print("You chosed Capsule Installation")
    #Ask for the capsule hostname
    hostname = raw_input("Enter the hostname of the Capsule\n")

    #Ask for the version of the capsule to install
    ask_version = raw_input("Enter the version of Capsule you would like to install\n1-6.6\n2-6.7\n")
    if ask_version == "1":
      version = "6.6"
    else:
      version = "6.7"

    #Ask wether you want to subscribe the nodes or not
    ask_sub = raw_input("Do you want to subscribe the node?\n1-Yes\n2-No\n")
    if ask_sub == "1":
      sub = "true"
    else:
      sub = "false"

    #Ask wether you want to enable the repos or not
    if sub == "false":
      ask_enabled= raw_input("Do you want to enable the repos?\n1-Yes\n2-No\n")
      if ask_enabled == "1":
        enable_repos = "true"
      else:
        enable_repos = "false"
    else:
      enable_repos = "true"
    
    #Ask wether you want to subscribe the nodes or not
    ask_lb = input("Do you want the Capsule with load balancer?\n1-Yes\n2-No\n")
    if ask_lb == 1:
      lb = "true"
    else:
      lb = "false"

    #Ask for the satellite hostname
    satellite = raw_input("Please enter Satellite hostname\n")

    #Ask for the Satellite username
    admin = raw_input("Please enter your satellite username\n")

    #Ask for the password of the user
    admin_passwd = raw_input("Please enter your password\n")

    #Ask for the Satellite fqdn
    sat_fqdn = raw_input("Please enter satellite fqdn\n")

    #Call the function for writing the variables in the capsule role    
    set_vars_capsule(admin,admin_passwd,satellite,lb,version,sub,enable_repos,hostname,sat_fqdn)

    #Run capsule role
    if sub:
      #Write hostname on capsule.yml and inventory
      write_host_capsule(hostname,satellite,sub) 
      os.system('ansible-playbook capsule.yml --ask-vault-pass')
    else:
      #Write hostname on capsule_no_sub.yml and inventory
      write_host_capsule(hostame,satellite,sub)
      os.system('ansible-playbook capsule_no_sub.yml')

  elif action == 3:
    print("You chosed Satellite Upgrade")

    #Ask for the hostame of the satellite
    sat_host = raw_input("Enter the hostname of the satellite\n")
    write_host_up_sat(sat_host)

    #Ask the version to which you want to update
    ask_sat_version = raw_input("To which version would you like to update?\n1-6.7\n")
    if ask_sat_version == "1":
      sat_version = "6.7"
      write_version_up_sat(sat_version)
    else:
      print("This version is not allowed")

    #Run the playbook
    os.system('ansible-playbook upgrade-satellite.yml')

  else:
    print("You chosed Capsule Upgrade")

    #Ask for the hostame of the capsule
    cap_host = raw_input("Enter the hostname of the capsule\n")
    write_host_up_cap(cap_host)

    #Ask if using the capsule as a proxy for discovered hosts
    ask_proxy = raw_input("Do you plan to use the Capsule as a proxy for discovered hosts\n1-Yes\n2-No\n")
    if ask_proxy == "1":
      proxy = "true"
    else:
      proxy = "false"
    set_vars_up_cap(proxy)

    #Run the playbook
    os.system('ansible-playbook upgrade-capsule.yml')

elif product == 2:
  print("You chosed Tower")
  ask_sub= raw_input("Do you want to subscribe the nodes?\n1-Yes\n2-No\n")
  if ask_sub == "1":
    sub = "true"
  else:
    sub = "false"
  set_vars_tower(sub)
  ask_nodes= input("How many tower nodes do you want?\nEnter a number\n")
  if ask_nodes== 1:
    ask_local= input("Is this node localhost?\n1-Yes\n2-No\n")
    if ask_local == 1:
      nodes = {}
      nodes[0] = "localhost ansible_connection=local"
    else:
      nodes = {}
      print "Enter the hostname of the node"
      node_fqdn = raw_input()
      nodes[0] = node_fqdn
  else:
    nodes = {}
    i = 1
    while i <= ask_nodes:
      print "Enter the hostname of node number ", i
      print "Please write all of them in the same format"
      node_fqdn = raw_input()
      nodes[i-1] = node_fqdn
      i += 1
  ask_dat = input("Do you want a database?\n1-Yes\n2-No\n")
  if ask_dat == 1:
    database = raw_input("Enter the hostname of the database\n")
    database_bool = "true"
  else:
    database = ""
    database_bool = "false"
  admin_pass = raw_input("Enter the password of the admin\n")
  pg_passwd = raw_input("Enter postgres password\n")
  downloaded = "false"
  set_downloaded(downloaded)
  os.system('ansible-playbook tower_download.yml')
  downloaded = "true"
  set_downloaded(downloaded)
  write_host_tower(nodes,ask_nodes,database,database_bool)
  set_tower_vars(nodes,ask_nodes,database,database_bool,admin_pass,pg_passwd)
  install = "false"
  set_install(install)
  if ask_sub == "1":
    os.system('ansible-playbook tower_subscribe.yml --ask-vault-pass')
  install = "true"
  set_install(install)
  os.system('ansible-playbook tower.yml')
  os.system('./roles/tower/files/tower-setup/setup.sh')
elif product == 3:
  print("You chosed OCP")
 
  ask_nodes= input("How many tower nodes do you want in your cluster?\nEnter a number\n")
  print "Enter the hostname of the node\n"

  nodes = {}
  i = 1
  while i <= ask_nodes:
    print "Enter the hostname of node number ", i
    print "Please write all of them in the same format"
    node_fqdn = raw_input()
    nodes[i-1] = node_fqdn
    i += 1
  write_host_ocp(nodes,ask_nodes)

  print ("Running prerequisites for OCP 3.11 to be installed")

  os.system('ansible-playbook ocp3.yml --ask-vault-pass')

  print ("All the nodes are ready, please run your inventory file with ansible-playbook [-i /path/to/inventory] playbooks/deploy_cluster.yml")

else:
  print("You chosed IDM")
  
  #Ask for the node in which IDM will be installed
  hostname = raw_input("Enter the hostname of the IDM\n")
  write_host_idm(hostname)

  #Ask wether you want to subscribe the node or not
  ask_sub = raw_input("Do you want to subscribe the node?\n1-Yes\n2-No\n")
  if ask_sub == "1":
    sub = "true"
  else:
    sub = "false"

  #Ask wether you want integrated DNS in your IDM
  ask_dns = raw_input("Do you want to have integrated DNS in your IDM?\n1-Yes\n2-No\n") 
  if ask_dns == "1":
    dns = "true"
  else:
    dns = "false"
 
  #Ask wether you want auto reverse zone detection
  ask_reverse = raw_input("Do you want to have reverse zone auto detection)\n1-Yes\n2-No\n")
  if ask_reverse == "1":
    reverse = "true"
  else:
    reverse = "false"

  #Enter realm name
  realm = raw_input("Please enter the realm name\n")

  #Please enter the Directory Manager password
  dm_passwd = raw_input("Please enter the Directory Manager Password\n")
  
  #Please enter the IPA admin password
  ipa_passwd = raw_input("Please enter IPA admin password\n")

  #Do you want to enable ntp configuration?
  ask_ntp = raw_input("Do you want to enable ntp?\n1-Yes\n2-No\n")
  if ask_ntp == "1":
    ntp = "true"
  else:
    ntp = "false"
  
  #Do you want to enable auto forwarders?
  ask_forward = raw_input("Do you want to enable auto forwarders?\n1-Yes\n2-No\n")
  if ask_forward == "1":
    forward = "true"
  else:
    forward = "false"

  #Do you want to have an unattended installation?
  ask_unattended = raw_input("Do you want to have an unattended installation?\n1-Yes\n2-No\n")
  if ask_unattended == "1":
    unattended = "true"
  else:
    unattended = "false"
  
  set_vars_idm(sub,dns,reverse,realm,dm_passwd,ipa_passwd,ntp,forward,unattended)

  if sub == "true":
    os.system('ansible-playbook idm.yml --ask-vault-pass')
  else:
    os.system('ansible-playbook idm_no_sub.yml')

