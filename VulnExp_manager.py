from sqlalchemy.engine import create_engine
import markdown
import json
import codecs
import re
import sys

def GetExp(plugin_code):
    engine = create_engine('sqlite:///owtf.db')
    connection = engine.connect()


    titles="Title: C-Based Toolchain Hardening"
    args = dict(enumerate(sys.argv))
    titles=args[1]

    query = "SELECT exp FROM db WHERE Title ='" + titles + "'"
    result = connection.execute(query)

    rendered = ""

    for row in result:
    	rendered += row['exp']

    jsoner=json.loads(rendered)


    html = markdown.markdown(jsoner)
    #output_file.write(html)
    connection.close()
