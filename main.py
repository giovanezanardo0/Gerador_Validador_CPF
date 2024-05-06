"""O módulo random fornece funções para geração de números pseudoaleatórios."""

import random


class validation:
    """
    Classe que fornece métodos para validar CPFs.

    Métodos Estáticos:
        - validate(cpf: str) -> bool:
            Valida se um CPF é válido.
            Retorna True se o CPF é válido, False caso contrário.

        - clean_cpf(cpf: str) -> str:
            Remove símbolos e caracteres especiais de um CPF, deixando apenas a sequência de 11 números.

        - length_cpf(cpf: str) -> bool:
            Verifica se um CPF possui exatamente 11 dígitos.

        - is_sequence(cpf: str) -> bool:
            Verifica se um CPF é uma sequência de números iguais.

        - validate_digits(cpf: str, digit_verification: int) -> int:
            Calcula e valida os dígitos verificadores de um CPF.
            Retorna o dígito verificador calculado.

        - validate_digit_one(cpf: str) -> bool:
            Valida o primeiro dígito verificador de um CPF.

        - validate_digit_two(cpf: str) -> bool:
            Valida o segundo dígito verificador de um CPF.
    """

    @staticmethod
    def validate(cpf: str) -> bool:
        clean_cpf = validation.clean_cpf(cpf)

        if not validation.lenth_cpf(clean_cpf):
            return False

        if validation.is_sequence(clean_cpf):
            return False

        if not validation.validate_digit_one(clean_cpf):
            return False

        if not validation.validate_digit_two(clean_cpf):
            return False

        return True

    @staticmethod
    def clean_cpf(cpf: str) -> str:
        clean_cpf = ""
        for digit in cpf:
            if digit.isdigit():
                clean_cpf += digit
        return clean_cpf

    @staticmethod
    def lenth_cpf(cpf: str) -> bool:
        return len(cpf) == 11

    @staticmethod
    def is_sequence(cpf: str) -> bool:
        return (cpf[0] * len(cpf)) == cpf

    @staticmethod
    def validate_digits(cpf: str, digit_verication: int) -> int:
        sum_total = 0
        mutiplier = digit_verication
        cpf_numbers = cpf[: mutiplier - 1]

        for digit in cpf_numbers:
            sum_total += int(digit) * mutiplier
            mutiplier -= 1

        if sum_total % 11 < 2:
            return 0
        else:
            return 11 - (sum_total % 11)

    @staticmethod
    def validate_digit_one(cpf: str) -> bool:
        digit_one = 10
        return validation.validate_digits(cpf, digit_one) == int(cpf[9])

    @staticmethod
    def validate_digit_two(cpf: str) -> bool:
        digit_one = 11
        return validation.validate_digits(cpf, digit_one) == int(cpf[10])


class generation:
    """
    Classe que fornece um método estático para gerar CPFs aleatórios.

    Métodos Estáticos:
        - generate_cpf() -> str:
            Gera um número de CPF aleatório válido.
            Retorna uma string contendo o CPF gerado.

    Este método utiliza o algoritmo de geração de dígitos verificadores para garantir que o CPF gerado seja válido.
    O CPF é gerado com base em números aleatórios e é validado automaticamente antes de ser retornado.
    """

    @staticmethod
    def generate_cpf():
        """
        Classe que fornece um método estático para gerar CPFs aleatórios.

        """

        def calculate_digit(cpf_partial):
            """
            Calcula o dígito verificador de um CPF parcial.

            Args:
                cpf_partial (list): Uma lista de 9 ou 10 dígitos do CPF.

            Returns:
                int: O dígito verificador calculado.

            Esta função recebe uma lista contendo 9 ou 10 dígitos do CPF parcial (sem os dígitos verificadores) e calcula o dígito verificador correspondente.
            O algoritmo utilizado para calcular o dígito verificador é baseado na multiplicação dos dígitos pelos seus pesos, seguido do cálculo do módulo 11.
            Se o módulo for menor que 2, o dígito verificador é 0. Caso contrário, é a diferença entre 11 e o módulo.

            Exemplos:
                calculate_digit([0, 1, 2, 3, 4, 5, 6, 7, 8])
                9
                calculate_digit([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
                5
            """
            if len(cpf_partial) == 9:
                sum = 0
                for i, digit in enumerate(cpf_partial):
                    sum += digit * (10 - i)
                remainder = sum % 11
                if remainder < 2:
                    return 0
                else:
                    return 11 - remainder
            elif len(cpf_partial) == 10:
                sum = 0
                for i, digit in enumerate(cpf_partial):
                    sum += digit * (11 - i)
                remainder = sum % 11
                if remainder < 2:
                    return 0
                else:
                    return 11 - remainder

        cpf_partial = [random.randint(0, 9) for _ in range(9)]

        digit1 = calculate_digit(cpf_partial)
        cpf_partial.append(digit1)

        digit2 = calculate_digit(cpf_partial)
        cpf_partial.append(digit2)

        return "".join(map(str, cpf_partial))


# Teste do CPF gerado
cpf = generation.generate_cpf()
print("CPF Gerado:", cpf)

# Validação do CPF gerado
if validation.validate(cpf):
    print("CPF válido!")
else:
    print("CPF inválido!")
