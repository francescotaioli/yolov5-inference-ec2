import torch


def inference(img_path, conf_level=0.6, save_path='predicted'):
    model = torch.hub.load('ultralytics/yolov5', 'custom',
                           path='model/nfl_weights.pt',
                           )
    model.conf = conf_level
    model.eval()
    bounding_boxes = model(img_path)
    bounding_boxes.save(save_path)
    return bounding_boxes.xyxy[0]
