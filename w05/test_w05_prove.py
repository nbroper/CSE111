from w05_prove import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest

def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)
        
        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(quantity)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners
#########################################################################################################
def test_get_noun():
    #1 Test the single nouns.

    single_nouns = ["bird", "boy", "car", "cat", "child",
     "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(11):

        #quantity = random.randint(1)
        noun = get_noun(1)
        assert noun in single_nouns

    plural_nouns = ["birds", "boys", "cars", "cats", "children",
         "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(11):

        quantity = random.randint(2,11)
        noun = get_noun(quantity)
        assert noun in plural_nouns
###########################################################################################################
def test_get_verb():
 
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
     "ran", "slept", "talked", "walked", "wrote"]

    single_present_verbs = ["drink", "eat", "grow", "laugh", "think",
            "run", "sleep", "talk", "walk", "write"]

    plural_present_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
            "runs", "sleeps", "talks", "walks", "writes"]

    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
            "will think", "will run", "will sleep", "will talk",
            "will walk", "will write"]

    # for _ in range(6):
         
    #     #assert get_verb in single_present_verbs

    #     verb = get_verb(quantity, tense)
    #     assert verb in plural_present_verbs
    for _ in range(3):
            
        #sets quantity randomly for single or plural
        quantity = random.randint(1, 10)
        tense = random.choice(['past', 'present', 'future'])

        if tense == 'past':
            assert get_verb(quantity, tense) in past_verbs

        elif tense == 'present' and quantity == 1:
            assert get_verb(quantity, tense) in single_present_verbs

        elif tense == 'present' and quantity != 1:
            assert get_verb(quantity, tense) in plural_present_verbs

        else:
            assert get_verb(quantity, tense) in future_verbs


#################################################################################

def test_get_preposition():

    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    for _ in range(15):
    
        preposition = random.choice(prepositions)
        assert get_preposition in prepositions

###################################################################################

def test_get_prepositional_phrase():

    quantity = random.randint(1, 10)
    words = 3

    for _ in range(10):

        list = get_prepositional_phrase(quantity)
        word_list = list.split()
        number_of_words = len(word_list.split())
        assert number_of_words in words

        


pytest.main(["-v", "--tb=line", "-rN", __file__])   