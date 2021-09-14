import tensorflow as tf

# Convert the model
converter = tf.lite.TFLiteConverter.from_saved_model('/home/mlst01/CarCarder/tensorflow_object_detection_ssdmobilenet/train_0620_V10/tflite/saved_model/') # path to the SavedModel directory
tflite_model = converter.convert()

# Save the model.
with open('/home/mlst01/CarCarder/tensorflow_object_detection_ssdmobilenet/train_0620_V10/tflite/model.tflite', 'wb') as f:
  f.write(tflite_model)