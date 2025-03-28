

def my_api_call():
    for i in range(1, 5):
        yield i


records = my_api_call()

if not any(records):
    raise Exception

for record in records:
    print(record)
