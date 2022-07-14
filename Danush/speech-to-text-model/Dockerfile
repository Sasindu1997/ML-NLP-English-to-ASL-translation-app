FROM tensorflow/tensorflow:latest-gpu-jupyter
WORKDIR /speech-to-text-model
RUN python -m pip install --upgrade pip
RUN pip install numpy
RUN pip install librosa
RUN pip install ipython
RUN pip install matplotlib
RUN #pip install sounddevice
#RUN pip install -r requirements.txt
#CMD ["python", "src/speech_to_text_model.py"]