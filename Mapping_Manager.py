from sqlalchemy.engine import create_engine
import sys


def category(para):

	engine = create_engine('sqlite:///mapping.db')
	connection = engine.connect()
	titler=para
	query = "SELECT Category FROM db WHERE OWASP_Testing_Guide_v3_num ='" + titler + "'"
	result = connection.execute(query)
	rendered = ""
	for row in result:
		rendered += row['Category']
	return rendered

def getcode():
    engine = create_engine('sqlite:///mapping.db')
    connection = engine.connect()
    query = "SELECT OWASP_Testing_Guide_v3_num FROM db"
    result=connection.execute(query)
    plugin_code=[]
    for row in result:
        plugin_code.append(row['OWASP_Testing_Guide_v3_num'])
    return plugin_code


