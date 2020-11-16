#!/usr/bin/python3
# coding: utf-8


def conv(dec_ch):
  for loop in range(int(dec_ch[2]+dec_ch[3]), -1, -1):
    subStr = '2^'+str(loop)
    if (len(str(loop)) < 2):
      subStr = '2^0'+str(loop)
    if (subStr in dec_ch):
      print ('1', end='')
    else:
      print ('0', end='')
    if (loop%4 == 0): # un espace tous les 4 chiffres
      print (' ', end='')


def dec(base, puissance, nombre, dec_ch):
  if (base ** puissance <= nombre):
    nombre -= base ** puissance
    power = str(puissance)
    if (len(str(puissance)) < 2):
      power = '0' + str(puissance)
    dec_ch += str(base)+'^'+str(power)+'+'
  if (base ** puissance == 1):
    return dec_ch[:-1]
  # Dans ce cas, la récurrence peut être remplacée.
  return (dec(base, puissance-1, nombre, dec_ch))


def main():
  while (True):
    nombre = int(input('Nombre à convertir : '))
    puissance = 99
    decompo = dec(2, puissance, nombre, '')
    print (nombre, '=', decompo)
    if (nombre < 2 ** 99):
      conv(decompo)
    else:
      print ('Pour une conversion en binaire, saisissez un nombre < 2⁹⁹.')
    print ()
    print ('Appuie sur une touche non numérique pour quitter.')


main()
----------------------------------------------------------------------------- Résultat -----------------------------------------------------------------------