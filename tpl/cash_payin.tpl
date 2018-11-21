<head>
    <title>Strichliste</title>
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">

</head>
<body>
<h1>Hallo {{customer['name']}}, du willst Geld einzahlen</h1>
<h2>Dein Kontostand beträgt derzeit {{"{:.2f}".format(customer['credit'])}}</h2>
<form action="/cash_payin" method="post">
    Betrag:<br>
    <table>
        <tr>
            <td><input class="arr up" type="button" onclick='document.getElementById("1xx.xx").stepUp()'></td>
            <td><input class="arr up" type="button" onclick='document.getElementById("x1x.xx").stepUp()'></td>
            <td><input class="arr up" type="button" onclick='document.getElementById("xx1.xx").stepUp()'></td>
            <td></td>
            <td><input class="arr up" type="button" onclick='document.getElementById("xxx.1x").stepUp()'></td>
            <td><input class="arr up" type="button" onclick='document.getElementById("xxx.x1").stepUp()'></td>
            <td></td>
        </tr>
        <tr>
            <td><input class="num" type="number" value="0" min="0" max="9" id="1xx.xx" name="1xx.xx"></td>
            <td><input class="num" type="number" value="0" min="0" max="9" id="x1x.xx" name="x1x.xx"></td>
            <td><input class="num" type="number" value="0" min="0" max="9" id="xx1.xx" name="xx1.xx"></td>
            <td>.</td>
            <td><input class="num" type="number" value="0" min="0" max="9" id="xxx.1x" name="xxx.1x"></td>
            <td><input class="num" type="number" value="0" min="0" max="9" id="xxx.x1" name="xxx.x1"></td>
            <td>€</td>
        </tr>
        <tr>
            <td><input class="arr down" type="button" onclick='document.getElementById("1xx.xx").stepDown()'></td>
            <td><input class="arr down" type="button" onclick='document.getElementById("x1x.xx").stepDown()'></td>
            <td><input class="arr down" type="button" onclick='document.getElementById("xx1.xx").stepDown()'></td>
            <td></td>
            <td><input class="arr down" type="button" onclick='document.getElementById("xxx.1x").stepDown()'></td>
            <td><input class="arr down" type="button" onclick='document.getElementById("xxx.x1").stepDown()'></td>
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