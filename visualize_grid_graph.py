def Mat2Str(M):
    S = ""
    for s in M:
        for c in s:
            S+=str(c)
        S+="\n"
    return S

colors_vertex = {0:'white',1:'red',2:'orange',3:'yellow',4:'green',5:'cyan', 6:'blue', 7:'magenta',  }

def format_num(k):
    s = str(k)
    if len(s) <2:
        return ' ' + s
    else:
        return s
def rgb2hex(r,g,b):
    return '#%02x%02x%02x' % (r,g,b)

def rgb(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)
    x = (value-minimum) / (maximum - minimum)
    if x >2.0/5:
        r = 0
        if x > 4.0/5:
            r = int(255*(5*x-4))
        b = int(min(255,255*(5*x-2)))
    else:
        b = 0
        r = int(min(255, 255*(2-5*x)))
    if x < 4.0/5:
        g = int(min(255, 255*(4-5*x),255*5*x))
    else:
        g = 0
    return r, g, b

def makeStr(l):
    if l <= 9:
        return " " + str(l)
    return str(l)

def getMessageString(G,N,L,k,cuts,BC):
    M = [['  ']*(3*(N-1)+1) for _ in xrange((3*(L-1)+1))]
    for i in range(L):
        for j in range(N):
            l = BC[i][j]
            if l >0:
                r,g,b = rgb(1,k,l)
                x = (l-1)*1.0/(k-1)
                if x > 1.0/10 and x < 7.0/10:
                    M[3*i][3*j]=  "<span style='font-weight: bold;background-color: " + rgb2hex(r,g,b)+"'>" + makeStr(l)+"</span>"
                else:
                    M[3*i][3*j]=  "<span style='font-weight: bold;border-color:black;color:white;background-color: " + rgb2hex(r,g,b)+"'>" + makeStr(l)+"</span>"
            else:
                M[3*i][3*j]=  "<span class='site-"+colors_vertex[l]+"'> *</span>"
 
    for e in G.edges():
        # s = source node
        # t = target node
        (S,T) = e
        (Sx,Sy) = S
        (Tx,Ty) = T
        if Sx != -1 and Sy != -1 and Tx != -1 and Ty != -1:
            C = round(255*(1-cuts[e])) 
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

def vgg(G,N,L,k,cuts,M,name):
    """ visualizes the grid graph by printing to an HTML file called name """
    printToHTML(getMessageString(G, N, L,k, cuts, M),name)
    return None



def vgganimate(G,N,L,k,cuts_series,Msg,name):
    M = "<head><link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\"></head>"
    S1 = """
    <link rel="stylesheet" type="text/css" href="style.css">
   <script type="text/javascript" src="gui.js"></script>
    <script>
    var MAX = """
    S2 = """
    </script>
    </body>
    <input type="button" onclick="myfirst()" value="first" />
    <input type="button" onclick="myprev()" value="prev" />
    <input type="button" onclick="mynext()" value="next" />
    <input type="button" onclick="mylast()" value="last" />
    <input type="button" onclick="autoplay()" value="autoplay" />
    <input type="button" onclick="stopautoplay()" value="stop" />
    """
    M = M + S1 + str(len(cuts_series)) + S2

    for i in range(len(cuts_series)):
        cuts = cuts_series[i]
        j = i +1
        M = M + "<pre id=\"iter" + str(j) + "\"" + (">" if j ==1 else " style=\"display: none;\">")
        M = M + getMessageString(G,N,L,k,cuts,Msg)
        M = M + "</pre>\n"
    M = M + "</body>"
    f = open(name,'w')
    f.write(M)
    f.close()
    return None
