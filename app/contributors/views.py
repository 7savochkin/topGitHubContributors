from django.core.exceptions import ValidationError
from django.views.generic import FormView

from contributors.forms import RepositoryForm
from contributors.services import CommonContributorsService


class TopContributorsView(FormView):
    """Form View for getting top 5 contributors of GitHub repository"""
    template_name = "index.html"
    form_class = RepositoryForm

    def form_valid(self, form: RepositoryForm):
        validated_url = form.cleaned_data.get('repository_url')
        service = CommonContributorsService(url=validated_url)
        try:
            service.run()
        except ValidationError as error:
            form.add_error(field='repository_url', error=error)
            return self.form_invalid(form)
        breakpoint()
