<head>
    <title>Strichliste</title>
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">

</head>
<body>
<h1>Hallo {{customer['name']}}, du willst Geld einzahlen</h1>
<h2>Dein Kontostand beträgt derzeit {{"{:.2f}".format(customer['credit'])}}</h2>
<form action="/cash_payin" method="post">
    Betrag:<br>
    <input type="number" min="0" max="9" id="1xx.xx"
    <input type="text" name="name" style="width:300px;height:50px" id="name" required> <br><br>
    <input type="submit" class="btn" style="height:100px;width:300px" value="Bargeld einzahlen">
</form>

<div id="keyboard"></div>
<input class="btn" type="button" onclick="location.href='/'" value="Zurück">

</body>
</html>