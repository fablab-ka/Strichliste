<head>
    <title>Strichliste</title>
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">
</head>
<meta http-equiv="refresh" content="120" >
<body>
<h1>Hallo {{customer['name']}}, du willst Geld einzahlen</h1>
<h2>Dein Kontostand beträgt derzeit {{"{:.2f}".format(customer['credit'])}}</h2>
<form action="/cash_payin" method="post">
    Betrag:<br>
    <table>
        <tr>
            <td><input class="key up" type="button" onclick='document.getElementById("1xx.xx").stepUp()' value="▲"></td>
            <td><input class="key up" type="button" onclick='document.getElementById("x1x.xx").stepUp()' value="▲"></td>
            <td><input class="key up" type="button" onclick='document.getElementById("xx1.xx").stepUp()' value="▲"></td>
            <td></td>
        </tr>
        <tr>
            <td><input class="num" type="number" value="0" min="0" max="9" id="1xx.xx" name="1xx.xx" maxlength="1"></td>
            <td><input class="num" type="number" value="0" min="0" max="9" id="x1x.xx" name="x1x.xx" maxlength="1"></td>
            <td><input class="num" type="number" value="0" min="0" max="9" id="xx1.xx" name="xx1.xx" maxlength="1"></td>
            <td>€</td>
        </tr>
        <tr>
            <td><input class="key down" type="button" onclick='document.getElementById("1xx.xx").stepDown()' value="▼"></td>
            <td><input class="key down" type="button" onclick='document.getElementById("x1x.xx").stepDown()' value="▼"></td>
            <td><input class="key down" type="button" onclick='document.getElementById("xx1.xx").stepDown()' value="▼"></td>
            <td></td>
        </tr>
    </table>
    <br><br>

    <input type="submit" class="btn" style="height:100px;width:320px" value="Bargeld einzahlen">
    <input class="btn" type="button" onclick="location.href='/'" value="Zurück">

</form>

<div id="keyboard"></div>

</body>
</html>