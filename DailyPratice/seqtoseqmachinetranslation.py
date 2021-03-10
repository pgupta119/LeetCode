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

    def forward(self,x):
    #shape of [sequence length,batch_size][26,32]

    #shape of [sequence length,batch_size][26,32,300] embedding_size
        embedding=self.dropout(self.embedding(x))

    #Shape --> outputs (26, 32, 1024) [Sequence_length , batch_size , hidden_size]
    #Shape --> (hs, cs) (2, 32, 1024) , (2, 32, 1024) [num_layers, batch_size size, hidden_size]
        outputs, (hidden_state, cell_state) = self.LSTM(embedding)

    return hidden_state, cell_state

class DecoderLSTM(nn.Module):
    def __init__ (self, input_size,embedding_size,hidden_size, num_layers, p, output_size):
        super(DecoderLSTM,self).__init__()


        self.input_size=input_size
        self.output_size=output_size
        self.embedding_size=embedding_size
        self.hidden_layer=hidden_layer
        self.num_layers=num_layers
        self.embedding=nn.Embedding(self.input_size,self.embedding_size)
        self.dropout=Dropout(p)
        self.tag=True
        self.LSTM=nn.LSTM(Self.embedding_size, num_layers,droput=p)
        self.fc=nn.Linear(self.hidden_size,self.output_size)


    def forward(self, hidden_state, cell_state):

        x=x.unsqueezw(0)
        embedding=self.droput(self.embedding(x))
        outputs, (hidden_state,cell_state)=self.LSTM(embedding,(hidden_state,cell_state))
        predictions=self.fc(outputs)
        predictions=predictions.squeeze(0)

    return  predictions, hidden_state, cell_state




class seq2seq(nn.Module):
    def __init__(self, source, target, tfr=0.5):
        batch_size=source.shape[1]
        target_len=target.shape[0]
        target_vocab_size=len(english.vocab)
        outputs=torch.zeros (target_len,batch_size,target_vocab_size).to(device)
        hidden_state_encoder,cell_state_encoder=self.DecoderLSTM        

    







        

#create batches of training, testing, and validation data using iteratorrs



