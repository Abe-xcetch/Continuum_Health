// Continuum UI behaviour. Loaded before Alpine so components are registered first.
// Alpine's CSP build cannot evaluate inline logic: register components here with
// Alpine.data() and reference them by name in templates (x-data="dismissible").

document.addEventListener("alpine:init", () => {
  // Hide an alert or panel, e.g. a dismissible message.
  window.Alpine.data("dismissible", () => ({
    open: true,
    dismiss() {
      this.open = false;
    },
  }));
});
