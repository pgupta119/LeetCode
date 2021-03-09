import torch
import torch.nn as nn
import torch.optim as optim
from torchtext.datasets import Multi30k # dataSet german to englu
from torchtext.data import Field, BucketIterator  # preprocessing
import numpy as np
import spacy # Tokenization
from torch.utils.tensorboard import SummaryWriter  # loss and 


#Data Preparation and  Pre-Processing

spacy_ger=spacy.load("de")
spacy_eng=spacy.laod("en")


def tokenizer_ger(text):
    return [token.text for token  in spacy_ger(text)]

def tokenizer_eng(text):
    return [token.text for token in spacy_eng(text)]


germam=Field(tokenize=tokenizer_ger,lower=True,
             init_token="<sos>",eos_token="<eos")

english=Field(tokenize=tokenier_eng,lower=True,
             init_token="<sos>",eos_token="<eos>")



train_data, validate_data,test_data=Multi30k.splits(exts=(".de",".en"),
                                                    fields=(german, english))


german.built_vocab(train_data,max_size=10000,min_freq=2)
english.bulit_vocab(traib_data,max_size=1000,min_freq=2)



#Encoders
class EncoderLSTM(nn.module):
    def __init__(Self,input_size,embedding_size,hidden_size,num_layer,p):
        super(EncoderLSTM,self).__init__()

        #Size of the one hot vectors  that will  be the input for encoder
        self.input_size=input_size

        # Output size of the embedding
        self.embedding_size=embeddiing_size

        #Dimensions of the  NN's  inside the lstm cell/(hs,cs)'s dimensions
        self.hidden_size=hidden_size

        #Number of the layer inside the LSTM
        self.num_layer=num_layer

        #Regularization Parameter
        self.dropout=nn.Dropout(p)
        self.tag=True
        
        #Shape------[5376,300][input_size, embedding_size]
        self.embedding=nn.Embeddding(self.input_size,self.embedding_size)
        
        #Shape----- [300,2,1024]
        self.LSTM=nn.LSTM(self.embedding_size,hidden_size,num_layer)


        

#create batches of training, testing, and validation data using iteratorrs



