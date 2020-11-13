# Ardorgram

A tool to visualize your relationships ardor on Telegram

## The story

Lately, I've been accused of being too much sensitive in my long-distance relationship with my partner. So she came up with an idea; if you know how to code, then visualize usage of love words in our daily chat on Telegram. We usually use telegram for daily chats, so I began searching the web for a probable solution. I searched for keywords such as "visualize tool for telegram", "word graph telegram", and I found some good resources but they all had security problems or they did not support custom languages or custom words so I decided to do it myself.

## Ingredients

First of all, I decided to study some technologies and facts that I should consider using in my project, here you can read a summary of two of them.
1. Semantic analysis :
In linguistics, semantic analysis is the process of relating syntactic structures, from the levels of phrases, clauses, sentences, and paragraphs to the level of the writing as a whole, to their language-independent meanings. And yes if you don't want to be on the wrong side of the road you need to spend more time searching about this part. But as we speak Persian in our chat and there are no good resources for semantic analysis in Persian, I decided to postpone this part to future updates, but for now, I simply found some love words by searching those junky "love word to your partner to make him or her love you more" websites and I imported them into my lovewords.CSV, feel free to add your own languages or love words to it.
2. Visualization tool:
using python for this project, I had a handful of libraries and chart types to visualize data and my choice was Plotly, which is open-source, easy to use and I suppose it has an acceptable GUI. 

## Getting started

1. Clone the project.
2. Download dependencies such as pandas and NumPy.
3. Add your own love words to lovewords.CSV
4. Run the project.
5. Insert the result.json path in which you save your telegram exported chat. Don't forget to add result.json at the end of your path.
6. Wait for the process to get completed.
7. Boom! your ardor graphs are ready. 

## Data security

As I mentioned earlier, one of my biggest concerns was safety so I decided to do the whole process offline without telegram API. I also didn't put a link to the precompiled project to show you my level of concern ;-).

## troubleshooting 
1. You might get the error

```raise ImportError( ImportError: Plotly express requires pandas to be installed)```

It's a bug related to Windows users and you can resolve it by just downgrading your NumPy.
2. You might not get the results on Chrome browser -I don't know why- to resolve this, just change your default browser to Firefox if you have it. 

## Disclaimer
Nothing is constant but change; I found no academic research showing any coherence between love words in chat and real-life relationship status. but I think relativity is enough. My project does not measure your absolute relationship quality, but it gives you an image of your ups and downs in the online world.



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update the tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
