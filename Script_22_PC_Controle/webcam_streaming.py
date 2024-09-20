import cv2
from flask import Flask, render_template, Response

video = cv2.VideoCapture(1)

def get_frame():
    while True:
        success, frame = video.read()
        sc, encoded_image = cv2.imencode('.jpg', frame)
        frame = encoded_image.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# url_for('video_feed')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed_url')
def video_feed():
    return Response(get_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', post=5001)