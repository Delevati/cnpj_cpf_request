def valida_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])

cpf_teste = "Numero_aqui"
if valida_cpf(cpf_teste):
    print("CPF válido.")
else:
    print("CPF inválido.")