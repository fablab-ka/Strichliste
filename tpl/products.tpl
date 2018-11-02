<head>
    <title>Strichliste</title>
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">

</head>
<meta http-equiv="refresh" content="20; URL=/">
<body>

<h1>Hallo {{customer['name']}}, dein Kontostand beträgt {{"{:.2f}".format(customer['credit'])}}€</h1>
<h1>Was willst du? kaufen</h1>
<div class="box_container">
%for product in products:
<a href="/product/{{product['id']}}">
<div class="box">
    {{product['name']}}
    <br>
    {{"{:.2f}".format(product['price'])}}€
</div>
</a>
%end
</div>

<input class="btn" type="button"" onclick="location.href='/'" value="Zurück">


<form action="/product_barcode" method="post">
    <input style="display:none" id="barcode" type="number" name="barcode">
</form>
<script language="javascript" type="text/javascript" src="/static/js/barcode.js"></script>


</body>
</html>