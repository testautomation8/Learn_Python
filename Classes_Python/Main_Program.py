from Classes_Python import Class_Demo

iOS = Class_Demo.Phone("iPhone", "8s")
Android = Class_Demo.Phone("Samsung","Note9")

print("The type of phone is " + iOS.gettype())
print("The model of phone is " + iOS.getmodel())
print(iOS)
print(isinstance(iOS, Class_Demo.Phone))

print("The type of phone is " + Android.gettype())
print("The model of phone is " + Android.getmodel())
print(Android)
print(isinstance(Android, Class_Demo.Phone))