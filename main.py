from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer


def text_summarization_english(text):
    # For Strings
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    # Summarize using sumy TextRank
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, 2)
    text_summary = ""
    for sentence in summary:
        text_summary += str(sentence)

    return text_summary



textEnglish = """A vaccine for the coronavirus will likely be ready by early 2021 but rolling it out safely across India’s 1.3 billion people will be the country’s biggest challenge in fighting its surging epidemic, a leading vaccine scientist told Bloomberg.
India, which is host to some of the front-runner vaccine clinical trials, currently has no local infrastructure in place to go beyond immunizing babies and pregnant women, said Gagandeep Kang, professor of microbiology at the Vellore-based Christian Medical College and a member of the WHO’s Global Advisory Committee on Vaccine Safety.
The timing of the vaccine is a contentious subject around the world. In the U.S., President Donald Trump has contradicted a top administration health expert by saying a vaccine would be available by October. In India, Prime Minister Narendra Modi’s government had promised an indigenous vaccine as early as mid-August, a claim the government and its apex medical research body has since walked back.
"""

summaryEnglish = text_summarization_english(textEnglish)
print("English Text")
print("Total Karakter : " , len(textEnglish))
print(summaryEnglish)
print("Total Karakter : " , len(summaryEnglish))

