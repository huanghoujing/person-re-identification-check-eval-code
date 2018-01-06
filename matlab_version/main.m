
%% Load data

query_gallery_distance = dlmread('../data/query_gallery_distance.txt', ' ');
query_id = dlmread('../data/query_id.txt', ' ');
query_cam = dlmread('../data/query_cam.txt', ' ');
gallery_id = dlmread('../data/gallery_id.txt', ' ');
gallery_cam = dlmread('../data/gallery_cam.txt', ' ');

%% Compute score

[CMC, map, ~, ~] = evaluation(query_gallery_distance', gallery_id, query_id, gallery_cam, query_cam);

%% Save score to file

dlmwrite('CMC.txt', CMC(1:100), 'delimiter', '\n');
dlmwrite('mAP.txt', map, 'delimiter', '\n');

%% Print score

fprintf('CMC Rank-1 to Rank-10: ');
for i = 1:10
    fprintf('%f  ', CMC(i));
end

fprintf('\nmAP: %f\n', map);