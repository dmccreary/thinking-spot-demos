// Renders math marked up by pymdownx.arithmatex (generic mode) with KaTeX.
// Generic mode only recognizes \( \), \[ \], and $$ $$ as math delimiters —
// it never treats a bare `$` as a delimiter, so currency like $50-$100
// renders as plain text instead of being mistaken for math.
document$.subscribe(({ body }) => {
  renderMathInElement(body, {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "\\(", right: "\\)", display: false },
      { left: "\\[", right: "\\]", display: true },
    ],
  });
});
