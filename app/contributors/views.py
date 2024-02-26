from django.core.exceptions import ValidationError
from django.views.generic import FormView

from contributors.exceptions import ValidationRepositoryUrlError
from contributors.forms import RepositoryForm
from contributors.services import TopRepositoriesService


class TopContributorsView(FormView):
    """Form View for getting top 5 contributors of GitHub repository"""
    template_name = "index.html"
    form_class = RepositoryForm

    def form_valid(self, form: RepositoryForm):
        validated_url = form.cleaned_data.get('repository_url')
        service = TopRepositoriesService(url=validated_url)
        try:
            top_repositories = service.process()
            context = self.get_context_data(form=RepositoryForm())
            context.update({
                'current_repository_url': validated_url,
                'top_repositories': top_repositories,
            })
            return self.render_to_response(context)
        except ValidationRepositoryUrlError as error:
            form.add_error(field='repository_url',
                           error=ValidationError(error.message))
            return self.form_invalid(form)
