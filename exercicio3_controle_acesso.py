RH = {"ver_salario", "editar_perfil"}
TI = {"acesso_servidor", "editar_perfil"}

print("=" * 60)
print("EXERCICIO 3 - Controle de Acesso e Permissoes")
print("=" * 60)

print(f"\nPermissoes RH: {RH}")
print(f"Permissoes TI: {TI}")

def permissoes_acumuladas(cargo1, cargo2):
   """Retorna a uniao das permissoes de dois cargos."""
   return cargo1 | cargo2

total_permissoes = permissoes_acumuladas(RH, TI)
print(f"\nPermissoes totais (RH uniao TI):")
print(f"  {total_permissoes}")

permissoes_arquivo_confidencial = {"ver_salario", "acesso_servidor", "editar_perfil"}

print(f"\nPermissoes necessarias para arquivo confidencial:")
print(f"  {permissoes_arquivo_confidencial}")

def verificar_acesso(permissoes_usuario, permissoes_necessarias):
   """Verifica se as permissoes necessarias sao subconjunto das do usuario."""
   if permissoes_necessarias <= permissoes_usuario:
       return True, set()
   else:
       faltantes = permissoes_necessarias - permissoes_usuario
       return False, faltantes


print(f"\n--- Funcionario so com cargo RH ---")
acesso, faltantes = verificar_acesso(RH, permissoes_arquivo_confidencial)
if acesso:
   print("  ACESSO PERMITIDO")
else:
   print(f"  ACESSO NEGADO | Faltam: {faltantes}")


print(f"\n--- Funcionario so com cargo TI ---")
acesso, faltantes = verificar_acesso(TI, permissoes_arquivo_confidencial)
if acesso:
   print("  ACESSO PERMITIDO")
else:
   print(f"  ACESSO NEGADO | Faltam: {faltantes}")


print(f"\n--- Funcionario com AMBOS os cargos ---")
acesso, faltantes = verificar_acesso(total_permissoes, permissoes_arquivo_confidencial)
if acesso:
   print("  ACESSO PERMITIDO")
else:
   print(f"  ACESSO NEGADO | Faltam: {faltantes}")