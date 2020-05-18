import os
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

def inst_file(name,passwd,org,loc):
  with open('roles/satellite/files/satellite-installer.sh', 'r') as file:
    data = file.readlines()
    data[2] = "--foreman-initial-organization " + org +" \\ \n"
    data[3] = "--foreman-initial-location " + loc +" \\ \n"
    data[4] = "--foreman-initial-admin-username " + name +" \\ \n"
    data[5] = "--foreman-initial-admin-password " + passwd +"\n"
  with open('roles/satellite/files/satellite-installer-automated.sh', 'w') as file:
    file.writelines( data )

def set_vars(version,parted,sub):
  with open('roles/satellite/vars/main.yml', 'r') as file:
    data = file.readlines()
    data[1] = "version: " + version +"\n"
    data[2] = "parted: " + parted +"\n"
    data[3] = "sub: " + sub + "\n"
  with open('roles/satellite/vars/main.yml', 'w') as file:
    file.writelines( data )

product = input("Which product would you like to choose?\n1-Satellite\n2-Tower\n3-OCP\n4-IDM\n")
if product == 1:
  print("You chosed Satellite")
  action = input("Which action would you like to take?\n1-Satellite installation\n2-Capsule Installation \n3-Satellite Upgrade \n4-Capsule Upgrade\n")
  if action == 1:
    print("You chosed Satellite installation\n")
    hostname = raw_input("Enter the hostname of the Satellite\n")  
    write_host(hostname)
    ask_version = raw_input("Enter the version of Satellite you would like to install\n1-6.6\n2-6.7\n")
    if ask_version == 1:
      version = "6.6"
    else:
      version = "6.7"
    ask_parted = raw_input("Do you want to make partitions for /dev/vdb and /dev/vdc?\n(Recommended for quicklab installations)\n1-Yes\n2-No\n")
    if ask_parted == 1:
      parted = "true"
    else:
      parted = "false"
    ask_sub= raw_input("Do you want to subscribe the node?\n1-Yes\n2-No\n")
    if ask_sub == 1:
      sub = "true"
    else:
      sub = "false"
    set_vars(version,parted,sub)
    name = raw_input("Enter the admin user name\n")
    passwd = raw_input("Enter the password of the admin\n")
    org = raw_input("Enter Organization name\n")
    loc = raw_input("Enter Location name\n")
    inst_file(name,passwd,org,loc)
    os.system('ansible-playbook satellite.yml --ask-vault-pass')
  elif action == 2:
    print("You chosed Capsule Installation")
  elif action == 3:
    print("You chosed Satellite Upgrade")
  else:
    print("You chosed Capsule Upgrade")
elif product == 2:
  print("You chosed Tower")
elif product == 3:
  print("You chosed OCP")
else:
  print("You chosed IDM")
