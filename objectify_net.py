import sys
import os

content = '//embeds.cs\n' \
          'using System;\n' \
          '\n' \
          'namespace Program {\n' \
          '\tpublic class Embeds {\n'

i = 1
for arg in sys.argv[1:]:
    file = open(arg, 'rb')
    file_bytes = list(file.read(os.path.getsize(arg)))
    file.close()

    content += '\t\tpublic static byte[] embedded_image_' + str(i) + ' = ' + str(file_bytes).replace('[', '{').replace(']', '}') + ';\n\n'
    i += 1

content += '\t}\n}\n'

output = open('embeds.cs', 'wb')
output.write(bytes(content, 'utf-8'))
output.close()
