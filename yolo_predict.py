from yolov4.tf import YOLOv4
import cv2
import matplotlib.pyplot as plt
from PIL import Image
from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg

class PredictorImage(object):

    def __init__(self):
        self.yolo = YOLOv4()
        self.yolo.classes = './coco.names'
        self.yolo.make_model()
        self.yolo.load_weights("./model/yolov4-custom_last.weights", weights_type="yolo")
        self.config = Cfg.load_config()
        self.config['weights'] = './model/transformerocr.pth'
        self.config['predictor']['beamsearch']=False
        self.config['device'] = 'cpu'
        self.detector = Predictor(self.config)
        self.classes = ['id', 'name', 'dmy', 'add1', 'add2']
        self.res = dict.fromkeys(self.classes, '')
        # self.address_correction = AddressCorrection()
            
    def predict(self, img):
        return self.yolo.predict(img)

    def inference(self, img):
        res = self.predict(img)
        img_h, img_w = img.shape[:2]
        for r in res:
            x_center_p, y_center_p,  w_p, h_p, cl, pro = r[0], r[1], r[2], r[3], r[4], r[5]
            w = int(img_w * w_p)
            h = int(img_h * h_p)
            x = int(x_center_p * img_w - w/2)
            y =  int(y_center_p * img_h - h/2)
            resize_img = img[y:y+h, x:x+w, :]
            self.predict_ocr(resize_img, self.classes[int(cl)])
            cv2.rectangle(img,(int(x), int(y)),(int(x+w), int(y+h)),(0,255,0),1)
        print(self.res)
        cv2.imshow('predict', img)
        cv2.waitKey(0)
    
    def predict_ocr(self, img, label):
        img = Image.fromarray(img)
        s = self.detector.predict(img)
        self.res[label] += s + ' '


if __name__ == '__main__':
    img = cv2.imread('./test/a.jpg')
    pre = PredictorImage()
    pre.inference(img)