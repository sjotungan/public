/* Meny: hamburgaren på små skärmar och undermenyerna.
   Undermenyns förälder är en knapp – ett klick på etiketten fäller ut menyn. */
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
    var button = item.querySelector(".nav__sub-button");
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
    var button = item.querySelector(".nav__sub-button");
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

/* Bildvisaren: ett klick på en bild i ett galleri öppnar den i ett överlägg i
   stället för att lämna sidan. Där finns bildtexten, resten av bilderna i
   samma galleri som miniatyrer och en väg tillbaka – utan att sidan lämnas,
   så läsaren står kvar på samma ställe när visaren stängs.

   Allt bygger på markup som redan finns: varje <figure> i ett .gallery har en
   länk till originalbilden och en <figcaption>. Utan JavaScript öppnar länken
   bilden som förut. */
(function () {
  "use strict";

  var galleries = [].slice.call(document.querySelectorAll(".gallery"));
  if (!galleries.length) return;

  var ICON = {
    close: "M6 6l12 12M18 6 6 18",
    prev: "m15 5-7 7 7 7",
    next: "m9 5 7 7-7 7"
  };

  function svg(name) {
    return (
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
      'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" ' +
      'aria-hidden="true"><path d="' + ICON[name] + '"/></svg>'
    );
  }

  // Rubriken närmast ovanför galleriet – "Bilder från gymmet" och liknande –
  // används som namn på uppsättningen. Den säger var i sidan bilderna hör
  // hemma, vilket annars går förlorat när sidan täcks av överlägget.
  function setTitle(gallery) {
    var node = gallery;
    while (node && node !== document.body) {
      var sibling = node.previousElementSibling;
      while (sibling) {
        var heading = sibling.matches("h1, h2, h3, h4")
          ? sibling
          : sibling.querySelector("h1, h2, h3, h4");
        if (heading) return heading.textContent.trim();
        sibling = sibling.previousElementSibling;
      }
      node = node.parentElement;
    }
    return "";
  }

  // En uppsättning = ett galleri. Bilder utan länk hoppas över.
  function collect(gallery) {
    var items = [];
    [].slice.call(gallery.querySelectorAll("figure")).forEach(function (figure) {
      var link = figure.querySelector("a[href]");
      var img = figure.querySelector("img");
      if (!link || !img) return;
      var caption = figure.querySelector("figcaption");
      items.push({
        link: link,
        href: link.getAttribute("href"),
        thumb: img.getAttribute("src"),
        alt: img.getAttribute("alt") || "",
        caption: caption ? caption.textContent.trim() : ""
      });
    });
    return items;
  }

  var sets = [];
  galleries.forEach(function (gallery) {
    var items = collect(gallery);
    if (!items.length) return;
    var set = { title: setTitle(gallery), items: items };
    sets.push(set);
    items.forEach(function (item, index) {
      item.link.addEventListener("click", function (event) {
        // Låt modifierade klick öppna bilden i en ny flik som vanligt.
        if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
        if (event.button !== 0) return;
        event.preventDefault();
        open(set, index);
      });
    });
  });
  if (!sets.length) return;

  var box = document.createElement("div");
  box.className = "lightbox";
  box.setAttribute("role", "dialog");
  box.setAttribute("aria-modal", "true");
  box.setAttribute("aria-label", "Bildvisning");
  box.hidden = true;
  box.innerHTML =
    '<div class="lightbox__bar">' +
    '  <p class="lightbox__title"></p>' +
    '  <p class="lightbox__count" role="status"></p>' +
    '  <button class="lightbox__close" type="button">' + svg("close") + "Stäng</button>" +
    "</div>" +
    '<div class="lightbox__stage">' +
    '  <button class="lightbox__nav lightbox__nav--prev" type="button" aria-label="Föregående bild">' +
    svg("prev") + "</button>" +
    '  <img class="lightbox__img" alt="">' +
    '  <button class="lightbox__nav lightbox__nav--next" type="button" aria-label="Nästa bild">' +
    svg("next") + "</button>" +
    "</div>" +
    '<div class="lightbox__foot">' +
    '  <p class="lightbox__caption"></p>' +
    '  <ul class="lightbox__thumbs" aria-label="Övriga bilder"></ul>' +
    "</div>";
  document.body.appendChild(box);

  var elTitle = box.querySelector(".lightbox__title");
  var elCount = box.querySelector(".lightbox__count");
  var elImg = box.querySelector(".lightbox__img");
  var elCaption = box.querySelector(".lightbox__caption");
  var elThumbs = box.querySelector(".lightbox__thumbs");
  var elStage = box.querySelector(".lightbox__stage");
  var closeButton = box.querySelector(".lightbox__close");

  var current = null; // uppsättningen som visas
  var index = 0;

  function buildThumbs(set) {
    elThumbs.innerHTML = "";
    if (set.items.length < 2) return;
    set.items.forEach(function (item, i) {
      var li = document.createElement("li");
      var button = document.createElement("button");
      button.type = "button";
      button.innerHTML = '<img src="" alt="">';
      button.firstChild.src = item.thumb;
      button.setAttribute("aria-label", "Bild " + (i + 1) + ": " + (item.caption || item.alt));
      button.addEventListener("click", function () {
        show(i);
      });
      li.appendChild(button);
      elThumbs.appendChild(li);
    });
  }

  function preload(i) {
    var item = current.items[i];
    if (!item) return;
    var img = new Image();
    img.src = item.href;
  }

  function show(next) {
    var total = current.items.length;
    index = (next + total) % total;
    var item = current.items[index];

    box.classList.add("is-loading");
    elImg.onload = elImg.onerror = function () {
      box.classList.remove("is-loading");
    };
    elImg.src = item.href;
    // En bild som redan ligger i cachen ger inget onload om src är oförändrad.
    if (elImg.complete) box.classList.remove("is-loading");
    elImg.alt = item.alt;
    elCaption.textContent = item.caption;
    elCount.textContent = "Bild " + (index + 1) + " av " + total;

    var thumbs = [].slice.call(elThumbs.querySelectorAll("button"));
    thumbs.forEach(function (button, i) {
      if (i === index) button.setAttribute("aria-current", "true");
      else button.removeAttribute("aria-current");
    });
    if (thumbs[index] && thumbs[index].scrollIntoView) {
      thumbs[index].scrollIntoView({ block: "nearest", inline: "center" });
    }

    preload(index + 1);
    preload(index - 1);
  }

  function open(set, at) {
    current = set;
    elTitle.textContent = set.title;
    box.classList.toggle("is-single", set.items.length < 2);
    buildThumbs(set);
    box.hidden = false;
    document.body.classList.add("has-lightbox");
    show(at);
    closeButton.focus();
  }

  function close() {
    if (box.hidden) return;
    // Fokus lämnas till den bild som visades sist, inte den som klickades:
    // läsaren kommer tillbaka till samma ställe i galleriet som i visaren.
    var back = current ? current.items[index].link : null;
    box.hidden = true;
    document.body.classList.remove("has-lightbox");
    elImg.removeAttribute("src");
    current = null;
    if (back) back.focus({ preventScroll: true });
    if (back && back.scrollIntoView) {
      back.scrollIntoView({ block: "nearest" });
    }
  }

  closeButton.addEventListener("click", close);
  box.querySelector(".lightbox__nav--prev").addEventListener("click", function () {
    show(index - 1);
  });
  box.querySelector(".lightbox__nav--next").addEventListener("click", function () {
    show(index + 1);
  });

  // Ett klick på den mörka ytan runt bilden stänger också.
  elStage.addEventListener("click", function (event) {
    if (event.target === elStage) close();
  });

  document.addEventListener("keydown", function (event) {
    if (box.hidden) return;
    if (event.key === "Escape") {
      event.preventDefault();
      close();
    } else if (event.key === "ArrowRight") {
      show(index + 1);
    } else if (event.key === "ArrowLeft") {
      show(index - 1);
    } else if (event.key === "Home") {
      show(0);
    } else if (event.key === "End") {
      show(current.items.length - 1);
    } else if (event.key === "Tab") {
      // Fokus stannar i överlägget så länge det är öppet.
      var focusable = [].slice.call(box.querySelectorAll("button")).filter(
        function (node) {
          return node.offsetParent !== null;
        }
      );
      if (!focusable.length) return;
      var first = focusable[0];
      var last = focusable[focusable.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    }
  });

  // Svep på pekskärm: samma sak som pilarna.
  var startX = null;
  var startY = null;
  elStage.addEventListener(
    "touchstart",
    function (event) {
      if (event.touches.length !== 1) return;
      startX = event.touches[0].clientX;
      startY = event.touches[0].clientY;
    },
    { passive: true }
  );
  elStage.addEventListener(
    "touchend",
    function (event) {
      if (startX === null || !event.changedTouches.length) return;
      var dx = event.changedTouches[0].clientX - startX;
      var dy = event.changedTouches[0].clientY - startY;
      startX = null;
      if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy)) {
        show(dx < 0 ? index + 1 : index - 1);
      }
    },
    { passive: true }
  );
})();
