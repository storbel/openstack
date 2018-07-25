#!/bin/python


import csv
import json
import os
import shade



import shade
shade.simple_logging(debug=True)
cloud = shade.openstack_cloud()





f = open('openstackreport.csv',"w")
csv_file = csv.writer(f)
f.write("List Aggregates\n")
csv_file.writerow(cloud.list_aggregates())
f.write("List Domains\n")
csv_file.writerow(cloud.list_domains())
f.write("List Endpoints\n")
csv_file.writerow(cloud.list_endpoints())
f.write("List Groups\n")
csv_file.writerow(cloud.list_groups())
f.write("List Keypairs\n")
csv_file.writerow(cloud.list_keypairs())
f.write("List Roles\n")
csv_file.writerow(cloud.list_roles())
f.write("List Services\n")
csv_file.writerow(cloud.list_services())
f.write("list Users\n")
csv_file.writerow(cloud.list_users())
f.write("List volumes\n")
csv_file.writerow(cloud.list_volumes())



f.close()


f=open('openstackreport.csv','r')

content=f.readlines()

for line in content:
  print line
