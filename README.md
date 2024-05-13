# CS224N: Natural Language Processing with Deep Learning

This repo contains my coding solutions to CS224N. See the [course website](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1244/index.html).

## Setup

I followed the conda environment setup following each assignment PDF. I skipped GPU training for assignment 4 and 5, and just checked that loss was improving over a few iterations.

For Assignment 4, I needed to `python -m pip install` the following modules from the conda environment:

* sacrebleu
* sentencepiece
* tensorboard

## Summary
CS224N is a good introductory resource to learn about NLP, recurrent neural networks, and attention/transformers. The coding assignments were fairly simple with a lot of emphasis on the writing portion (which I mostly did not do). However, going through the coding assignments and following the lecture slides and notes were sufficient in building my knowledge in NLP.

I think that [Stanford's CS231N Convolutional Neural Networks for Visual Recognition](https://github.com/caojoshua-self-guided-courses/StanfordCS231n) is a better course for learning about neural networks in general. It has more focus on implementation of forward/backward passes and vision is simpler to understand than language in my opinion. It would be better to start with CS231N, and then move on to CS224N if there is specific interest in NLP.
