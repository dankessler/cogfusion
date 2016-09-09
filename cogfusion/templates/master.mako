<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="${request.static_url('cogfusion:static/master.css')}">
    <title>Cogfusion</title>
  </head>

  <body>

        <p id="header">
            <a href="${request.route_url('home')}"><h1>Cogfusion</h1></a>
            <a href="${request.route_url('contrasts')}">contrasts</a>
        </p>

        ${self.body()}

  </body>
</html>
