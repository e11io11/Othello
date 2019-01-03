from termcolor import *

import colorama #not needed on linux

def indice_valide(plateau, indice):
    if indice >= 0 and indice <= plateau["n"]-1:
        return True
    else:
        return False


def case_valide(plateau, i, j):
    if indice_valide(plateau, i) and indice_valide(plateau, j):
        return True
    else:
        return False


def get_case(plateau, i, j):
    assert case_valide(plateau, i, j), "La case est invalide"
    return plateau["cases"][i*plateau["n"]+j]


def set_case(plateau, i, j, val):
    assert case_valide(plateau, i, j), "La case est invalide"
    assert (val == 0 or val == 1 or val == 2), "La valeur est invalide"
    plateau["cases"][i*plateau["n"]+j] = val


def creer_plateau(n):
    assert n == 4 or n == 6 or n == 8, "La taille du plateau est invalide"
    i = 0
    cases = []
    while i < n*n :
        cases.append(0)
        i += 1
    cases[int((n/2-1)*n+n/2-1)] = 2
    cases[int((n/2-1)*n+n/2)] = 1
    cases[int((n/2)*n+n/2-1)] = 1
    cases[int((n/2)*n+n/2)] = 2

    plateau = {
                "n":n,
                "cases":cases
              }
    return plateau


def afficher_plateau(plateau):
    colorama.init() #not needed on linux
    n = plateau["n"]

    background_colors = ["on_cyan", "on_green"]
    border_background_color = "on_blue"
    border_color = "white"
    white_piece_color = "white"
    black_piece_color = "grey"


    cprint("     "+n*"         "+"     ", border_color, border_background_color)
    ligne_abscisse = "     "
    i = 1
    while i < n+1 :
        ligne_abscisse += "    "+str(i)+"    "
        i+=1
    cprint(ligne_abscisse+"     ", border_color, border_background_color)
    cprint("     "+n*"         "+"     ", border_color, border_background_color)


    l_pair = ""
    l_impair = ""
    i = 0
    while i < n:
        l_pair += colored("         ", "blue", background_colors[i%2])
        l_impair += colored("         ", "blue", background_colors[(i+1)%2])
        i+=1


    i=0
    while i < n:
        if i%2 == 0:
            print(colored("     ", "blue", border_background_color) + l_pair + colored("     ", "blue", border_background_color))
            print(colored("     ", "blue", border_background_color) + l_pair + colored("     ", "blue", border_background_color))
            ligne_valeurs = ""
            j = i*n
            fin_ligne = j+n
            while j < fin_ligne:
                if plateau["cases"][j] == 0:
                    ligne_valeurs += colored("         ", "blue", background_colors[(fin_ligne-j)%2])
                elif plateau["cases"][j] == 1:
                    ligne_valeurs += colored("   ###   ", black_piece_color, background_colors[(fin_ligne-j)%2])
                else:
                    ligne_valeurs += colored("   ###   ", white_piece_color, background_colors[(fin_ligne-j)%2])
                j += 1
            print(colored("  "+chr(i+97)+"  ", border_color, border_background_color) + ligne_valeurs + colored("  "+chr(i+97)+"  ", border_color, border_background_color))
            print(colored("     ", "blue", border_background_color) + l_pair + colored("     ", "blue", border_background_color))
            print(colored("     ", "blue", border_background_color) + l_pair + colored("     ", "blue", border_background_color))
        else:
            print(colored("     ", "blue", border_background_color) + l_impair+colored("     ", "blue", border_background_color))
            print(colored("     ", "blue", border_background_color) + l_impair+colored("     ", "blue", border_background_color))
            ligne_valeurs = ""
            j = i*n
            fin_ligne = j+n
            while j < fin_ligne:
                if plateau["cases"][j] == 0:
                    ligne_valeurs += colored("         ", "blue", background_colors[((fin_ligne-j)+1)%2])
                elif plateau["cases"][j] == 1:
                    ligne_valeurs += colored("   ###   ", black_piece_color, background_colors[((fin_ligne-j)+1)%2])
                else:
                    ligne_valeurs += colored("   ###   ", white_piece_color, background_colors[((fin_ligne-j)+1)%2])
                j += 1
            print(colored("  "+chr(i+97)+"  ", border_color, border_background_color) + ligne_valeurs + colored("  "+chr(i+97)+"  ", border_color, border_background_color))
            print(colored("     ", "blue", border_background_color) + l_impair + colored("     ", "blue", border_background_color))
            print(colored("     ", "blue", border_background_color) + l_impair + colored("     ", "blue", border_background_color))
        i+=1


    cprint("     "+n*"         "+"     ", border_color, border_background_color)
    cprint(ligne_abscisse+"     ", border_color, border_background_color)
    cprint("     "+n*"         "+"     ", border_color, border_background_color)
