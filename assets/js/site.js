/* Meny: hamburgaren på små skärmar och undermenyerna.
   Progressiv förbättring – utan JavaScript nås alla länkar ändå, eftersom
   föräldern i undermenyn är en vanlig länk till sin egen sida. */
(function () {
  "use strict";

  var header = document.querySelector(".site-header");
  if (!header) return;

  var toggle = header.querySelector(".nav-toggle");
  var subs = [].slice.call(header.querySelectorAll(".nav__has-sub"));

  function setNav(open) {
    header.setAttribute("data-nav-open", open ? "true" : "false");
    if (toggle) toggle.setAttribute("aria-expanded", open ? "true" : "false");
  }

  function setSub(item, open) {
    item.setAttribute("data-open", open ? "true" : "false");
    var button = item.querySelector(".nav__sub-toggle");
    if (button) button.setAttribute("aria-expanded", open ? "true" : "false");
  }

  function closeAllSubs(except) {
    subs.forEach(function (item) {
      if (item !== except) setSub(item, false);
    });
  }

  setNav(false);
  subs.forEach(function (item) {
    setSub(item, false);
    var button = item.querySelector(".nav__sub-toggle");
    if (!button) return;
    button.addEventListener("click", function (event) {
      event.stopPropagation();
      var open = item.getAttribute("data-open") === "true";
      closeAllSubs(item);
      setSub(item, !open);
    });
  });

  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = header.getAttribute("data-nav-open") !== "true";
      setNav(open);
      if (!open) closeAllSubs();
    });
  }

  document.addEventListener("click", function (event) {
    if (!header.contains(event.target)) {
      closeAllSubs();
      setNav(false);
    }
  });

  document.addEventListener("keydown", function (event) {
    if (event.key !== "Escape") return;
    closeAllSubs();
    if (header.getAttribute("data-nav-open") === "true") {
      setNav(false);
      if (toggle) toggle.focus();
    }
  });

  // Återställ läget när layouten växlar tillbaka till den breda menyn.
  var wide = window.matchMedia("(min-width: 861px)");
  var onChange = function (event) {
    if (event.matches) {
      setNav(false);
      closeAllSubs();
    }
  };
  if (wide.addEventListener) wide.addEventListener("change", onChange);
  else if (wide.addListener) wide.addListener(onChange);
})();
