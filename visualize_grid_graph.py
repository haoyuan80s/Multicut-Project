def Mat2Str(M):
    S = ""
    for s in M:
        for c in s:
            S+=str(c)
        S+="\n"
    return S

colors_vertex = {0:'white',3:'red',2:'green', 1:'blue', 4:'yellow',5:'magenta', 6:'cyan', 7:'orange'}

def format_num(k):
    s = str(k)
    if len(s) <2:
        return ' ' + s
    else:
        return s

def getMessageString(G,N,L,cuts,BC):
    M = [['  ']*(3*(N-1)+1) for _ in xrange((3*(L-1)+1))]
    for i in range(L):
        for j in range(N):
            M[3*i][3*j]=  "<span class='site-"+colors_vertex[BC[i][j]]+"'> *</span>"
 
    for e in G.edges():
        # s = source node
        # t = target node
        (S,T) = e
        (Sx,Sy) = S
        (Tx,Ty) = T
        if Sx != -1 and Sy != -1 and Tx != -1 and Ty != -1:
            C = round(255*(1-0.25*cuts[e])) 
            hex_color_code = '#%02x%02x%02x' % (C,C,C)
            (dx,dy) = (Tx-Sx,Ty-Sy)
            (i,j)=(3*Sx+2*dx,3*Sy + 2*dy)
            # print "===="
            # print G.vertices()
            # print (S,T)
            # print len(M)
            # print len(M[0])
            # print i
            # print j
            M[i][j] = "<span class='msg' style = 'background-color : " + hex_color_code + "'>  </span>"

            (T,S) = e
            (Sx,Sy) = S
            (Tx,Ty) = T
             
            (dx,dy) = (Tx-Sx,Ty-Sy)
            (i,j)=(3*Sx+2*dx,3*Sy + 2*dy)
            M[i][j] = "<span class='msg' style = 'background-color : " + hex_color_code + "'>  </span>"
    # requires a list of list of chars
 
 
    return Mat2Str(M)

def printToHTML(M,filename):
    M = "<body><pre>"+M+"</pre><body>"
    M = "<head><link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\"></head>"+M
    f = open(filename,'w')
    f.write(M)
    f.close()
    return None

def fill(H,M):
    for s in H.vertices():
        (i,j) = s
        if i == -1:
            d_s = H.dist_from(s)
            P = [(k,l) for (k,l) in H.vertices() if d_s[(k,l)] < float("inf") and k != -1] 
            for (k,l) in P:
                M[k][l] = j
    return M

def vgg(G,N,L,cuts,M,name):
    """ visualizes the grid graph by printing to an HTML file called name """
    printToHTML(getMessageString(G, N, L, cuts, M),name)
    return None

