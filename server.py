from flask import Flask, jsonify, request
import threading
import main

app = Flask(__name__)
status = {"finished": False}
sightreading_done = False

@app.route('/status')
def get_status():
    return jsonify(status)

@app.route('/sightreading_status', methods=['GET'])
def get_sightreading_status():
    return jsonify({'done': sightreading_done})

@app.route('/set_sightreading_done', methods=['POST'])
def set_sightreading_done():
    global sightreading_done
    sightreading_done = True
    return jsonify({'success': True})

@app.route('/reset_sightreading_status', methods=['POST'])
def reset_sightreading_status():
    global sightreading_done
    sightreading_done = False
    return jsonify({'success': True})

def run_main():
    main.mainLoop()
    status["finished"] = True

if __name__ == "__main__":
    # Run mainLoop in a separate thread so Flask can serve requests
    t = threading.Thread(target=run_main)
    t.start()
    app.run(port=5000)
