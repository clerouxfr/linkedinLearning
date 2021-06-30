import httplib2


class HTTPConnection:


    def __init__(self, langue):
        self.langue = langue

    def get(self, page):
        h = httplib2.Http(".cache")
        self.url = "http://{0}.wikipedia.org/wiki/{1}".format(
            self.langue,
            page.replace(" ", "_")
        )
        reponse, contenu = h.request(self.url, "GET")
        print(reponse)

HTTPConnection("fr").get("Kruder und Dorfmeister")
