"""AccessibleFormMixin: labels/errors are wired to widgets for screen readers."""

from django import forms

from apps.core.forms import INPUT_CLASSES, INPUT_ERROR_CLASSES, AccessibleFormMixin


class SampleForm(AccessibleFormMixin, forms.Form):
    name = forms.CharField(help_text="As shown on the badge.")
    code = forms.CharField()


def test_widgets_get_input_classes():
    form = SampleForm()

    assert form.fields["code"].widget.attrs["class"] == INPUT_CLASSES


def test_help_text_is_linked_with_aria_describedby():
    form = SampleForm()

    assert form.fields["name"].widget.attrs["aria-describedby"] == "id_name_help"
    assert "aria-describedby" not in form.fields["code"].widget.attrs


def test_errors_mark_field_invalid_and_link_error_element():
    form = SampleForm(data={"name": "", "code": ""})

    assert form.is_valid() is False
    attrs = form.fields["name"].widget.attrs
    assert attrs["aria-invalid"] == "true"
    assert attrs["aria-describedby"] == "id_name_help id_name_error"
    assert INPUT_ERROR_CLASSES in attrs["class"]


def test_repeated_validation_does_not_duplicate_ids():
    form = SampleForm(data={"name": "", "code": ""})
    form.full_clean()
    form.full_clean()

    assert form.fields["code"].widget.attrs["aria-describedby"] == "id_code_error"


def test_valid_form_has_no_invalid_markers():
    form = SampleForm(data={"name": "Synthetic", "code": "X1"})

    assert form.is_valid() is True
    assert "aria-invalid" not in form.fields["name"].widget.attrs


def test_non_field_errors_are_ignored():
    class WithClean(SampleForm):
        def clean(self):
            raise forms.ValidationError("Whole-form problem")

    form = WithClean(data={"name": "a", "code": "b"})

    assert form.is_valid() is False
    assert "aria-invalid" not in form.fields["name"].widget.attrs
