train_datagen=ImageDataGenerator(rescale=1./225,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)
test_datagen=ImageGenerator(rescale=1./225)