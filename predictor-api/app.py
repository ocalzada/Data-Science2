"""
This is routing logic for pic-metric-1/predictor.
"""
from flask import Flask, request
from flask import jsonify
from .resnet50 import process_img_path, resnet_model


# from werkzeug.debug import get_current_traceback


def create_app():
    app = Flask(__name__)

    @app.route('/predictor', methods=['POST'])
    def predictor():
        """
        This is a route that expects an image url and id.
        It returns image classifications, probabilities, and the photo_id.
        """
        # Get info from backend.
        lines = request.get_json(force=True)

        # Get strings from json.
        url = lines['url']
        photo_id = lines['photo_id']

        # Make sure the input's correct.
        assert isinstance(url, str)
        assert isinstance(photo_id, int)

        # Process the image and generate predictions.
        predictions = resnet_model(process_img_path(url))

        for prediction in predictions:
            prediction[1] = round(prediction[1], 2)

        send_back = {'photo_id': photo_id, 'predictions': predictions}

        # Return JSON object with photo_id and
        # a list of predictions as a string, unless
        # the url was invalid.  
        return jsonify(send_back)

    return app
