import re
import os

'''
Parse Xueyuan's human readable assertions
'''

dirname = os.path.abspath('functional/lighttpd-bug-2661-2662/buggy.2661')
example_str = 'src/mod_accesslog.c, before line 169(buffer_prepare_append(dest, str->used - 1);), assert(!(str->used == 0));'

assertion = example_str
m = re.match(r'([^,]+),\s*(before|after)\s*line\s*([0-9]+).*(assert\(.*\);)', assertion)
file_path = os.path.join(dirname, m.group(1))
before_after = m.group(2)
line_no = m.group(3)
assert_stmt = m.group(4)
assert_stmt = assert_stmt.replace('assert', '''#define my_assert(c) if (c) {} else{*((int*)0) = 0;}
my_assert''')

print(before_after, f'{file_path}:{line_no}')
print()
print(assert_stmt)
