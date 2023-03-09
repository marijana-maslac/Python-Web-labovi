#!python

import cgi

params = cgi.FieldStorage()



print('''
      <!DOCTYPE html>
      <html>
      <head>
      <meta charset="UTF-8">
      </head>
      <body>''')

if params.getvalue("loz") == params.getvalue("ponoviLoz"):
  print('''
    <form action="treca.py" mehotd="post">
    <table style="padding: 1px; border: 1px solid black;">
    <tr>
        <td style="padding: 1px; border: 1px solid black;">Status:</td>
        <td style="padding: 1px; border: 1px solid black;">Redovan:
        <input type="radio" name="status" value="redovan" checked> Izvanredan:
        <input type="radio" name="status" value="izvanredan">
        </td>
      </tr>
      <tr>
        <td style="padding: 1px; border: 1px solid black;">E-mail: 
        </td>
        <td style="padding: 1px; border: 1px solid black;">
        <input type="mail" name="email" value="" required>
        </td>
      </tr>
      <tr>
        <td style="padding: 1px; border: 1px solid black;">Smjer:
        </td>
        <td style="padding: 1px; border: 1px solid black;">
        <select id="smjer" name="smjer" style="width: 80%;">
            <option value="Baze podataka">Baze podataka</option>
            <option value="Programiranje">Programiranje</option>
            <option value="Racunalne mreze">Racunalne mreze</option>
        </select>
        </td>
      </tr>
      <tr>
        <td style="padding: 1px; border: 1px solid black;">Zavrsni:
        </td>
        <td style="padding: 1px; border: 1px solid black;">
        <input type="checkbox" name="zavrsni" value="da">
        </td>
      </tr>

      ''')
  print('<input type="hidden" name="ime" value="'+ params.getvalue('ime')+'">')
  print('''      
    <tr>
      <td style="padding: 1px; border: 1px solid black;"><input type="submit" value="Next"></td>
      <td style="padding: 1px; border: 1px solid black;"></td>
      </tr>
      </table>
      </form>
    ''')
else:
  print("Lozinka nije ispravna, pokusajte ponovno.")
  print(''' <br>
      <a href="prva.py">Pokusaj opet</a>
      ''')
print('''</body>
         </html>
         ''') 
