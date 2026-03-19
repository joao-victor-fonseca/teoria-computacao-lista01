import re

RESERVADAS = {
  "if", "else", "while", "for", "return",
  "int", "System", "out", "print", "public", "class"
}

codigo_fonte = """
public class StarRectangle {
  public void printRectangle(int n) {
      for (int i = 0; i < n; i++) {
          for (int j = 0; j < n; j++) {
              System.out.print(" * ");
          }
          System.out.println();
      }
  }
  public void printBottonLeftTriangle(int n) {
      for (int i = 0; i < n; i++) {
          for (int j = 0; j <= i; j++) {
              System.out.print(" * ");
          }
          System.out.println();
      }
  }
  public void printTopRightTriangle(int n) {
      for (int i = 0; i < n; i++) {
          for (int j = 0; j < n; j++) {
              if (j < i)
                  System.out.print("   ");
              else
                  System.out.print(" * ");
          }
          System.out.println();
      }
  }
}
"""

palavras_codigo = set(re.findall(r'[A-Za-z_]\w*', codigo_fonte))

print("=" * 60)
print("EXERCICIO 1 - Filtro de Palavras Reservadas")
print("=" * 60)

print(f"\nTodas as palavras extraidas do codigo:")
print(f"  {sorted(palavras_codigo)}")

reservadas_encontradas = palavras_codigo & RESERVADAS
print(f"\nPalavras RESERVADAS no codigo (intersecao):")
print(f"  {sorted(reservadas_encontradas)}")

identificadores = palavras_codigo - RESERVADAS
print(f"\nPossiveis IDENTIFICADORES (diferenca):")
print(f"  {sorted(identificadores)}")