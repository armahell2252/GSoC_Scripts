import base64
import json
import urllib2
import sys
import glob
import os
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import codecs
import subprocess


k=""
ink = codecs.open('commit-hash',mode='r')
hash=ink.readlines()
for ln in hash:
	k+=ln

se_hash=""
p = subprocess.Popen("git ls-remote https://github.com/lucif3rr/Python_Exploits.git | grep HEAD | awk '{print $1}' ", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

for line in p.stdout.readlines():

    se_hash+=line

retval = p.wait()

if se_hash!=k:

	
	os.remove('commit-hash')
	file=codecs.open('commit-hash','w')
	file.write(se_hash)
	file.close	

	
	GITHUB_REPOS_API_BASE_URL = 'https://api.github.com/repos/'

	def write_file(item, dir_name):
	    name = item['name']
	    res = urllib2.urlopen(item['url']).read()
	    coded_string = json.loads(res)['content']
	    contents = base64.b64decode(coded_string)
	    print os.path.join(dir_name, name)
	    f = open(os.path.join(dir_name, name), 'w')
	    f.write(contents)
	    f.close()

	def write_files(url, dir_name, recursive=True):

	    print 'url', url
	    os.makedirs(dir_name)
	    github_dir = json.loads(urllib2.urlopen(url).read())
	    for item in github_dir:
	        if item['type'] == 'file':
	            write_file(item, dir_name)
	        elif item['type'] == 'dir':
	            write_files(item['url'], dir_name=os.path.join(dir_name, item['name']))


	if __name__ == '__main__':
	    args = dict(enumerate(sys.argv))
	    path = 'mfbx9da4/blog/server'
	    path = 'lucif3rr/lucif3rr.github.io/Templates/_posts'
	    path = path.split('/')

	    new_dir_name = path[-1]
	    if os.path.exists(new_dir_name):
	        raise 'Directory', new_dir_name, 'already exists'

	    # use contents api
	    path.insert(2, 'contents')
	    path = '/'.join(path)

	    recursive = eval(args.get(2)) if args.get(2) else True
	    write_files(GITHUB_REPOS_API_BASE_URL + path, new_dir_name, recursive=recursive)



	ExpBase = declarative_base()

	class VulnExp(ExpBase):
		__tablename__ = 'VulnExp'
		Title = Column(String, primary_key=True)
		Desc = Column(String)
		Category=Column(String)

	engine = create_engine('sqlite:///VulnExp.db')
	session = sessionmaker()
	session.configure(bind = engine)
	ExpBase.metadata.create_all(engine)

	s = session()

	texto=""
	titler=""

	os.chdir("_posts")
	for file in glob.glob("*.md"):
		inp=codecs.open(file,mode="r")
		i=1
		tect=inp.readlines()
		for line in tect:
			if i==2:
				lock=line.strip()
			if i==7:
 	        		titler=line.strip()
	        	if i>=9:
	        		texto+=line
			i=i+1

		vuln = {'Title': titler, 'Desc':texto }
		vuln_desc = json.dumps(texto)
	    	obj = VulnExp(Title = vuln['Title'],Desc=vuln_desc,Category=lock)
		s.add(obj)
		s.commit()
		text=""
		line=""
		titler=""
		texto=""


else:
	print("No update necessary")
