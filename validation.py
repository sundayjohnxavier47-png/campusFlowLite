def get_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This can not be empty")