print("=" * 60)
print("EXERCICIO 4 - Validacao de Alfabeto")
print("=" * 60)

def validar_alfabeto(alfabeto, frase):
   """
   Verifica se todos os caracteres da frase pertencem ao alfabeto.
   Usa operacao de SUBCONJUNTO (<=) e DIFERENCA (-).
   """
   caracteres_frase = set(frase)

   print(f"\n  Alfabeto = {sorted(alfabeto)}")
   print(f"  Frase: \"{frase}\"")
   print(f"  Caracteres encontrados: {sorted(caracteres_frase)}")

   if caracteres_frase <= alfabeto:
       print("  String VALIDA! Todos os caracteres pertencem ao alfabeto")
       return True
   else:
       invalidos = caracteres_frase - alfabeto
       print(f"  String INVALIDA! Caracteres fora do alfabeto: {sorted(invalidos)}")
       return False

print("\n--- Teste 1: Alfabeto binario ---")
sigma_binario = {'0', '1'}
validar_alfabeto(sigma_binario, "10101")
validar_alfabeto(sigma_binario, "10102")

print("\n--- Teste 2: Letras minusculas (com espaco) ---")
sigma_minusculas = set("abcdefghijklmnopqrstuvwxyz ")
validar_alfabeto(sigma_minusculas, "hello world")
validar_alfabeto(sigma_minusculas, "Hello World!")

print("\n--- Teste 3: Alfabeto hexadecimal ---")
sigma_hex = set("0123456789ABCDEFabcdef")
validar_alfabeto(sigma_hex, "1A3F")
validar_alfabeto(sigma_hex, "1A3G")