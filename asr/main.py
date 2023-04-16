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


@app.route('/api/asr', methods=['GET','POST'])
def asr():
    decoderVoix = EncoderDecoderASR.from_hparams(source="speechbrain/asr-crdnn-commonvoice-fr",
                                                 savedir="pretrained_models/asr-crdnn-commonvoice-fr")

    if 'audio' in request.files:
        f = request.files['audio']
        filePath = os.getcwd() + "\\voixAutorise\\final_record.wav"
        f.save(filePath)
        print(decoderVoix.transcribe_file(os.getcwd() + "\\voixAutorise\\final_record.wav"))
        return jsonify({'asr': decoderVoix.transcribe_file(os.getcwd() + "\\voixAutorise\\final_record.wav")})
    return 'Aucun fichier audio n\'a été envoyé'


if __name__ == '__main__':
    #decoderVoix = EncoderDecoderASR.from_hparams(source="speechbrain/asr-crdnn-commonvoice-fr",
    #                                             savedir="pretrained_models/asr-crdnn-commonvoice-fr")
    #print(decoderVoix.transcribe_file(os.getcwd() + "\\voixAutorise\\final_record.wav"))
    app.run(host='0.0.0.0')

# auth = False
# for x in authentifier :
#    score, prediction = authentification.verify_files("C:\\Users\\burge\\PycharmProjects\\asr\\new_audio.wav", x)
#    if(prediction):
#        auth = True
#        decoderVoix.transcribe_file("C:\\Users\\burge\\PycharmProjects\\asr\\new_audio.wav")
#        print(decoderVoix.transcribe_file("C:\\Users\\burge\\PycharmProjects\\asr\\voixAutorise\\testJerome.wav"))
#        print(auth, x)
#        break
