import textract

text = textract.process('sample.pdf')

text = text.decode("utf8")

print(text)
