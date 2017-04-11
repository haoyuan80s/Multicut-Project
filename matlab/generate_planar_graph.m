function [A,x,y,st] = generate_planar_graph(n, seed, fname, k)
% GENERATE_PLANAR_GRAPH generates a random planar graph on [0,1]x[0,1] with
% adjacency matrix A and point coordinates x(i),y(i) for i = 1...n. Uses
% random seed and writes to 'fname.adj', 'fname.vtx', and 'fname.stp' using
% k random s-t pairs if specified.

    if exist('seed','var') && ~isempty(seed)
        rng(seed)
    end
    
    x = rand(n,1);
    y = rand(n,1);
    T = delaunay(x,y);
    d = pdist2([x y], [x y]);
    A = tri2adj(T,d);
    
    if exist('fname','var') && ~isempty(fname)
        idx = find(triu(A) > 0);
        [i,j] = ind2sub([n n], idx);
        csvwrite([fname '.adj'], [i j A(idx)]);
        
        fid = fopen([fname '.vtx'], 'w');
        fprintf(fid, '(%f,%f)\n', [x'; y']);
        fclose(fid);
        
        st = reshape(randperm(n,2*k), [k 2]);
        csvwrite([fname '.stp'], st);
    end

end