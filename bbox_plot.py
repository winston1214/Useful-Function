## Reference YOLOv5
import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class Colors:
    # Ultralytics color palette https://ultralytics.com/
    def __init__(self):
#         hex = matplotlib.colors.TABLEAU_COLORS.values()
        hexs = ('FF3838', 'FF9D97', 'FF701F', 'FFB21D', 'CFD231', '48F90A', '92CC17', '3DDB86', '1A9334', '00D4BB',
                '2C99A8', '00C2FF', '344593', '6473FF', '0018EC', '8438FF', '520085', 'CB38FF', 'FF95C8', 'FF37C7')
        self.palette = [self.hex2rgb(f'#{c}') for c in hexs]
        self.n = len(self.palette)

    def __call__(self, i, bgr=False):
        c = self.palette[int(i) % self.n]
        return (c[2], c[1], c[0]) if bgr else c

    @staticmethod
    def hex2rgb(h):  # rgb order (PIL)
        return tuple(int(h[1 + i:1 + i + 2], 16) for i in (0, 2, 4))

def plot_bbox(img_path,label_dic,xyxys):
    '''
    img_path : image directory
    label_dic : {'label 1':0,'label 2':0 , ...}
    xyxy = [[xmin,ymin,xmax,ymax],[xmin,ymin,xmax,ymax], ...]
    '''
    colors = Colors()  # create instance for 'from utils.plots import colors'

    im0 = cv2.imread(img_path)

    lw = max(round(sum(im0.shape) / 2 * 0.003), 2)

    # label_dic = {'car_front':0,'car_back':1,'truck_back':2}
    txt_color=(255, 255, 255)

    for idx,xyxy in enumerate(xyxys):
        color = colors(label_dic[label])
        p1, p2 = (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3]))
        cv2.rectangle(im0, p1, p2, color, thickness=lw, lineType=cv2.LINE_AA)
        tf = max(lw - 1, 1)  # font thickness
        w, h = cv2.getTextSize(label, 0, fontScale=lw / 3, thickness=tf)[0]  # text width, height
        outside = p1[1] - h >= 3
        p2 = p1[0] + w, p1[1] - h - 3 if outside else p1[1] + h + 3
        cv2.rectangle(im0, p1, p2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(im0,
                    label, (p1[0], p1[1] - 2 if outside else p1[1] + h + 2),
                    0,
                    lw / 3,
                    txt_color,
                    thickness=tf,
                    lineType=cv2.LINE_AA)
    plt.imshow(cv2.cvtColor(im0,cv2.COLOR_BGR2RGB))
