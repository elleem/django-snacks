from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["snacks"] = [
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/en/e/e9/First_Single_Volume_Edition_of_The_Lord_of_the_Rings.gif",
                "title": "The Lord of the Rings Trilogy",
                "description": "Middle earth mission to Mount Doom.",
                "reference_url": "https://en.wikipedia.org/wiki/The_Lord_of_the_Rings"
            },
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/en/b/bd/H2G2_UK_front_cover.jpg",
                "title": "The Hitchhiker's Guide to the Galaxy",
                "description": "Arthur Dent never throws in the towel.",
                "reference_url": "https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy"
            },
            {
                "image_url": "https://en.wikipedia.org/wiki/Frankenstein#/media/File:Frankenstein_1818_edition_title_page.jpg",
                "title": "Frankenstein",
                "description": "Dr. Frankenstein fixates on fashioning life from fragments, ultimately forsaking his forlorn creature.",
                "reference_url": "https://en.wikipedia.org/wiki/Frankenstein"
            },
            {
                "image_url": "https://en.wikipedia.org/wiki/File:Dune-Frank_Herbert_(1965)_First_edition.jpg",
                "title": "Dune",
                "description": "Destiny, devotion, and the balance between ecology and empire.",
                "reference_url": "https://en.wikipedia.org/wiki/Dune_(novel)"
            },
            {
                "image_url": "https://en.wikipedia.org/wiki/Nineteen_Eighty-Four",
                "title": "1984",
                "description": "'War is Peace.' 'Freedom is Slavery.' 'Ignorance is Strength.'",
                "reference_url": "https://en.wikipedia.org/wiki/File:1984first.jpg"
            },
            {
                "image_url": "https://en.wikipedia.org/wiki/File:Fahrenheit_451_1st_ed_cover.jpg",
                "title": "Fahrenheit 451",
                "description": "Intellectual freedom is forever worth fueling.",
                "reference_url": "https://en.wikipedia.org/wiki/Fahrenheit_451"
            },
        ]

        return context

class AboutView(TemplateView):
    template_name = 'about.html'