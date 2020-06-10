from gensim.summarization.summarizer import summarize


def summarizer(text):
    try:
        summary = summarize(str(text), word_count=100)
        if summary:
            return summary
    except Exception as e:
        return "Error Encountered!!!"
