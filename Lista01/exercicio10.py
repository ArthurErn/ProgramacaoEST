print("==== Teste de Formatação de Strings ====")

myInt = 12345
myFloat = 3.14159
myString = "Curso de Python"

print("Integer: ", myInt)

print("Decimal %d e um integer %d" %(myInt, myInt))

print("Integer Hexadecimal %x" %myInt)

print("Float", myFloat)

print("Default %f", myFloat)

print("Exponencial %e" %myFloat)

print("Justify Right (%10d)" % myFloat)

print("Justify Left (%-10d)" %myFloat)

print("Form 9 digits %.9d" %myInt)

print("Form 3 digits after decimal point %.3f" % myFloat)

print("Ten and five numbers allowed in the string:")

print("(%.10s) (%.5s)" % (myString, myString))

