"""We want to search a set of English language sentences for a keyword.
Every sentence that contains the keyword should be returned."""

text = """Early sales of Apple's new iPhones have lived up to high expectations.

The strong sales mirror growing consumer demand for smartphones with bigger
screens. IDC, a research firm, estimated that at least 20 percent of all
smartphones shipped last year in China, the largest smartphone market in
the world, were five inches or larger. It also predicted that manufacturers
this year would ship more "phablets," or smartphones with screens measuring
at least 5-point-5 diagonal inches, than laptops. \
\
The company on Monday said it sold more than 10 million of the iPhone 6 and
6 Plus models in the first three days they were available in stores. That
is higher than the nine million new iPhones it sold last year in their
first weekend on sale. But some analysts, like Gene Munster of Piper
Jaffray, wondered whether first-weekend sales were still a reliable measure
for consumer demand.

The iPhone sales were on the upper end of financial analysts' expectations,
which ranged from 6 million to the "low teens" of millions of sales.
"""
# >>> def search_text(text, keyword):
# >>>     # ...
#
# The sample text that we want to search for: `iPhone` and `Apple`

def search_text(inputtext, keyword):
    if not inputtext:
        return ''

    sentlist = inputtext.split(".")
    outputlist = []
    for sentence in sentlist:
        if sentence and sentence.find(keyword) >= 0:
            outputlist.append(sentence)

    #return ". ".join(outputlist)
    return outputlist

keyword = 'iPhone'
ret = search_text(text, keyword)
print "Output is: ", ret