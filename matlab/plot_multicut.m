function plot_multicut(x, y, AG, AH, st)
% PLOT_MULTICUT plots a multicut on a graph with adj. matrix AG and
% residual adj. matrix AH.

    [xx1,yy1] = gplot(AG, [x y]);
    [xx2,yy2] = gplot(AH, [x y]);
    
    plot(xx1,yy1, '- ', 'Color', [0.7 0.7 0.7], 'LineWidth', 1.5);
    hold on;
    plot(xx2,yy2, '-ok', 'LineWidth', 3);
    plot(x,y, ' ok', 'MarkerFaceColor', [0 0 0], 'LineWidth', 3);
    
    k = size(st,1);
    colors = sin(rand(k,3)*pi).^2;
    for i = 1:k
        plot(x(st(i,:)'), y(st(i,:)'), ' o', 'Color', colors(i,:), ...
            'MarkerFaceColor', colors(i,:));
    end

end