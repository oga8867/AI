

import pandas as pd
import numpy as np
from keras.preprocessing.image import *
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import random
import os
import keras


fm = keras.datasets.fashion_mnist
(trainImage, trainLabel), (testImage, testLabel)= fm.load_data()

# 검증데이터 분리
trainImage, valImage= train_test_split(trainImage, test_size=0.1)
trainLabel, valLabel = train_test_split(trainLabel,test_size=0.1)

# 데이터 전처리
trainImage=trainImage.reshape(54000,784).astype("float32")/255.0
valImage=valImage.reshape(6000,784).astype("float32")/255.0
trainLabel=np_utils.to_categorical(trainLabel)
testImage=testImage.reshape(10000,784).astype("float32")/255.0
testLabel=np_utils.to_categorical(testLabel)
valLabel=np_utils.to_categorical(valLabel)

print(trainImage.shape)
print(trainLabel.shape)
print(valImage.shape)
print(valLabel.shape)
print(testImage.shape)
print(testLabel.shape)

#2 모델 구성

model = Sequential()
model.add(Dense(units = 1024, input_dim = 28*28, activation = 'relu'))
model.add(Dense(units = 512, input_dim = 28*28, activation = 'relu'))
model.add(Dense(units = 256, input_dim = 28*28, activation = 'relu'))
model.add(Dense(units = 128, input_dim = 28*28, activation = 'relu'))
model.add(Dense(units = 64, input_dim = 28*28, activation = 'relu'))
model.add(Dense(units = 32, input_dim = 28*28, activation = 'relu'))
model.add(Dense(units = 10, activation = 'softmax'))

#3 모델 학습과정 설정
model.compile(loss = 'categorical_crossentropy', optimizer = 'sgd', metrics = ['accuracy'])

#4. 모델 학습
hist = model.fit(trainImage, trainLabel, epochs = 10, batch_size = 32,
                 validation_data=(valImage,valLabel))

#5. 모델평가
res = model.evaluate(testImage, testLabel, batch_size=32)

print("cost:"+str(res[0]))
print("accuracy:"+str(res[1]))


import matplotlib.pyplot as plt
figs, loss_ax = plt.subplots()
loss_ax.plot(hist.history['loss'],'y',label='train loss')
loss_ax.plot(hist.history['val_loss'],'r',label='val loss')

loss_ax.legend(loc='upper left')
loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')

plt.show()


# 모델 예측
xhat = testImage
yhat = model.predict(xhat)

category={0:"T-shirt/top", 1: "Trouser", 2: "Pullover" , 3:"Dress" , 4:"Coat", 5:"Sandal", 6:"Shirt", 7:"Sneaker", 8:"Bag",9:"Ankle boot"}

import pandas as pd

index=[]
ori=[]
pred=[]

for i in range(0, testLabel.shape[0]):
    if np.argmax(yhat[i]) != np.argmax(testLabel[i]):
        index.append(i)
        ori.append(category[np.argmax(testLabel[i])])
        pred.append(category[np.argmax(yhat[i])])
res=pd.DataFrame({"label":ori,
                  "predict":pred,
               },
                 index=index)
print(res)



# 틀린 예측 사진 확인하기

ver=res.sample(n=8).index

# %matplotlib notebook

cnt=0
for n in ver:
    cnt+=1
    plt.subplot(4,4,cnt)
    plt.imshow(testImage[n].reshape(28,28), cmap='Greys')
    t="label:"+str(res['label'][n])+"\npred:"+str(res['predict'][n])
    plt.title(t)
plt.tight_layout()
plt.show()