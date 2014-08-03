from sqlalchemy.engine import create_engine
import markdown
import json
import codecs
import re
import sys
from Mapping_Manager import category


def GetExp(plugin_code):
    engine = create_engine('sqlite:///VulnExp.db')
    connection = engine.connect()

    plugin_category = category(plugin_code)	

    query = "SELECT Desc FROM VulnExp WHERE Category ='" + plugin_category + "'"
    result = connection.execute(query)

    rendered = ""

    for row in result:
    	rendered += row['Desc']

    jsoner=json.loads(rendered)


    html = markdown.markdown(jsoner)

    return html
