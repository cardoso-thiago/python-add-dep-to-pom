scope_test_text = '<scope>test</scope>'
dependency_text = '</dependency>'

line_to_insert = 0

with open(r"pom.xml", 'r') as fp:
    for line_number, line in enumerate(fp):
            if dependency_text in line:
                line_to_insert = line_number
            if scope_test_text in line:
                break

with open(r"pom.xml", 'r') as fp:
    file_lines = fp.readlines()

    dependency = '''\t\t</dependency>
\t\t<dependency>
\t\t\t<groupId>org.springframework.boot</groupId>
\t\t\t<artifactId>spring-boot-starter-logging</artifactId>
\t\t\t<version>2.6.8</artifactId>
\t\t</dependency>\n'''

    file_lines[line_to_insert] = dependency
    fp.close()

if line_to_insert != 0:
    with open('pom.xml', 'w') as fp:
        fp.writelines(file_lines)