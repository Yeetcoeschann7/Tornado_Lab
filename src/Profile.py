import tornado.web
import base64
import json

D={
    "alice": {
        "name" : "Alice Smith", 
        "dob" : "2001-01-01",
        "email": "alice@example.com",
        "profile": "/static/alice.jpg"
    },
    "bob": {
        "name" : "Bob Jones", 
        "dob" : "1987-10-31",
        "email": "bob@bob.xyz",
        "profile": "/static/bob.jpg"
    },
    "carol": {
        "name" : "Carol Ling", 
        "dob" : "1993-07-17",
        "email": "carol@example.com",
        "profile": "/static/carol.jpg"
    },
    "dave": {
        "name" : "Dave N. Port", 
        "dob" : "1983-03-14",
        "email": "dave@dave.dave",
        "profile": "/static/dave.jpg"
    },
}

class ProfileHandler(tornado.web.RequestHandler):
    def get(self):
        L = self.request.path.split("/")
        uname = L[2]
        info = D[uname]
        self.render("profilepage.html", user = str(uname), name=info["name"], dateOfBirth=info["dob"], email=info["email"], profilePic=info["profile"])

    def post(self):
        J=json.loads(self.request.body)

        fullName = J["fullName"]
        email = J["email"]
        uname = J["uname"]
        pic = J["pic"]

        # Import profile pic and decide file type
        ppic = base64.b64decode(pic)
        imgType = "NA"
        if ppic[0] == 0x89:
            imgType = "png"
        elif ppic[0] == 0xff:
            imgType = "jpeg"

        info = D[uname]

        print("WE GOT:", uname, fullName, email, ppic[:20])
        resp={"ok": True}
        
        if fullName != "":
            info["name"] = fullName
        if email != "":
            info["email"] = email

        if imgType != "NA": #if image type is valid (png or jpg) change image
            print("FILE IS VALID!")
            info["profile"] = f"data:image/{imgType};base64," + str(pic)
        else:
            print("FILE IS BAD!")

        self.write(json.dumps(resp))