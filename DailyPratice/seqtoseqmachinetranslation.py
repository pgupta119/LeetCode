import torch
import torch.nn as nn
import torch.optim as optim
from torchtext.datasets import Multi30k # dataSet german to englu
from torchtext.data import Field, BucketIterator  # preprocessing
import numpy as np
import spacy # Tokenization
from torch.utils.tensorboard import SummaryWriter  # loss and 

spacy_ger=spacy.load('de')
spacy_eng=spacy.load('en')

def tokenizer_gen(text):
    return [tok.text for tok in spacy_gen.tokenizer(text))]

def tokenizer_eng(text):
    return [tok.text for tok in spacy_eng.tokenizer(text)]

#example of Tokenizer
#[" Hello I am a Hero "] -> ["Hello","I", "am", "a","Hero"]


german=Field(tokenize=tokenize_gen,lower=True,
              init_token='<sos>',eos_token='<eos' )

english=Field(tokenize=tokenize_eng, lower=True,
              init_token='<sos>',eos_token='<eos>')
#Spilt the data  into train, validate and  test
train_data,validaton_data,test_data=Multi30k,splits(exts=('.de','.en'),fields=(german, english))

#train the german vocab
german.built_vocab(train_data,max_size=10000, min_freq=2)

#train the english vocab
english.built_vocab(train_data,max_size=10000, min_freq=2)

class Encoder(nn.Module):
    #input_size as vocabulary
    #embedding_size
    #hidden_layers
    #number fo layers
    #Dropout
    def __init__(self,input_size,embedding_size,hidden_layer,num_layers,p):
        super(Encoder,self).__init__() #why?
        self.hidden_layer=hidden_layer
        self.num_layers=num_layers
        
        self.dropout=nn.Dropout(p)
        self.embedding=nn.Embedding(input_size, embedding_size)
        self.rnn=nn.LSTM(embeddding_size,hidden_size, num_layers, droput=p )
    
    def forward(self,x)
    #x is vector of indices
    #x shape:(seq_length, N)
    embeddding=self.dropout(self.embedding(x))
    #embedding  shape : (seq_length, N, embedding_size)
    output,(hidden, cell)=self.rnn(embedding)
     return hidden,cell


         

class Decoder(nn.Module):
    def __init__(Self, input_size,embedding_sie, hidden_layer, output_size, num_layer, p):
        super(Encoder,self).__init__() #why?
        self.hidden_layer=hidden_layer
        self.num_layers=num_layers
        
        self.dropout=nn.Dropout(p)
        self.embedding=nn.Embedding(input_size, embedding_size)
        self.rnn=nn.LSTM(embeddding_size,hidden_size, num_layers, droput=p )
    
    def forward(self,x)
    #x is vector of indices
    #x shape:(seq_length, N)
    embeddding=self.dropout(self.embedding(x))
    #embedding  shape : (seq_length, N, embedding_size)
    output,(hidden, cell)=self.rnn(embedding)
     return hidden,cell



class Seq2Seq(nn.module):
    #combine Encoder and Decoder