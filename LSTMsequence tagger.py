# import torch  creatin and training of the neural network
import torch.nn as nn
# import torch function for arthmetical oprations
import torch.nn.functional as F
# import optim for various optimization algorithm
import torch.optim as optim
# using collection  count to stores elements as dictionary keuys, and their counts are stored as dictionary values
from collection import Counter,defaultdict

# create class for LSTMTagger
class LSTMTagger:
    def __init__(self,model_dim,vocab_size,targset_size,device, input_format, output_format, dataset):
        #constructure to build a sequence trigger
        #mode_dim is for  taking the dimension of the model
        #vocab_size is the size of the vocabaluary
        #tagset_size is the size of the target
         
        super(LSTMTagger,self).__init__()
        #Embedding takes dictionary size ,  size of each embedding vector
        self.word_embeddings=nn.Embedding(vocab_size,model_dim)
        # This LSTM takes embedding as input, and outputs  hidden states
        # LTSM with same dimensionality
        self.lstm=nn.LSTM(model_dim,model_dim)
        #The linear layer thats maps from hidden state space to tag space
        self.hidden2tag=nn.Linear(model_dim,target_size)
        # To preventing Overfitting 
        #During training, randomly zeroes some of the elements of the input tensor with probability p using samples from a Bernoulli distribution.
        self.dropout=nn.Dropout(p=0.1)
        self.device=device
        self.input_format=input_format
        self.output_format=output_format
        self.dataset=dataset

    def forward(self,sentence):
        #forward function is defining for how the model will run from input to output
        #1.Embedding
        embeds=self.word_embeddings(sentence)
        #2.output from lstm
        lstm_out,_ =self.lstm(self.dropout(embeds.view(len(sentence),1,-1)))
        #3. Get the tag space
        tag_space=self.hidden2tag(self.dropout(lstm_out.view(len(sentence),-1)))
        #4. Get the Tag Score using softmax
        tag_score=F.log_softmax(tag_space, dim=1)
        return tag_score

    def 






