# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import utils
nlines = len(open("birth_dev.tsv", encoding='utf-8').readlines())
total, correct = utils.evaluate_places("birth_dev.tsv", ["London" for _ in range(nlines)])
print("total: " + str(total))
print("correct: " + str(correct))
print("percent correct: " + str(correct / total))
