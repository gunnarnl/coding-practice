"""
[Medium]

This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""

# Okay I don't know how to do this at all so I'm going to look it up.

#How some other guy solved this:
def solution(sample_generator):
    sample_count = 0
    selected_sample = None
    for sample in sample_generator:

        sample_count += 1
        if random.random() <= 1.0 / sample_count:
            selected_sample = sample

    return selected_sample

#Basically for each sample, it's updating the probability that the new sample will be chosen over the an old one. I guess I didn't totally understand the problem, but basically the question assumes that a stream is just a series of elements that the program "sees" one by one, and so it doesn't have access to all samples at once.
