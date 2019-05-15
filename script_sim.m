clear;
clc;

x_IC = [0;
        1;
        0;
        0];

sim('simulation')

clf(figure(1), 'reset')
figure(1)
squareX = [1 2 2 1 1];
squareY = [1 1 2 2 1];
g = hgtransform;
patch('XData', squareX, 'YData', squareY, 'FaceColor','blue','Parent',g);
xlim([0 10])
ylim([0 10]) 

pt1 = [0; 0; 0];
pt2 = [5 2 0];
translate = [0; 0; 0];
for t = 1:1:50
ptCur = [x(t,1); 0; 0];

display(x(t,2))    
    
g.Matrix = makehgtform('translate', ptCur,...
                       'zrotate', x(t,2));
drawnow

end
