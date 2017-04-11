function [A,x,y] = read_2d_graph(fname)
% READ_2D_GRAPH reads a graph from 'fname.adj' and 'fname.vtx'.
%
    
    vfile = fopen([fname '.vtx'], 'r');
    T = textscan(vfile, '(%f,%f)');
    x = T{1};
    y = T{2};
    n = length(x);
    assert( n > 0, 'Input .vtx file is not formed correctly');
    fclose(vfile);
    
    afile = fopen([fname '.adj'], 'r');
    T = textscan(afile, '%f,%f,%f'); % i and j must be doubles for some reason
    i = T{1};
    j = T{2};
    w = T{3};
    A = sparse(i, j, w, n, n);
    A = A + A';
    fclose(afile);

end