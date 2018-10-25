<head>
    <title>Strichliste</title>
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">
</head>
<meta http-equiv="refresh" content="20; URL=/">
<body>
<h1>Kauf bestätigen?</h1>
<ul>
    <li>
        Käufer: {{customer['name']}}
    </li>
    <li>
        Produkt: {{product['name']}}
    </li>
</ul>

<form action="/confirm">
    <input class="btn" type="submit" style="height:200px;width:200px" value="Bestätigen">
</form>
<form action="/">
    <input class="btn" type="submit"style="height:200px;width:200px" value="Abbrechen">
</form>



</body>
</html>