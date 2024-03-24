
#!/usr/bin/env python3

import csv, re

def contains_domain(address, domain):
  """Returns True if the email address contains the given domain,
    in the domain position, false if not."""
  if str(domain) in str(address):
    return True
  return False

def replace_domain(address, old_domain, new_domain):
  """Replaces the old domain with the new domain in
    the received address."""
  old_domain_pattern = r"" + old_domain + "$"
  address = re.sub(old_domain_pattern, new_domain, address)
  return address

def main():
  """Processes the list of emails, replacing any instances of the
    old domain with the new domain."""
  old_csv = "/home/student-01-b2a831267586/data/user_emails.csv"
  updated_csv = "/home/student-01-b2a831267586/data/updated_user_emails.csv"
  old_domain, new_domain = 'abc.edu', 'xyz.edu'
  with open(updated_csv, "w") as csv_writer:
    writer = csv.writer(csv_writer)
    with open(old_csv) as csv_content:
      read_csv = csv.reader(csv_content)
      for row in read_csv:
        name,  email = row
        if contains_domain(email, old_domain):
          email = replace_domain(email, old_domain, new_domain)
          writer.writerow([name, email])
        else:
          writer.writerow([name, email])

main()


# CSV File data
# Full Name, Email Address
# Blossom Gill, blossom@abc.edu
# Hayes Delgado, nonummy@utnisia.com
# Petra Jones, ac@abc.edu
# Oleg Noel, noel@liberomauris.ca
# Ahmed Miller, ahmed.miller@nequenonquam.co.uk
# Macaulay Douglas, mdouglas@abc.edu
# Aurora Grant, enim.non@abc.edu
# Madison Mcintosh, mcintosh@nisiaenean.net
# Montana Powell, montanap@semmagna.org
# Rogan Robinson, rr.robinson@abc.edu
# Simon Rivera, sri@abc.edu
# Benedict Pacheco, bpacheco@abc.edu
# Maisie Hendrix, mai.hendrix@abc.edu
# Xaviera Gould, xlg@utnisia.net
# Oren Rollins, oren@semmagna.com
# Flavia Santiago, flavia@utnisia.net
# Jackson Owens, jackowens@abc.edu
# Britanni Humphrey, britanni@ut.net
# Kirk Nixon, kirknixon@abc.edu
# Bree Campbell, breee@utnisia.net
