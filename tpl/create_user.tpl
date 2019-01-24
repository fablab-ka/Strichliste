<head>
    <title>Strichliste</title>
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">
    <link rel="stylesheet" type="text/css" href="/static/css/jkeyboard.css">

</head>
<body>
<h1>Neuen Benutzer erstellen</h1>
<form action="/new_user" method="post">
    <table>
        <tr>
            <td><h4>Name</h4></td>
            <td><h4>RFID</h4></td>
        </tr>
        <tr>
            <td><input type="text" name="name" style="width:300px;height:50px" id="name" required></td>
            <td><input type="text" name="rfid" id="barcode" style="width:300px;height:50px"></td>
        </tr>
        <tr>
            <td><input class="btn" type="button" onclick="location.href='/'" value="Zurück"></td>
            <td><input type="submit" class="btn" style="height:100px;width:300px" value="Erstellen"></td>
        </tr>
    </table>

</form>

<div id="keyboard"></div>


<script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
<!--<script language="javascript" type="text/javascript" src="/static/js/barcode.js"></script>-->


</body>
</html>