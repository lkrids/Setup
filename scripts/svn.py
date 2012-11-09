import re, pprint, sys, datetime, os

svnRoot = ''

date = datetime.datetime.now()
datePrev = date-datetime.timedelta(days=1)
cur = "%s-%s-%s" %(date.year,date.month,date.day)
prev = "%s-%s-%s" %(datePrev.year,datePrev.month,datePrev.day)

prevFile = "data/"+prev+".txt"
exists = False
try:
  open(prevFile)
  exists = True
except IOError:
  pass

if not exists:
  com = "svn log ".svnRoot." --verbose -r{"+prev+"}:{"+cur+"} > "+prevFile
  print com
  os.system(com)

file = open(prevFile)

rev = re.compile(r'^r[0-9]', re.M)
splitRev = re.compile(r' \| ')
fileMark = re.compile(r'^   [A-Z] ', re.M)
fileSplit = re.compile(r'^([A-Z]) ', re.M)
begW = re.compile(r'^\s*', re.M)
endW = re.compile(r'\s*$', re.M)
project = re.compile(r'^(/[^/]*/[^/]*).*', re.M)

date = ''
user = ''
counts = 0
users = {}
files = {}
actions = {}
for line in file:
  if re.match(rev, line):
    p = re.split(splitRev, line)
    user = p[1]
    date = p[2]
    #print user+" "+date
    counts += 1
    if user in users:
      users[user] += 1
    else:
      users[user] = 1
  else:
    if re.match(fileMark, line):
      line = re.sub(begW, '', line)
      line = re.sub(endW, '', line)
      p = re.split(fileSplit, line)
      t = p[2]

      if not (user in files):
        files[user] = {}
      if not (t in files[user]):
        files[user][t] = 1
      else:
        files[user][t] += 1

#print "commits: %s" %counts
p = sorted(users.items(), key=lambda x: x[1])
for v in p:
  print "\n---------------------------------"
  print v
  print "---------------------------------"
  o = sorted(files[v[0]].items(), key=lambda x: x[0])
  for t in o:
    print t[0]

print "\ndate: "+prev+"\n"
