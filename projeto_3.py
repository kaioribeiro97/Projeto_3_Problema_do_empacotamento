import numpy as np
import time
import os
import statistics

def menu ():
  peso = []
  while True:
        print("---------Menu---------\n")
        print('[1] - obter os pesos')
        print('[2] - Bin-Packing-Problem')
        print('[3] - Limpar console')
        print('[4] - Sair')
        a = int(input('Digite uma das cinco opções: '))
        if a == 1:
          peso,opcao = pesos()
        elif a == 2:
          if peso == []:
            print("Você deve obter os valores")
            menu()
          else: 
            while True:
              print('[0] - Voltar')
              print('[1] - next-fit')
              print('[2] - first-fit')
              print('[3] - best-fit')
              b = int(input('Digite uma das opções: '))
                        
              if b == 1:
                f = open('saida.txt', 'a')
                n=[0,1,2,3,4]
                tempos = [0 for x in n]
                arquivo_texto = arquivo(opcao)
                f.write('Arquivo texto: {}\n'.format(arquivo_texto))
                for i in range(5):
                  a =  time.time()
                  capacidade =  10000
                  n = len(peso)
                  next_fit = next_Fit(peso, capacidade)
                  b = time.time()
                  
                  print("Numero de compartimentos necessários no Next Fit:", next_fit)
                  tempos[i]=b-a
                  media = statistics.median(tempos)
                f.write("Metodo: Next fit\n")
                f.write("Tempo de execucao: {:.6e}s\n".format(media))
                f.write("Numero de compartimentos necessarios no Next Fit:{}\n".format(next_fit))
                print("Tempos:",tempos)
                f.close()
              elif b == 2:
                f = open('saida.txt', 'a')
                n=[0,1,2,3,4]
                tempos = [0 for x in n]
                arquivo_texto = arquivo(opcao)
                f.write('Arquivo texto: {}\n'.format(arquivo_texto))
                for i in range(5):
                  a =  time.time()
                  capacidade =  10000
                  n = len(peso)
                  first_fit = first_Fit(peso, n, capacidade)
                  b = time.time()
                  tempos[i]=b-a
                  media = statistics.median(tempos)
                f.write("Metodo: First fit\n")
                f.write("Tempo de execucao: {:.6e}s\n".format(media))
                f.write("Numero de compartimentos necessarios no First Fit:{}\n".format(first_fit))
                print("Numero de compartimentos necessários no First Fit:",first_fit)
                print("Tempos:",tempos)  
                f.close()
              elif b == 3:
                f = open('saida.txt', 'a')
                n=[0,1,2,3,4]
                tempos = [0 for x in n]
                arquivo_texto = arquivo(opcao)
                f.write('Arquivo texto: {}\n'.format(arquivo_texto))
                for i in range(5):
                  a =  time.time()
                  capacidade =  10000
                  n = len(peso)
                  best_fit = best_Fit(peso, n, capacidade)
                  b = time.time()
                  tempos[i]=b-a
                  media = statistics.median(tempos)
                f.write("Metodo: Best fit\n")
                f.write("Tempo de execucao: {:.6e}s\n".format(media))
                f.write("Numero de compartimentos necessarios no Best Fit:{}\n".format(best_fit))
                print("Numero de compartimentos necessários no Best Fit:",best_fit)
                print("Tempos:",tempos)  
                f.close()
              elif b ==0 :
                menu()
      
        elif a == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
        elif a == 4:
          print('exit')
          break
def arquivo(opcao):
  if opcao == 1:
    arquivo_texto = 'Waescher_TEST005'
  elif opcao == 2:  
    arquivo_texto = 'Waescher_TEST014'
  elif opcao == 3:  
    arquivo_texto = 'Waescher_TEST022'
  elif opcao == 4:
    arquivo_texto = 'Waescher_TEST030'
  elif opcao == 5:
    arquivo_texto = 'Waescher_TEST044'
  elif opcao == 6:
    arquivo_texto = 'Waescher_TEST049'
  elif opcao == 7:
    arquivo_texto = 'Waescher_TEST054'
  elif opcao == 8:
    arquivo_texto = 'Waescher_TEST055A'
  elif opcao == 9:
    arquivo_texto = 'Waescher_TEST055B'
  elif opcao == 10:
    arquivo_texto = 'Waescher_TEST058'
  elif opcao == 11:
    arquivo_texto = 'Waescher_TEST065'
  elif opcao == 12:
    arquivo_texto = 'Waescher_TEST068'
  elif opcao == 13:
    arquivo_texto = 'Waescher_TEST075'
  elif opcao == 14:
    arquivo_texto = 'Waescher_TEST082'
  elif opcao == 15:
    arquivo_texto = 'Waescher_TEST084'
  elif opcao == 16:
    arquivo_texto = 'Waescher_TEST095'
  elif opcao == 17:
    arquivo_texto = 'Waescher_TEST097'
  return arquivo_texto
  
  
  
          
def pesos():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("---------Arquivos---------\n")
    print('[1] - Waescher_TEST005')
    print('[2] - Waescher_TEST014')
    print('[3] - Waescher_TEST022')
    print('[4] - Waescher_TEST030')
    print('[5] - Waescher_TEST044')
    print('[6] - Waescher_TEST049')
    print('[7] - Waescher_TEST054')
    print('[8] - Waescher_TEST055A')
    print('[9] - Waescher_TEST055B')
    print('[10] - Waescher_TEST058')
    print('[11] - Waescher_TEST065')
    print('[12] - Waescher_TEST068')
    print('[13] - Waescher_TEST075')
    print('[14] - Waescher_TEST082')
    print('[15] - Waescher_TEST084')
    print('[16] - Waescher_TEST095')
    print('[17] - Waescher_TEST097')
    print("[18] - Voltar")
    opcao = int(input('Digite uma das opções: '))
    if opcao !=18:
      caminho = 'dataset/' + str(opcao) + '.txt'
      peso = np.loadtxt(caminho).astype(int)
    if opcao == 18:
      menu()
    return peso,opcao

def next_Fit(peso, c):
    res = 0
    rem = c
  
    for _ in range(len(peso)):
        if rem >= peso[_]:
            rem = rem - peso[_]
        else:
            res += 1
            rem = c - peso[_]
  
    return res

def first_Fit(peso, n, c):
    res = 0
    bin_rem = [0]*n

    for i in range(n):
        j = 0
        while( j < res):
            if (bin_rem[j] >= peso[i]):
                bin_rem[j] = bin_rem[j] - peso[i]
                break
            j+=1
        if (j == res):
            bin_rem[res] = c - peso[i]
            res= res+1
    return res

def best_Fit(peso, n, c):
    res = 0
    bin_rem = [0]*n
    for i in range(n):
        j = 0
        min = c + 1
        bi = 0
 
        for j in range(res):
            if (bin_rem[j] >= peso[i] and bin_rem[j] - peso[i] < min):
                bi = j
                min = bin_rem[j] - peso[i]
        if (min == c + 1):
            bin_rem[res] = c - peso[i]
            res += 1
        else:
            bin_rem[bi] -= peso[i]
    return res
