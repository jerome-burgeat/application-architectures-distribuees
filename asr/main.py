import glob
import os
import os.path
import sys
from flask import Flask, jsonify, request

app = Flask(__name__)
from speechbrain.pretrained import SpeakerRecognition
from speechbrain.pretrained import EncoderDecoderASR

sys.path.append(os.getcwd())

authentification = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb",
                                                   savedir="pretrained_models/spkrec-ecapa-voxceleb")
authentifier = glob.glob("/\\voixAutorise\\*.wav")


@app.route('/api/asr', methods=['POST'])
def asr():
    decoderVoix = EncoderDecoderASR.from_hparams(source="speechbrain/asr-crdnn-commonvoice-fr",
                                                 savedir="pretrained_models/asr-crdnn-commonvoice-fr")

    if 'audio' in request.files:
        f = request.files['audio']
        filePath = os.getcwd() + "\\voixAutorise\\final_record.wav"
        f.save(filePath)
        result = decoderVoix.transcribe_file(os.getcwd() + "\\voixAutorise\\final_record.wav")
        print(result)
        return jsonify(result)
    return 'Aucun fichier audio n\'a été envoyé'


if __name__ == '__main__':
    app.run(host='0.0.0.0')