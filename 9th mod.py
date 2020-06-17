def example(*others):
    x = []
    x = others
    for i in reversed(x):
        print(i)
print(example(1, 2, 3, 4))

def decorate(func):
    def wrapper_func(*args):
        return_value = func(*args)
        return "<html>{}<html>".format(return_value)
    return wrapper_func

@decorate
def myfunction(arg):
    return arg

print(myfunction("Testi"))

# Практическое задание - переделать 6 и 7 пр. зад в функции

def lowering(arg):
    lowered = str(arg.lower())
    return lowered

def translating(arg):
    punct = str.maketrans(".,?!:;-", "       ")
    translated = arg.translate(punct)
    return translated

def splitting(arg):
     splitted = arg.split()
     return splitted

def joining(arg):
     joined = "\n".join(arg)
     return joined

with open('C:\\Users\\Student\\Desktop\\moby_01.txt', encoding='UTF8') as infile, open(
                "C:\\Users\\Student\\Desktop\\moby_01_clean.txt", "w") as outfile:
    for arg in infile:
        lowered = lowering(arg)
        translated = translating(lowered)
        splitted = splitting(translated)
        joined = joining(splitted)
        outfile.write(joined)

