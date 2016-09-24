

script = """
data = context.portal_quickinstaller.listInstalledProducts()
return \"""<form action="http://localhost:8080/Plone/census/@@rapido/plonecensus/block/submit">
<textarea name="data">%s</textarea><input type="submit">
</form>\""" % data
"""
#from Products.PythonScripts.standard import html_quote

def script_quoted(context):
    """ return script quoted
    """
    return script



def top_plugins(context):
    html = "<ul>"
    for plugin in context.app.search("install_count>=0", sort_index="install_count", reverse=True):
        html += "<li><a href='../@rapido/view/plugin/{id}'>{name}</a></li>".format(
            id = plugin.id,
            name = plugin.id
        )
    return html

def show_request(context):
    return context.request