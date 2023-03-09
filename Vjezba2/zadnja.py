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

print('''
      <form action="zadnja.py" mehotd="post">
      <table style="padding: 1px; border: 1px solid black;">
      <tr>
      <td style="padding: 1px; border: 1px solid black;"colspan="2"><b>Uneseni podaci: </b>
      </td>
      <td></td>
      </tr>
      <tr>
      <td style="padding: 1px; border: 1px solid black;">Ime:
      </td>
      <td style="padding: 1px; border: 1px solid black;">''')
print(params.getvalue('ime') )
print('''</td>
      </tr>
      <tr>
      <td style="padding: 1px; border: 1px solid black;">E-mail:
      </td>
      <td style="padding: 1px; border: 1px solid black;">''')
print(params.getvalue('email'))
print('''</td>
      </tr>
      <tr>
      <td style="padding: 1px; border: 1px solid black;">Status:
      </td>
      <td style="padding: 1px; border: 1px solid black;">''')
print(params.getvalue('status'))
print('''</td>
      </tr>
      <tr>
      <td style="padding: 1px; border: 1px solid black;">Smjer:
      </td>
      <td style="padding: 1px; border: 1px solid black;">''')
print(params.getvalue('smjer'))
print('''</td>
      </tr>
      <tr>
      <td style="padding: 1px; border: 1px solid black;">Zavrsni rad:
      </td>
      <td style="padding: 1px; border: 1px solid black;">''')
print(params.getvalue('zavrsni')) 
print('''</td>
      </tr>
      <tr>
      <td style="padding: 1px; border: 1px solid black;">Napomene:
      </td>
      <td style="padding: 1px; border: 1px solid black;">''')
print(params.getvalue('napomena'))
print('''</td>
      </tr>
      </table>
      </form>
      <a href="prva.py">Na pocetak</a>''')
print('''
      </body>
      </html>
      ''')