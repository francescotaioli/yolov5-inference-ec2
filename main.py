import random
from flask import Flask
from flask import request
from inference import inference

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "<h1>Call /predict endpoint. I.e curl -w '\n' -F image=@helmet.jpg [base_url]/predict</h1>"


@app.route('/predict', methods=['POST'])
def prepare_image_and_predict():
    image = request.files['image']  # get the image
    save_path = 'predicted'  # path to save the predicted image

    random_list_ = generate_random_seq()
    path = f'uploaded/nfl_predictor_{generate_random_seq()}.jpg'  # save the input image with 'unique' filename
    image.save(path)
    bounding_boxes = inference(path, save_path=save_path)  # make inference to the model

    b_boxes_positions = create_json_response(bounding_boxes.tolist())  # create json with the response from the model
    result = {'b_boxes_positions': b_boxes_positions}
    return result


def create_json_response(bounding_boxes):
    res = []
    for box in bounding_boxes:
        tmp = {
            'x1': box[0],
            'y1': box[1],
            'x2': box[2],
            'y2': box[3],
            'confidence': box[4],
            'class': box[5]
        }
        res.append(tmp)
    return res


def generate_random_seq(length=5):
    seq = random.sample(range(10, 30), length)
    return str(seq)


if __name__ == "__main__":
    app.run()
