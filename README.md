# HMM
Hidden Markov Model
This project is about Part Of Speech Tagging. (POS). This project is about assigning a tag to each word used in a sentence. For 
assigning tagging we use the Hidden Markov Model, which consists of Transitional Probabilities along with Emission probabilities.
This is a 2 step process, they are :
  1. We build a HMM model from a corpus provided. The model consists of transition probabilities as well as emission probability.
  2. Use this model to assign tags to each word in a test sentence. 

During the second step, we may seen unseen data which may not have emission probability, for such cases, we make use of the 
transition probability. ie, we assign the tag of the current word to be the tag which has the highest probability from the previous state.
This project is in Python.
