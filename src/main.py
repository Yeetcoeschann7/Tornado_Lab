import asyncio
import os, os.path
import tornado.web
import Index, Profile
import os

HTMLDIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..","html"
    )
)

def makeApp():
    endpoints=[
        ("/",Index.Handler),
        ("/profile/.*",Profile.ProfileHandler)
    ]
    app = tornado.web.Application(
        endpoints,
        static_path=HTMLDIR
    )
    app.listen(8000)
    print("===========================================")
    print("Point your browser at http://localhost:8000")
    print("===========================================")
    return app

if __name__ == "__main__":
    app = makeApp()
    asyncio.get_event_loop().run_forever()   
