<head>
    <title>Strichliste</title>
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">
    <link rel="stylesheet" type="text/css" href="/static/css/jkeyboard.css">

</head>
<body>
<h1>Neuen Benutzer erstellen</h1>
<form action="/new_user" method="post">
    Name<br>
    <input type="text" name="name" style="width:300px;height:50px" id="name" required> <br><br>
    <!--PIN<br>-->
    <!--<input type="text" name="pin"> <br><br>-->
    RFID<br>
    <input type="text" name="rfid" id="barcode" style="width:300px;height:50px" required> <br><br>
    <input type="submit" class="btn" style="height:100px;width:300px" value="Erstellen">
</form>

<div id="keyboard"></div>
<input class="btn" type="button" onclick="location.href='/'" value="Zurück">

<script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
<script src="/static/js/jkeyboard.js"></script>
<!--<script language="javascript" type="text/javascript" src="/static/js/barcode.js"></script>-->

<script>
    $('#keyboard').jkeyboard({
  layout: "english",
  input: $('#name')
});
</script>
</body>
</html>