import cv2
import numpy as np
from detect_pulse import detect_pulsation
from detection import detect
import pandas as pd
from export import export
dict = {}

dict = detect('video_path')
export(dict)

max_area = max(dict.values())
min_area = min(dict.values())

value_max = {i for i in dict if dict[i]==max_area}
value_min = {i for i in dict if dict[i]==min_area}

print(value_max - value_min)

