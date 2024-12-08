f = open("index.html", "w")
f.write(
    """
<!DOCTYPE html>
<html>
<head>
<title>Kennzeichen</title>
<meta charset='utf-8'/>
<meta name='noindex' content='noindex'/>
    <style>
        * {
            padding: 0;
            margin: 0;
            box-sizing: border-box;
        }
        html {
            width: 100vw;
            height: 100vh;
            font-family: serif;
        }
        body {
            color: ghostwhite;
            background: black;
            width: 100%;
            height: 100%;
        }
	</style>
</head>
<body>
<table>
<thead>
<tr>
<th>Abkürzung</th>
<th>Stadt / Landkreis</th>
</tr>
</thead>
<tbody>
"""
)
with open("data.csv", "r") as csv:
    for l in csv:
        split = l.split(",", 1)
        abk = split[0].strip()
        stadt = split[1].strip()
        f.write("<tr>")
        f.write("<td>{}</td>".format(abk))
        f.write("<td>{}</td>".format(stadt))
        f.write("</tr>\n")
f.write(
    """
</tbody>
</table>
</body>
</html>
"""
)
f.close()
