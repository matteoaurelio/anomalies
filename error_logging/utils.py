from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer


def find_and_summarize_error(text, keyword, context_size=3):
    # Split the text into lines
    lines = text.splitlines()

    # Find the index of lines containing the keyword
    error_lines_indices = [index for index, line in enumerate(lines) if keyword.lower() in line.lower()]

    # If no keyword is found, return None or the entire text
    if not error_lines_indices:
        return {"message": text}
    
    # Extract the context of the error
    context_lines = []
    for index in error_lines_indices:
        start = max(0, index - context_size)
        end = min(len(lines), index + context_size + 1)
        context_lines.extend(lines[start:end])

    # Join the context lines into a single string
    error_context = "\n".join(set(context_lines))

    # Summarize the error context using sumy
    parser = PlaintextParser.from_string(error_context, Tokenizer("english"))
    summarizer = Summarizer()

    # Summarize the error with the top 3 sentences
    summary = summarizer(parser.document, 2)

    # Return the summary
    output = "\n".join(str(sentence) for sentence in summary)
    return output