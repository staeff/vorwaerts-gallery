# Backlog

## Ideas/Todos

* Filter out wrong images in the data processing pipeline. Sometimes small details were recognized as additional image and therefore redundant
  What are the results when I filter for this? Should I still try to figure a heuristic value for height?
  As little as 155 are valid ads, so there might be more noise here.
  https://botsdam.de/vorwaerts/ads/27/ - 396x
* Use aws cloudfront to host the images (configure with whitenoise?)
* set up makefile to run different configurations (like with herald)
* Deploy to heroku (https://blog.ohidur.com/posts/python/articles/django-heroku-deployment/)
* make swipe navigation of single page and single ad
* group newspaper pages into issues
* Scale large images and have a popup, when displaying the single ad page
* wikimedia rest api on this day: Wikimedia REST API - https://en.wikipedia.org/api/rest_v1/#/Feed/aggregatedFeed

* Make an about page

        <div class="collapse bg-dark" id="navbarHeader">
            <div class="container">
                <div class="row">
                    <div class="col-sm-8 col-md-7 py-4">
                        <h4 class="text-white">About</h4>
                        <p class="text-muted">Dies ist ein Typoblindtext. An ihm kann man sehen,
                            ob alle Buchstaben da sind und wie sie aussehen. Manchmal benutzt man
                            Worte wie Hamburgefonts, Rafgenduks oder Handgloves, um Schriften zu testen.
                            Manchmal Sätze, die alle Buchstaben des Alphabets enthalten - man nennt
                            diese Sätze »Pangrams«. Sehr bekannt ist dieser:
                            The quick brown fox jumps over the lazy old dog. Oft werden in Typoblindtexte auch fremdsprachige Satzteile eingebaut (AVAIL® and Wefox™ are testing aussi la Kerning), um die Wirkung in anderen Sprachen zu testen. In Lateinisch sieht zum Beispiel fast jede Schrift gut aus. Quod erat demonstrandum.
                        </p>
                    </div>
                    <div class="col-sm-4 offset-md-1 py-4">
                        <h4 class="text-white">Links</h4>
                        <ul class="list-unstyled">
                            <li><a href="https://codingdavinci.de/" class="text-white">Coding da Vinci</a></li>
                            <li><a href="https://www.fes.de/archiv-der-sozialen-demokratie/" class="text-white">Archiv der sozialen Demokratie. FES</a></li>
                            <li><a href="https://github.com/staeff" class="text-white">Stephan Klinger</a></li>

                        </ul>
                    </div>
                </div>
            </div>
        </div>


## Learnings

* bit.io does not work as a backend for django, because you need access to a full postgres db and the
  capability to create several tables. With bit.io you only get 1 table, that you can work with.


## Return all ads belonging to a page as query set

```py
>>> page1_ads = ClassifiedAd.objects.filter(newspaper_page=NewspaperPage.objects.get(pk=1))
>>> len(page1_ads)
```

If we have a foreign key we can use `select_related` or use snake case to fetch the related fields in a single query.
