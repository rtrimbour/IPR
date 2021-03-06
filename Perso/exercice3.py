def minmaxmoy(liste = [10, 18, 14, 20, 12, 16]) :

    """Prend en entrée une liste d'entiers dont elle donne en sortie le minimum, le maximum et la moyenne sous forme d'un tuple.
    Si aucun argument donné en entrée la liste traitée par défaut sera : [10, 18, 14, 20, 12, 16]"""
    
    work_list = list(liste)
    work_list.sort()
    moy = 0
    min = work_list[0]
    max = work_list[-1]

    for a in work_list :
        moy = moy + a
    moy = moy // len(work_list)

    return(min, max, moy)
