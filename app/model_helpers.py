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

    # Read Headers
    html += "<th>"
    for header in lines[0].split(","):
        html += f"<td>{header}</td>"
    html += "</th>"


    for line in lines[1:]:
            html += "<tr>"
            for entry in line.split(','):
                html += f"<td>{entry}</td>"
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

