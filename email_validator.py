import re

re_pattern = r'^[a-zA-Z0-9_-]+@{1}[a-zA-Z0-9]*\.[a-zA-Z]{1,3}$'

test_string = [
    'madspank666@gmail.com', 
    'itsme@gmail',
    '@something',
    '@something.com',
    '@something.co1',
    'sone.com'
]
for email in test_string:
    try:
        print('success' if re.match(re_pattern, email) else 'failure')
    except Exception as e:
        print(e)






