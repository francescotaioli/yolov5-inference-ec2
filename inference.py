import torch


def inference(img_path, conf_level=0.4, save_path='predicted'):
    model = torch.hub.load('ultralytics/yolov5', 'custom',
                           path='model/nfl_weights.pt',
                           )
    model.eval()
    bounding_boxes = model(img_path)
    bounding_boxes.save(save_path)
    return bounding_boxes.xyxy[0]
