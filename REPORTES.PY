import webbrowser as wb
class Reportes:
  def reporteUnaImagen(self,nombres,llenow):
    
    output = open("UNAIMAGEN.html","w",encoding="utf-8")
    output.write("""<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
    <title>Document</title>
    <style>
      p{
        position:absolute;
      }
      h1{
        text-align: center;
      }
      img{
        height: 1010px;
        width: 100%;
        position: absolute;
      }
      h3{
         position: relative;
      }
      table{
        position: relative;
      }
      h1{
        position: relative;
        color:red
      }
      #todo{
        width:70%;
        heigth:300px;
        position: relative;
        top: 40px;
        margin: auto;
        background: rgba(128, 128, 128, 0.486);
        padding-left: 100px;
        padding-right: 100px;
        padding-bottom:20px;

       }
      th{
        text-align: center;
      }
      #w{
        color:yellow
      }
      #to{
        margin-top:10px;
        
         background: rgb(0, 0, 0);

      }
      #to:hover{
             background:rgb(73, 73, 73);
      }
      </style>
    </head>
    <body>
    <img src="2.jpg" alt="">
    <div  id="todo">
    <h1 class="display-1">REPORTE UNA IMAGEN </h1>""")
    
    for letra2 in nombres.split(","):
     
      output.write("<h3>"+ letra2 + "</h3>"+"\n")
    
    output.write("<h3>"+ llenow + "</h3>"+"\n")
    output.write("""
    
    </div>
    </body>
    </html>""")
  def dosImagenes(self,nombres,llenow,llenow2):
    output = open("DOSIMAGENES.html","w",encoding="utf-8")
    output.write("""<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
    <title>Document</title>
    <style>
      p{
        position:absolute;
      }
      h1{
        text-align: center;
      }
      img{
        height: 1010px;
        width: 100%;
        position: absolute;
      }
      h3{
         position: relative;
      }
      table{
        position: relative;
      }
      h1{
        position: relative;
        color:red
      }
      #todo{
        width:90%;
        heigth:300px;
        position: relative;
        top: 40px;
        margin: auto;
        background: rgba(128, 128, 128, 0.486);
        padding-left: 100px;
        padding-right: 100px;
        padding-bottom:20px;

       }
      th{
        text-align: center;
      }
      #w{
        color:yellow
      }
      #to{
        margin-top:10px;
        
         background: rgb(0, 0, 0);

      }
      #to:hover{
             background:rgb(73, 73, 73);
      }
      </style>
    </head>
    <body>
    <img src="2.jpg" alt="">
    <div  id="todo">
    <h1 class="display-1">REPORTE DOS IMAGENES </h1>""")
    
    for letra2 in nombres.split("*"):
     
      output.write("<h3>"+ letra2 + "</h3>"+"\n")
    
    output.write("<h3>"+ llenow + "</h3>"+"\n")
    output.write("<h3>"+ llenow2 + "</h3>"+"\n")
    output.write("""
    
    </div>
    </body>
    </html>""")
  def errores(self,nombre,nombres3):
    output = open("errores.html","w",encoding="utf-8")
    output.write("""<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
    <title>Document</title>
    <style>
      p{
        position:absolute;
      }
      h1{
        text-align: center;
      }
      img{
        height: 1010px;
        width: 100%;
        position: absolute;
      }
      h3{
         position: relative;
      }
      table{
        position: relative;
      }
      h1{
        position: relative;
        color:red
      }
      #todo{
        width:90%;
        heigth:300px;
        position: relative;
        top: 40px;
        margin: auto;
        background: rgba(128, 128, 128, 0.486);
        padding-left: 100px;
        padding-right: 100px;
        padding-bottom:20px;

       }
      th{
        text-align: center;
      }
      #w{
        color:yellow
      }
      #to{
        margin-top:10px;
        
         background: rgb(0, 0, 0);

      }
      #to:hover{
             background:rgb(73, 73, 73);
      }
      </style>
    </head>
    <body>
    <img src="2.jpg" alt="">
    <div  id="todo">
    <h1 class="display-1">REPORTE ERRORES </h1>""")
    
    for letra2 in nombre.split(","):
     
      output.write("<h3>"+ letra2 + "</h3>"+"\n")
    for letra23 in nombres3.split(","):
     
      output.write("<h3>"+ letra23 + "</h3>"+"\n")
    
    output.write("""
    
    </div>
    </body>
    </html>""")
  def desplegar(self):
    wb.open_new("DOSIMAGENES.html")
    wb.open_new("UNAIMAGEN.html")
    wb.open_new("errores.html")

