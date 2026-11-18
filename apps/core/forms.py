from typing import Any

from django import forms

INPUT_CLASSES = (
    "block w-full min-h-11 rounded-md border border-slate-400 bg-white px-3 py-2 text-base "
    "focus:border-blue-700 focus:outline-2 focus:outline-blue-700"
)
INPUT_ERROR_CLASSES = "border-red-700"


class AccessibleFormMixin(forms.BaseForm):
    """Adds Tailwind classes, aria-describedby and aria-invalid to every widget.

    Pairs with templates/components/_form_field.html, which renders the help text and
    error elements these IDs point to.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.setdefault("class", INPUT_CLASSES)
            if field.help_text:
                self._describe(name, f"{self[name].auto_id}_help")

    def full_clean(self) -> None:
        super().full_clean()
        for name in self.errors:
            if name not in self.fields:
                continue  # non-field errors
            attrs = self.fields[name].widget.attrs
            attrs["aria-invalid"] = "true"
            attrs["class"] = f"{attrs.get('class', '')} {INPUT_ERROR_CLASSES}".strip()
            self._describe(name, f"{self[name].auto_id}_error")

    def _describe(self, name: str, element_id: str) -> None:
        attrs = self.fields[name].widget.attrs
        ids = attrs.get("aria-describedby", "").split()
        if element_id not in ids:
            attrs["aria-describedby"] = " ".join([*ids, element_id])
