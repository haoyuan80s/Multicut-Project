function A = tri2adj(T, d)
% TRI2ADJ converts a list of vertex triangles into an adjacency matrix. If
% a distance measure is given for the vertices, the adjacency matrix is
% weighted by those distances.
%

    nT = max(T(:));
    assert(ismatrix(T) && size(T,2) == 3, 'Input T is of the wrong size');
    if ~exist('d', 'var')
        d = ones(nT);
    else
        assert(ismatrix(d) && size(d,1) == size(d,2), 'Input d is of the wrong size');
        assert(size(d,1) >= nT, 'Input T refers to vertices not included in d');
    end
    n = size(d,1);
    m = size(T,1);
    
    A = zeros(n);
    for i = 1:m
        A(T(i,1),T(i,2)) = 1;
        A(T(i,2),T(i,3)) = 1;
        A(T(i,3),T(i,1)) = 1;
    end
    A = (A + A') > 0;
    A = A .* d;

end