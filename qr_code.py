import qrcode

phone_number = int(input("enter your phone number? "))
name = input("enter your name: ")


img = qrcode.make(phone_number+name)
img.save("phone_number.png")
