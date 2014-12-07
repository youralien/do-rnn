starting with notes from visiting the indico guys (thanks madison and alec!)

### some datasets appropriate for RNNs
* reddit text
* adzuna kaggle dataset

###theano-ing 
* first try doing simple models
* then regular neural network from scratch
* try not to reference alec's stuff while doing this

### madison can send us papers for conceptual things: his recommendations (thanks for the email!)
* Plain and simple:  https://github.com/kastnerkyle/minet/blob/master/rnn.py
* More fully featured: https://github.com/IndicoDataSolutions/Foxhound/blob/dev_rnn/foxhound/neural_network/rnn/rnn.py
* "Names to look for cool RNN papers: Ilya Sutskever + Alex Graves + Yoshua Bengio.  When I have a chance to talk with Alec we'll send some more quality material your way."

### in progress
* visualizing what happens over time; laying it out in space
* alec talking about rnn's!
* usually for text
* might be easier to work with modeling a curve - x^2
* recurrent neural network != recursive neural network

### about the diagrams...
* weights (arrows - transformation functions... those are the hidden layers)
* circles - states (outputs of things)

### madison's heuristics/things for optimization:
* adadelta! if you don't know what hyperparams would work. strips out all the hyperparams and makes things work
* good feasibility check

### nn's can overfit really hard
* good gut checK; in order for a problem to be solvable, use your training data as your test data, and get really good results.... but overfitting yo; use a test set!
* dropout helps w/ regularization
* adding l1 and l2 regularization
* early stopping - as soon as you start to see when the test and train accuracy will diverge; check when you're overfitting (and have a good testing set!)

### other notes?
* general model -> fine tune on specific things
* scaling up software infrastructure
* general ML tools!
* transition towards a ML shop as opposed to be a software eng. 

### 11/22/2014 questions!
* weights vs. activity vectors
* n^2 weights and 2^n activity vectors?
* testing our understanding of the toy example
* how to feed in different features (i.e. nodes for bikeshare layers)
