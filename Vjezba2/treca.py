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
if params.getvalue("zavrsni") != None:
      zavrsni = 'Da'
else:
      zavrsni = 'Ne'
print('''
      <form action="zadnja.py" mehotd="post">
      <table style="padding: 1px; border: 1px solid black;">
      <tr>
      <td style="padding: 1px; border: 1px solid black;">Napomene: 
      </td>
      <td style="padding: 1px; border: 1px solid black;">
      <textarea name="napomena"></textarea>
      </td>
      </tr>
      ''')
print ('<input type="hidden" name="ime" value="' + params.getvalue("ime") + '">')
print ('<input type="hidden" name="status" value="' + params.getvalue("status") + '">')
print ('<input type="hidden" name="email" value="' + params.getvalue("email") + '">')
print ('<input type="hidden" name="smjer" value="' + params.getvalue("smjer") + '">')
print ('<input type="hidden" name="zavrsni" value="' + zavrsni + '">')
print('''
      <tr>
      <td style="padding: 1px; border: 1px solid black;"><input type="submit" value="Next"></td>
      <td style="padding: 1px; border: 1px solid black;"></td>
      </tr>
      </table>
      </form>
      </body>
      </html>
      ''')
