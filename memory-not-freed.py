import tensorflow as tf
for _ in range(100):
   tf.keras.backend.clear_session() # +
   model = tf.keras.Sequential([tf.keras.layers.Dense(10) for _ in range(10)])