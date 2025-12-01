from heapq import heappush,heappop

def voisins(i,j,ligne_matrice,colonne_matrice):
    liste_voisins = []
    
    # Voisin du dessus
    if i > 0:
        liste_voisins.append((i-1, j))
    
    # Voisin du dessous
    if i < ligne_matrice - 2:
        liste_voisins.append((i+1, j))
    
    # Voisin de gauche
    if j > 0:
        liste_voisins.append((i, j-1))
    
    # Voisin de droite
    if j < colonne_matrice - 1:
        liste_voisins.append((i, j+1))
    
    return liste_voisins

def dijkstra_grille(matrice,sourcex,sourcey):
    
    ligne_matrice=len(matrice)
    colonne_matrice=len(matrice[0])
    
    tag=[[0] * colonne_matrice for _ in range(ligne_matrice)]  # 0: non visité, -1: accepté, 1: front
    tag[sourcex][sourcey] = -1
    
    dist=[[float('inf')] * colonne_matrice for _ in range(ligne_matrice)]
    dist[sourcex][sourcey] = 0
    
    predx=[[-1] * colonne_matrice for _ in range(ligne_matrice)]
    predy=[[-1] * colonne_matrice for _ in range(ligne_matrice)]
    
    H=[]
    
    v=voisins(sourcex,sourcey,ligne_matrice,colonne_matrice)
    
    for voisin in v:
        vx,vy=voisin[0],voisin[1]
        if tag[vx][vy]==0:
            tag[vx][vy]=1
            heappush(H,[matrice[vx][vy],vx,vy,sourcex,sourcey])
    
    while H!=[]:
        dmin,vminx,vminy,px,py=heappop(H)
        if(tag[vminx][vminy]!=-1):
            dist[vminx][vminy]=dmin
            tag[vminx][vminy]=-1
            predx[vminx][vminy]=px
            predy[vminx][vminy]=py
            v=voisins(vminx,vminy,ligne_matrice,colonne_matrice)
            
            for voisin in v :
                vx,vy=voisin[0],voisin[1]
                if tag[vx][vy]==0:
                    tag[vx][vy]=1
            
            for voisin in v :
                vx,vy=voisin[0],voisin[1]
                if tag[vx][vy]==1:
                    nv_dist=dist[vminx][vminy]+matrice[vx][vy]
                    if dist[vx][vy]>nv_dist:
                        dist[vx][vy]=nv_dist
                        heappush(H,[nv_dist,vx,vy,vminx,vminy])
                        
    return dist,predx,predy,tag