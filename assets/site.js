// Progressive enhancement only: public content and navigation work without JavaScript.
for (const element of document.querySelectorAll('[data-year]')) {
  element.textContent = String(new Date().getFullYear());
}
