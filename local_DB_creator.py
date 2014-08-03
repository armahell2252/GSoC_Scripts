#local SQLAlchemy DB creator

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


VulnBase = declarative_base()

class descriptions(VulnBase):
	__tablename__ = 'VulnExp'
	Title = Column(String, primary_key=True)
	Desc = Column(String)
	Category=Column(String)

engine = create_engine('sqlite:///VulnExp.db')
session = sessionmaker()
session.configure(bind = engine)
VulnBase.metadata.create_all(engine)

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
		vuln = {'Title': titler, 'Description':texto }
	vuln_desc = json.dumps(texto)
    	obj = descriptions(Title = vuln['Title'],Desc=vuln_desc,Category=lock)
	s.add(obj)
	s.commit()
	text=""
	line=""
	titler=""
	texto=""
	lock=""
