import web

urls = (
    '/(.*)/(.*)', 'index'
)

render = web.template.render("./resources/")
app = web.application(urls, globals())

class index:
    def GET(self, name, age):
        if not name:
            name = 'World'
        if not age:
            age = 60
        return render.main(name,age)

if __name__ == "__main__":
    app.run()
