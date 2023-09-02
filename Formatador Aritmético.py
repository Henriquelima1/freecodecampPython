import re
def arithmetic_arranger(vetor):
  mat =[]
  for i in vetor:
    componentes = re.split(r'\s*([\+\-\*/])\s*', i)
    comprimento = len(componentes[0])
    if(comprimento <= len(componentes[2]))
      comprimento = len(componentes[2]

    
    mat[0][i] = componentes[0]
    mat[1][i] = componentes[1] + " " + componentes[2]
    mat[2][i] = "-----"

  
    return arranged_problems