def greet(first, *args):
    print(args)
    # return f"Hello, {first}{' and'*len(args)}!"
    # l = [" and" + x for x in args]
    print(args, end=" and")
    return f"Hello, {first}!"


#  ? задача - распаковать аргументы args,

print(greet("Timur"))
print(greet("Timur", "Roman"))
print(greet("Timur", "Roman", "Ruslan"))
