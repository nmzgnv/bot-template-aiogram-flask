from wtforms import TextAreaField
from wtforms.widgets import TextArea
from flask_admin.contrib.sqla import ModelView


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += " ckeditor"
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


class CKEditorModelView(ModelView):
    column_list = ['id', 'value']
    can_delete = False
    can_create = False
    form_overrides = dict(value=CKTextAreaField)

    create_template = 'text_model_view.html'
    edit_template = 'text_model_view.html'
