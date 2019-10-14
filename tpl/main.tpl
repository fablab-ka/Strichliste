<head>
    <title>Strichliste</title>
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">
</head>
<meta http-equiv="refresh" content="20" >
<body  >
<h1>Wer bist du?</h1>

<!--<form action="/cash" method="post">-->
    <!--<input type="submit" value="Ich zahle sofort" name="cash">-->
<!--</form>-->

<div class="box_container">
%for customer in customers:
<a href="/customer/{{customer.get_id()}}">
<div class="box">
    {{customer.name}}
</div>
</a>
%end
</div>
<input class="btn" style="width:400px" type="button" onclick="location.href='/create_customer'" value="Neuen Nutzer anlegen">

<!--<input type="button" onclick="location.href='/create_customer'" value="Neuen Benutzer anlegen">-->

<form action="/customer_barcode" method="post">
    <input style="display:none" id="barcode" type="text" name="barcode">
</form>
<script language="javascript" type="text/javascript" src="/static/js/barcode.js"></script>

</body>
</html>