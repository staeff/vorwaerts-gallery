# Backlog

## Return all ads belonging to a page as query set

```py
>>> page1_ads = ClassifiedAd.objects.filter(newspaper_page=NewspaperPage.objects.get(pk=1))
>>> len(page1_ads)
```

If we have a foreign key we can use select_related or use snake case to fetch the related fields in a single query.

* make swipe navigation of single page and single ad
* group pages into issues

* Use whitenoise with image cdn

* wikimedia rest api on this day: Wikimedia REST API - https://en.wikipedia.org/api/rest_v1/#/Feed/aggregatedFeed

* Filter images to get only the useful ones. Seems like 618/618 is the width value for the narrow column.
* What are the results when I filter for this? Should I still try to figure a heuristic value for height?
  As little as 155 are valid ads, so there might be more noise here.

* Not valid

http://127.0.0.1:8000/vorwaerts/ads/27/ - 396x

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
