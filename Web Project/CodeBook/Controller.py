import web

urls = (
    '/','home'
)

render = web.template.render("./Views/Templates/")
app = web.application(urls,globals())

#Classes/Routes

class home:
    def GET(self):
        return render.home()

if __name__ == '__main__':
    app.run()
