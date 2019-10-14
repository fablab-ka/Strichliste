<head>
    <title>Strichliste</title>
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">
</head>
<meta http-equiv="refresh" content="200; URL=/">
<body>
<h1>Kauf bestätigen?</h1>

<ul>
    <li>
        Käufer: {{customer}}
    </li>

</ul>

<form action="/confirm">
    <input class="btn" type="submit" value="Bestätigen">
</form>
<form action="/">
    <input class="btn" type="submit" value="Abbrechen">
</form>



</body>
</html>