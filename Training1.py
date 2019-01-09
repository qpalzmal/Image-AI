from imageai.Prediction.Custom import ModelTraining

model_trainer = ModelTraining()

# sets model type to "ResNet", other options are "Sqeezenet", "InceptionV3", DenseNet"
model_trainer.setModelTypeAsResNet()

# sets data directory where the dataset is stored
model_trainer.setDataDirectory("idenprof")

model_trainer.trainModel(num_objects=10,  # the number of different type of professionals in the dataset
                         num_experiments=200,  # number of times model trainer studies the images
                         enhance_data=True,  # creates modified copies of images to improve accuracy
                         batch_size=32,  # number of images model will study at once
                         show_network_summary=True)  # shows the structure of model type used

