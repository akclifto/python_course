from password import Password

def main():
    ps = Password()
    password = ps.generate_pw()
    return password


password = main()
print(f"password: \n{password}")
