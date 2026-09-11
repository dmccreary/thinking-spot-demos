// Renders math marked up by pymdownx.arithmatex with KaTeX. mkdocs.yml
// restricts arithmatex to inline_syntax: ['round'] and block_syntax:
// ['square'], so only \( \) and \[ \] are ever treated as math delimiters —
// a bare `$` (as in currency like $50-$100) is never mistaken for one.
document$.subscribe(({ body }) => {
  renderMathInElement(body, {
    delimiters: [
      { left: "\\(", right: "\\)", display: false },
      { left: "\\[", right: "\\]", display: true },
    ],
  });
});
