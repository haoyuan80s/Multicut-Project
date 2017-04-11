function [A,x,y,st] = read_2d_graph(fname)
% READ_2D_GRAPH reads a graph from 'fname.adj' and 'fname.vtx'. If st is
% requested, s-t pairs are read from 'fname.stp' as well.
%
    
    vfile = fopen([fname '.vtx'], 'r');
    T = textscan(vfile, '(%f,%f)');
    x = T{1}; y = T{2};
    n = length(x);
    assert( n > 0, 'Input .vtx file is not formed correctly');
    fclose(vfile);
    
    afile = fopen([fname '.adj'], 'r');
    T = textscan(afile, '%f,%f,%f'); % i and j must be doubles for some reason
    i = T{1}; j = T{2}; w = T{3};
    A = sparse(i, j, w, n, n);
    A = A + A';
    fclose(afile);
    
    if nargout == 4
        sfile = fopen([fname '.stp'], 'r');
        T = textscan(sfile, '%d,%d');
        st = [T{1} T{2}];
        fclose(sfile);
    end

end