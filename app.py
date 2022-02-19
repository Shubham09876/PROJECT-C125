from flask import Flask,jsonify,request
from predictionCode import predict_image

app = Flask(__name__)

@app.route('/predictedImage' , methods=['POST'])
def predictedImage():
    image = request.files.get('digit')
    prediction = predict_image(image)
    return jsonify({ 
        'image' : prediction
     } , 200)

if __name__ == '__main__':
    app.run(debug=True)