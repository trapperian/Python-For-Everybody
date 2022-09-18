text = "X-DSPAM-Confidence:    0.8475"

x = text.find('0')
y = text.find('5')

new_text = text[x:y]

print(float(new_text))
