
from sentences import get_determiner,get_noun,get_verb,get_prepositional_phrase,get_adjective,get_preposition
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

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # 1. Test the single determiners.
    single_noun = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(11):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_noun(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_noun

    # 2. Test the plural determiners.

    plural_noun = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_noun(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_noun

def test_get_verb():
   # 1. Test the single determiners.
    past_verb = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(11):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_verb(1,"past")

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in past_verb

    # 2. Test the plural determiners.

    present_verb = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(11):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_verb(1,"present")

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in present_verb
    
    # 3. Test the plural determiners.

    present_verb_many = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(11):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_verb(2,"present")

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in present_verb_many



     # 4. Test the plural determiners.

    future_verb = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(11):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_verb(1,"future")

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in future_verb


def test_get_preposition():
    # 1. Test the prepositions.
    prepositions= ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    # This loop will repeat the statements inside it 31 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(31):

        # Call the get_preposition function which
        # should return a  preposition
        word = get_preposition()


        # Verify that the word returned from get_preposition
        # is one of the words in the preposition list.
        assert word in prepositions

def test_get_preposition_phrase():
    # 1. Test lenght singular prepositions.
    
    phrase1=get_prepositional_phrase(1).split(" ")
    assert len(phrase1)==4

    # 2. Test lenght plural prepositions.
    
    phrase2=get_prepositional_phrase(2).split(" ")
    assert len(phrase2)==4

    #validating prepositions

    prepositions= ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    for _ in range(31):
        # Call the get_preposition function which
        # should return a  preposition
        word = phrase1[0]
        # Verify that the word returned from get_preposition
        # is one of the words in the preposi
        assert word in prepositions

    #validating determiner

     # 1. Test the single determiners.
    single_determiners = ["a", "one", "the"]
    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = phrase1[1]

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = phrase2[1]

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

       
    # test Adjetives

    
    adjetives = ["good","new","first","last","long","great","little","own","other","old","right","big","high","different","small","large","next","early","young","important","few","public","bad","same","able"]
    # This loop will repeat the statements inside it 26 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(26):

        # Call the get_adjetive function which
        # should return a single adjetive.
        word = phrase1[2]

        # Verify that the word returned from get_adjetive
        # is one of the words in the adjetives list.
        assert word in adjetives


    #test Nouns

    # 1. Test the single determiners.
    single_noun = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(11):

        # Call the get_determiner function which
        # should return a single determiner.
        word = phrase1[3]

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_noun

    # 2. Test the plural determiners.

    plural_noun = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = phrase2[3]

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_noun




def test_get_adjetive():
    # 1. Test the adjetives.
    adjetives = ["good","new","first","last","long","great","little","own","other","old","right","big","high","different","small","large","next","early","young","important","few","public","bad","same","able"]
    # This loop will repeat the statements inside it 26 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(26):

        # Call the get_adjetive function which
        # should return a single adjetive.
        word = get_adjective()

        # Verify that the word returned from get_adjetive
        # is one of the words in the adjetives list.
        assert word in adjetives
   

    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])