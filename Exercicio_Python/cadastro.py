login=input("Digite seu login: ")
senha=input("Digite sua senha: ")
if login=="adm" and senha=="123456":
    print("Digite:\np-Python\na-AI900\ne-Elétrica")
    op=input("Digite a opção: ")
    if op=="p" or op=="P":
        print("sala D21")
    elif op=="a" or op=="A":
        print("Sala C10")
    elif op=="e" or op=="E":
        print("Sala D30")
    else:
        print("Opção Inválida")          
else:
    print("Login ou Senha incorreto")