import tornado.web

D={
    "alice": {
        "name" : "Alice Smith", 
        "dob" : "Jan. 1",
        "email": "alice@example.com",
        "profile": "/static/alice.jpg"
    },
    "bob": {
        "name" : "Bob Jones", 
        "dob" : "Dec. 31",
        "email": "bob@bob.xyz",
        "profile": "/static/bob.jpg"
    },
    "carol": {
        "name" : "Carol Ling", 
        "dob" : "Jul. 17",
        "email": "carol@example.com",
        "profile": "/static/carol.jpg"
    },
    "dave": {
        "name" : "Dave N. Port", 
        "dob" : "Mar. 14",
        "email": "dave@dave.dave",
        "profile": "/static/dave.jpg"
    },
}

# Stuff from in class that I'll take the time to understand later.
#.............................................

class ProfileHandler(tornado.web.RequestHandler):
    def get(self):
        L = self.request.path.split("/")
        uname = L[2]
        info = D[uname]
        self.render( "profilepage.html", name=info["name"], dateOfBirth=info["dob"], email=info["email"], profilePic=info["profile"])