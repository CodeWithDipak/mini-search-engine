'''
Author - CodeWithDipak
Date - 7 nov 2020
purpose - Practice Purpose
'''

'''
make a Search Engine - 
You have given few sentences as a list(python list of sentences). 
Take a query string as an input from the user.
You have to pull out the sentences matching this query inputted by the user in the decreasing order of relevance.
Most relevant sentences is the one with maximum number of matching words wth the query.
'''


def max_repetition(sentence1, sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == '__main__':
    sentences = ["Dipak is a hacker", "Dipak is black hat hacker",
                 "Kiran is good boy", "Dipak is able to hack any system"]
    query = input("Enter the query you want to search:\n")
    scores = [max_repetition(query, sentence) for sentence in sentences]
    # print(scores)
    sortSentScores = [queries for queries in sorted(
        zip(scores, sentences), reverse=True)]
    # print(scoreSentScores)
    for value, search in sortSentScores:
        print(f"{search}, is having {value} search results.\n")
