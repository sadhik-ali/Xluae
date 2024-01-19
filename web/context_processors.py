from .models import EducationalPrograms
from .models import SocialMedia


def main_context(request):
    programs = EducationalPrograms.objects.all()
    social = SocialMedia.objects.all()
    return {"programs": programs, "social": social, "domain": request.META["HTTP_HOST"]}
