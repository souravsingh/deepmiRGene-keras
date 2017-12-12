from keras.models import Model
from keras.layers import Conv2D, MaxPooling2D, Input, Dropout, Conv2DTranspose, LSTM, Add
import numpy as np





model.add(Dropout(0.1))
model.add(LSTM(128, return_sequences=True, input_shape=(max_len, N_values)))
model.add(Dropout(0.1))
model.add(LSTM(128, return_sequences=True, input_shape=(max_len, N_values)))
model.add(Dropout(0.1))
model.add(LSTM(128, return_sequences=True, input_shape=(max_len, N_values)))
model.add(Dropout(0.1))
model.add(LSTM(128, return_sequences=True, input_shape=(max_len, N_values)))
model.add(LSTM(128, return_sequences=True, input_shape=(max_len, N_values)))
model.add(Dropout(0.1))
model.add(LSTM(128, return_sequences=True, input_shape=(max_len, N_values)))
model.add(LSTM(128, return_sequences=True, input_shape=(max_len, N_values)))
model.add(Dropout(0.1))
model.add(LSTM(128, return_sequences=True, input_shape=(max_len, N_values)))
