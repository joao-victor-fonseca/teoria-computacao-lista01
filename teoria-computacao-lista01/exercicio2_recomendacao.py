Usuario_A = {"Python", "Jogos", "Musica", "IA"}
Usuario_B = {"Java", "IA", "Musica", "Caminhada"}

print("=" * 60)
print("EXERCICIO 2 - Recomendacao de Amigos em Comum")
print("=" * 60)

print(f"\nUsuario A: {Usuario_A}")
print(f"Usuario B: {Usuario_B}")

em_comum = Usuario_A & Usuario_B
print(f"\nInteresses em COMUM (A intersecao B):")
print(f"  {em_comum}")

sugestoes_para_A = Usuario_B - Usuario_A
print(f"\nSugestoes para o Usuario A (B - A):")
print(f"  {sugestoes_para_A}")