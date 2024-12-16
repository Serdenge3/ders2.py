
import random

print("Rasgele Şifre Oluşturucu")
passwordlength = int(input(("Şifrenizi oluşturmak için bir input girin. "))) 


characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = random.choice (characters) + random.choice (characters) + random.choice (characters) + random.choice (characters) + random.choice (characters) + random.choice (characters) + random.choice (characters) + random.choice (characters) + random.choice (characters) + random.choice (characters)


print(f"Rasgele şifreniz: {password}")
