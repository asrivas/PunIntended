#import nltk

# given a string,
# if it is a title that exists on gutenberg, pull that text and use 
# it to seed the markov process
# otherwise, treat as a google query
# we could use a cache here
def generate_text(query):
    """
    if query in gutenberg.titles:
        seed_text = gutenberg.get(query)

    else:
        seed_text = google.search(query)
        

    p = markov.seed(seed_text)
    return markov.generate()
    """

    return None
