w = "This movie is not so bad"

split_word = w.split(' ')

w_output = []

for idx, word in enumerate(split_word):
    if word == "not":
      for i in split_word[idx+1:]:
         if i =="bad":
            w_output = split_word[:idx] + ["good"]
            break
         else:
            w_output = split_word

print(w_output)
