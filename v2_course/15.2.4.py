def greet(first, *args):
    print(args)
    # return f"Hello, {first}{' and'*len(args)}!"
    # l = [" and" + x for x in args]
    print(args, end=" and")
    return f"Hello, {first}!"


# {'and '+args(next)}
# Hello, Timur and Roman and Ruslan!
#  ? задача - распаковать аргументы args,

print(greet("Timur"))
print(greet("Timur", "Roman"))
print(greet("Timur", "Roman", "Ruslan"))
