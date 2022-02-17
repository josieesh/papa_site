import re

def get_csv(file_content):
    first = re.sub(r'[\s\n]{1,}([0-9]{1,2})[.][\s]{1,}', r'\n\g<1>,', file_content)

    second = re.sub(r'[\s]{2,}', ',', first)

    third = re.sub(r'\t', ',', second)
    return third

# **************
# TABLE CREATION
# **************

def create_or_recreate_object_html(obj_type, instance):
    old = obj_type.objects.filter(pk=getattr(instance, "id", None)).first()
    if instance.is_html and instance.text and ((old and instance.text != old.text) or not old):
        # Recreate or create brand new html
        instance.text = create_html_table(instance.text)

def create_html_table(plaintext):
    csv = get_csv(plaintext)
    lines = csv.splitlines()

    html = """
    <style>
        table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
        }

        td, th {
        border: 1px solid #dddddd;
        text-align: center;
        padding: 8px;
        }

        tr:nth-child(even) {
        background-color: #dddddd;
        }
    </style>
    <table>
    """
    headers = lines[0].split(",")
    rows = lines[1:]

    # Read Headers
    html += "<th>"
    # Special case is where the table has headers that span multiple columns
    special_case = False 
    if len(headers) == 3:
        special_case = True
        html += "<td></td>"
    for header in headers:
        html += "<td"
        if special_case:
            html += " colspan=\"5\""
        html += f">{header}</td>"
    html += "</th>"


    for row in rows:
        html += "<tr>"
        entries = row.split(',')
        entry = ""
        for i in range(len(entries)):
            entry += entries[i]
            if entry[len(entry)-1] != ":":
                html += f"<td>{entry}</td>"
                entry = ""

            
        html += "</tr>\n"

    html += "</table>"
    return html
    


# ****************
# OPTIONAL STYLING
# ****************

# <style>
# table {
#   font-family: arial, sans-serif;
#   border-collapse: collapse;
#   width: 100%;
# }

# td, th {
#   border: 1px solid #dddddd;
#   text-align: left;
#   padding: 8px;
# }

# tr:nth-child(even) {
#   background-color: #dddddd;
# }
# </style>

