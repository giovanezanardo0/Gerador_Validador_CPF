# Gerador e Validador de CPF

Este é um projeto Python que oferece funcionalidades para validar e gerar números de CPFs (Cadastro de Pessoas Físicas).

## Requisitos

- Python 3.x instalado.

## Como Utilizar:

### Validação de CPFs

Para validar um CPF, você pode utilizar o método `validate` da classe `validation`. Este método retorna `True` se o CPF fornecido for válido e `False` caso contrário.

```python
from validation import validation

cpf = "123.456.789-09"

if validation.validate(cpf):
print("CPF válido!")
else:
print("CPF inválido!")
```
### Geração de CPFs Aleatórios

Para gerar um CPF aleatório, você pode utilizar o método generate_cpf da classe generation. Este método retorna uma string contendo um CPF válido.

```python
from generation import generation

cpf_aleatorio = generation.generate_cpf()
print("CPF Aleatório Gerado:", cpf_aleatorio)
```
## Descrição das Classes e Métodos

### Classe validation

Esta classe fornece métodos estáticos para validar CPFs.

validate(cpf: str) -> bool: Valida se um CPF é válido.

clean_cpf(cpf: str) -> str: Remove símbolos e caracteres especiais de um CPF.

length_cpf(cpf: str) -> bool: Verifica se um CPF possui 11 dígitos.

is_sequence(cpf: str) -> bool: Verifica se um CPF é uma sequência de números iguais.

validate_digit_one(cpf: str) -> bool: Valida o primeiro dígito verificador de um CPF.

validate_digit_two(cpf: str) -> bool: Valida o segundo dígito verificador de um CPF.


### Classe generation

Esta classe fornece um método estático para gerar CPFs aleatórios.

generate_cpf() -> str: Gera um número de CPF aleatório válido.

## Autor

Este módulo foi desenvolvido por Giovane Aparecido Zanardo.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
