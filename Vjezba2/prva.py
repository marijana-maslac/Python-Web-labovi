#!python

import cgi

print('''
      <!DOCTYPE html>
      <html>
      <head>
      <meta charset="UTF-8">
      </head>
      <body>
      <form action="druga.py" mehotd="post">
      <table style="padding: 1px; border: 1px solid black;">
      <tr>
      <td style="padding: 1px; border: 1px solid black;">Ime:</td>
      <td style="padding: 1px; border: 1px solid black;"><input type="text" name="ime" value="" required></td>
      </tr>
      <tr>
      <td style="padding: 1px; border: 1px solid black;">Lozinka:</td>
      <td style="padding: 1px; border: 1px solid black;"><input type="password" name="loz" value="" required></td>
      </tr>
      <tr>
      <td style="padding: 1px; border: 1px solid black;">Ponovi lozinku:</td>
      <td style="padding: 1px; border: 1px solid black;"><input type="password" name="ponoviLoz" value="" required></td>
      </tr>
      <tr>
      <td style="padding: 1px; border: 1px solid black;"><input type="submit" value="Next"></td>
      <td style="padding: 1px; border: 1px solid black;"></td>
      </tr>
      </table>
      </form>
      </body>
      </html>
      ''')

params = cgi.FieldStorage()
