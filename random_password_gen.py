import random
import string

pass_len = int(input("Enter Password Length: "))

alpha_len = pass_len // 2
num_len = (pass_len * 3 + 9) // 10      # Equivalent to ceil(30%)
special_len = pass_len - alpha_len - num_len

password = []

password.extend(random.choices(string.ascii_letters, k=alpha_len))
password.extend(random.choices(string.digits, k=num_len))
password.extend(random.choices("@#$%&*", k=special_len))

random.shuffle(password)

print("".join(password))