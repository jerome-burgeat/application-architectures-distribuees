import glob
from speechbrain.pretrained import SpeakerRecognition
from speechbrain.pretrained import EncoderDecoderASR

authentification = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="pretrained_models/spkrec-ecapa-voxceleb")
authentifier = glob.glob("/\\voixAutorise\\*.wav")

decoderVoix = EncoderDecoderASR.from_hparams(source="speechbrain/asr-crdnn-commonvoice-fr", savedir="pretrained_models/asr-crdnn-commonvoice-fr")
auth = False

print(decoderVoix.transcribe_file("C:\\Users\\burge\\PycharmProjects\\asr\\voixAutorise\\testReda.wav"))

#for x in authentifier :
#    score, prediction = authentification.verify_files("C:\\Users\\burge\\PycharmProjects\\asr\\new_audio.wav", x)
#    if(prediction):
#        auth = True
#        decoderVoix.transcribe_file("C:\\Users\\burge\\PycharmProjects\\asr\\new_audio.wav")
#        print(decoderVoix.transcribe_file("C:\\Users\\burge\\PycharmProjects\\asr\\voixAutorise\\testJerome.wav"))
#        print(auth, x)
#        break