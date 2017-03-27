# HMM
Hidden Markov Model (HMM)

This project has been done using Python. This is about part of speech tagging (POS Tagging or POST). It assigns a tag to each word which is been used in the sentence. For assigning the tags we use the "Hidden Markov Model" which consists of Transitional Probabilities along with Emission probabilities. 

It consists of the below two steps:-

********* We build the HMM model from the corpus provided to us. The model consists of transition probabilities as well as emission probability. 

·        We use this model to assign tags to each word in a test sentence.

During the second step, we may see unseen data which may not have emission probability, for such cases, we make use of the transition probability. ie, we assign the tag of the current word to be the tag which has the highest probability from the previous state. 
