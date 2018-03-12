# diffbot article api

A simple wrapper for the Diffbot Article API.

## installation
`pip install diffbot_api`

## example usage

```
from article_parser import ArticleAPI

parser = ArticleAPI(token='YOUR DIFFBOT TOKEN')

url = 'https://www.nytimes.com/2018/03/10/world/asia/china-xi-jinping-term-limit-explainer.html?&moduleDetail=section-news-1&action=click&contentCollection=Asia%20Pacific&region=Footer&module=MoreInSection&version=WhatsNext&contentID=WhatsNext&pgtype=article'

article = parser.parse(url)

print(article.title) 
>> 'Ending Term Limits for China’s Xi Is a Big Deal. Here’s Why.'
```

## available attributes

* `pageUrl`: the normalized url of the article
* `date`: the date of the article
* `author`: the author(s) of the article
* `siteName`: the name of the site the article is from
* `videos`: any videos contained in the article
* `title`: the title of the article
* `html`: the normalized html of the article
* `text`: the text content of the article
* `tags`: the tags associated with the article
* `publisherCountry`: the country the article is from
