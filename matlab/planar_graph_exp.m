% Script to generate the test instances for the planar graph experiments

%%%%%
n_ = 10:10:200;
k_ = ceil((10:10:200)/20);
%%%%%
rng(0);

for t = 1:length(n_)
    
    n = n_(t);
    k = k_(t);
    stem = sprintf('data/n%03d_k%02d', n, k);
    if ~exist(stem, 'file')
        mkdir(stem);
    end
    
    for i = 1:5
        fname = sprintf('%s/G%d', stem, i);
        generate_planar_graph(n, [], fname, k);
    end
    
end
