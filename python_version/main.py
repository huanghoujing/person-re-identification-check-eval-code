from __future__ import print_function

import numpy as np
from ranking import cmc, mean_ap


# Load data

query_gallery_distance = np.loadtxt('../data/query_gallery_distance.txt')
query_id = np.loadtxt('../data/query_id.txt').flatten()
query_cam = np.loadtxt('../data/query_cam.txt').flatten()
gallery_id = np.loadtxt('../data/gallery_id.txt').flatten()
gallery_cam = np.loadtxt('../data/gallery_cam.txt').flatten()

print('query_gallery_distance.shape', query_gallery_distance.shape)
print('query_id.shape', query_id.shape)
print('query_cam.shape', query_cam.shape)
print('gallery_id.shape', gallery_id.shape)
print('gallery_cam.shape', gallery_cam.shape)

# Compute score

CMC_score = cmc(
  query_gallery_distance,
  query_ids=query_id,
  gallery_ids=gallery_id,
  query_cams=query_cam,
  gallery_cams=gallery_cam,
  topk=100,
  separate_camera_set=False,
  single_gallery_shot=False,
  first_match_break=True
)

mAP_score = mean_ap(
  query_gallery_distance,
  query_ids=query_id,
  gallery_ids=gallery_id,
  query_cams=query_cam,
  gallery_cams=gallery_cam
)

# Print score

print('CMC Rank-1 to Rank-10: ', end='')
for i in range(10):
  print(CMC_score[i], end='  ')
print('')

print('mAP:', mAP_score)

# Save score to file

with open('CMC-python-version.txt', 'w') as f:
  for s in CMC_score:
    f.write('{}\n'.format(s))

with open('mAP-python-version.txt', 'w') as f:
  f.write('{}\n'.format(mAP_score))
