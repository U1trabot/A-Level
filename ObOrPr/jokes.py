import json, random, time

with open('reddit_jokes.json', 'r') as f:
    joke_dict = json.load(f)

jokeList = list()

for joke in joke_dict:
    jokeList.append([joke['title'],'\n',joke['body']])

def main():
    joke = random.choices(jokeList)
    print ("".join(joke[0]))
    input()
    time.sleep(1)
    print()
    main()
main()