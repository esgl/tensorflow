import tensorflow as tf 
c = tf.constant("Hello, distributed Tensorflow")
server = tf.train.Server.create_local_server()
sess = tf.Session(server.target)
sess.run(s)