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






Base = declarative_base()

class mappings(Base):
	__tablename__ = 'db'
	OWASP_Testing_Guide_v3_num = Column(String, primary_key=True)
	OWASP_Testing_Guide_v3_Test_Names= Column(String)
	OWASP_Testing_Guide_v4_num=Column(String)
	OWASP_Testing_Guide_v4_Test_Names=Column(String)
	NIST_control=Column(String)
	Category=Column(String)


	
engine = create_engine('sqlite:///mapping.db')
session = sessionmaker()
session.configure(bind = engine)
Base.metadata.create_all(engine)

s = session()


texto=""
titler=""


inp=codecs.open("mappings.txt",mode="r")
i=1
tect=inp.readlines()
for line in tect:

	titler=line.strip();
	titler2=titler.split(",")
	for k in range(0,6):
		if titler2[k]=="x":
			titler2[k]="Not Applicable"
	obj = mappings(OWASP_Testing_Guide_v3_num = titler2[0],OWASP_Testing_Guide_v3_Test_Names=titler2[1],OWASP_Testing_Guide_v4_num=titler2[2],OWASP_Testing_Guide_v4_Test_Names=titler2[3],NIST_control=titler2[4],Category=titler2[5])
	s.add(obj)
	s.commit()
	text=""
	line=""
	titler=""






