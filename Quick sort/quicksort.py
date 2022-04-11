def distribuzione( a, lx, rx):
    p_i = lx
    rx -= 1
    lx += 1
    while lx < rx :
        while lx < len(a) and a[lx] <= a[p_i]:
             lx += 1
        while rx >= 0 and a[rx] > a[p_i]  :
             rx -= 1
        #il while  lx si ferma quando a[lx] è maggiore di a[p_i]
        #il while rx si ferma quando a[rx] è uguale a a[p_i]
        if lx < rx :
            a[lx], a[rx] = a[rx], a[lx]
        else :
            a[rx], a[p_i] = a[p_i], a[rx]   
    return rx
    
def quick_sort(a, lx, rx):
    if lx < rx-1:
        
        pos = distribuzione( a, lx, rx)
        print(a)
        quick_sort(a, lx, pos)
        quick_sort(a, pos+1, rx)
    
    distribuzione(a, 0, len(a))



