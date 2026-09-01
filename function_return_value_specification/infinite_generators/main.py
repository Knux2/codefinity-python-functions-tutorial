def id_generator():
    count = 1
    
    while True:
        yield f'ID_{count}'
        count += 1

id_gen = id_generator()

# Testing the result
for _ in range(5):
    unique_id = next(id_gen)
    print(unique_id)