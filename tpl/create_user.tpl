<head>
    <title>Strichliste</title>
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">
    <link rel="stylesheet" type="text/css" href="/static/css/jkeyboard.css">

</head>
<body>
<h1>Neuen Benutzer erstellen</h1>
<form action="/new_user" method="post">
    <label for="name">Name</label>
    <td><input type="text" style="width:300px;height:50px" id="name" required><br>
    <label for="email">Email</label>
    <td><input type="email" id="email" style="width:300px;height:50px" required><br>
    <label for="PIN">PIN (optional)</label>
    <td><input type="password" patter="(0-9){4,}"id="pin" title="PIN" style="width:300px;height:50px"><br>
    <label for="name">RFID (optional)</label>
    <td><input type="text" id="barcode" style="width:300px;height:50px"><br>

    <td><input class="btn" type="button" onclick="location.href='/'" value="Zurück">
    <td><input type="submit" class="btn" style="height:100px;width:300px" value="Erstellen">
</form>

<div id="keyboard"></div>


<script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
<!--<script language="javascript" type="text/javascript" src="/static/js/barcode.js"></script>-->


</body>
</html>