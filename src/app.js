(function () {
  'use strict';

  var doc = document;
  var root = doc.documentElement;
  var body = doc.body;

  function qs(sel, ctx) { return (ctx || doc).querySelector(sel); }
  function qsa(sel, ctx) { return Array.prototype.slice.call((ctx || doc).querySelectorAll(sel)); }

  /* Preloader */
  window.addEventListener('load', function () {
    var p = qs('.sb-preloader');
    if (p) p.classList.add('hide');
  });
  setTimeout(function () {
    var p = qs('.sb-preloader');
    if (p) p.classList.add('hide');
  }, 2200);

  /* Dark mode */
  var savedTheme = localStorage.getItem('sb-theme');
  if (savedTheme) root.setAttribute('data-theme', savedTheme);
  function toggleTheme() {
    var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    localStorage.setItem('sb-theme', next);
  }
  qsa('[data-action="theme"]').forEach(function (btn) {
    btn.addEventListener('click', toggleTheme);
  });

  /* Header scroll + progress */
  var header = qs('.sb-header');
  var bar = qs('.sb-progress');
  var topBtn = qs('.sb-top');
  function onScroll() {
    var y = window.scrollY || root.scrollTop;
    if (header) header.classList.toggle('is-scrolled', y > 8);
    if (topBtn) topBtn.classList.toggle('show', y > 500);
    if (bar) {
      var h = root.scrollHeight - window.innerHeight;
      bar.style.width = (h > 0 ? (y / h) * 100 : 0) + '%';
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* Drawer */
  var drawer = qs('.sb-drawer');
  function openDrawer(open) {
    if (!drawer) return;
    drawer.classList.toggle('open', open);
    body.style.overflow = open ? 'hidden' : '';
  }
  qsa('[data-action="menu"]').forEach(function (b) {
    b.addEventListener('click', function () { openDrawer(true); });
  });
  qsa('[data-action="menu-close"]').forEach(function (b) {
    b.addEventListener('click', function () { openDrawer(false); });
  });

  /* Clone nav into drawer */
  var srcNav = qs('.sb-nav');
  var dstNav = qs('.sb-drawer-nav');
  if (srcNav && dstNav && !dstNav.childElementCount) {
    dstNav.innerHTML = srcNav.innerHTML;
  }

  /* Search overlay */
  var search = qs('.sb-search');
  function openSearch(open) {
    if (!search) return;
    search.classList.toggle('open', open);
    body.style.overflow = open ? 'hidden' : '';
    if (open) {
      var inp = qs('.sb-search input[type="text"]');
      if (inp) setTimeout(function () { inp.focus(); }, 50);
    }
  }
  qsa('[data-action="search"]').forEach(function (b) {
    b.addEventListener('click', function () { openSearch(true); });
  });
  qsa('[data-action="search-close"]').forEach(function (b) {
    b.addEventListener('click', function () { openSearch(false); });
  });
  doc.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { openDrawer(false); openSearch(false); closeLite(); }
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      openSearch(true);
    }
  });

  /* Back to top */
  if (topBtn) {
    topBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* Cookie */
  var cookie = qs('.sb-cookie');
  if (cookie) {
    if (localStorage.getItem('sb-cookie') === '1') cookie.style.display = 'none';
    var ok = qs('[data-action="cookie"]');
    if (ok) ok.addEventListener('click', function () {
      localStorage.setItem('sb-cookie', '1');
      cookie.style.display = 'none';
    });
  }

  /* Reading time on cards + article */
  function words(el) {
    return (el && (el.innerText || el.textContent) || '').trim().split(/\s+/).filter(Boolean).length;
  }
  qsa('[data-readtime]').forEach(function (el) {
    var target = qs(el.getAttribute('data-readtime')) || qs('.post-body') || el;
    var n = Math.max(1, Math.round(words(target) / 200));
    el.textContent = n + ' min read';
  });
  qsa('.post-outer').forEach(function (card) {
    var slot = qs('.js-read', card);
    var src = qs('.post-snippet', card) || qs('.post-body', card);
    if (slot && src) {
      var n = Math.max(1, Math.round(words(src) / 180));
      slot.textContent = n + ' min';
    }
  });

  /* TOC */
  var toc = qs('#sb-toc-list');
  var article = qs('.post-body');
  if (toc && article && body.classList.contains('is-post')) {
    var heads = qsa('h2, h3', article);
    if (!heads.length) {
      var box = qs('.sb-toc');
      if (box) box.style.display = 'none';
    } else {
      heads.forEach(function (h, i) {
        if (!h.id) h.id = 'h-' + (i + 1);
        var li = doc.createElement('li');
        var a = doc.createElement('a');
        a.href = '#' + h.id;
        a.textContent = h.textContent;
        if (h.tagName === 'H3') li.style.marginLeft = '14px';
        li.appendChild(a);
        toc.appendChild(li);
      });
    }
    var tog = qs('[data-action="toc"]');
    if (tog) tog.addEventListener('click', function () {
      toc.style.display = toc.style.display === 'none' ? '' : 'none';
    });
  }

  /* Copy code */
  qsa('.post-body pre').forEach(function (pre) {
    pre.style.position = 'relative';
    var btn = doc.createElement('button');
    btn.className = 'copy-btn';
    btn.type = 'button';
    btn.textContent = 'Copy';
    btn.addEventListener('click', function () {
      var txt = pre.innerText;
      if (navigator.clipboard) navigator.clipboard.writeText(txt);
      btn.textContent = 'Copied';
      setTimeout(function () { btn.textContent = 'Copy'; }, 1400);
    });
    pre.appendChild(btn);
  });

  /* Lightbox */
  var lite = qs('.sb-lite');
  var liteImg = lite ? qs('img', lite) : null;
  function closeLite() {
    if (lite) lite.classList.remove('open');
  }
  if (lite) {
    lite.addEventListener('click', closeLite);
    qsa('.post-body img').forEach(function (img) {
      img.style.cursor = 'zoom-in';
      img.addEventListener('click', function () {
        liteImg.src = img.src;
        lite.classList.add('open');
      });
    });
  }

  /* Share */
  function share(net) {
    var url = encodeURIComponent(location.href);
    var title = encodeURIComponent(doc.title);
    var map = {
      fb: 'https://www.facebook.com/sharer/sharer.php?u=' + url,
      tw: 'https://twitter.com/intent/tweet?url=' + url + '&text=' + title,
      wa: 'https://api.whatsapp.com/send?text=' + title + '%20' + url,
      li: 'https://www.linkedin.com/shareArticle?mini=true&url=' + url + '&title=' + title,
      tg: 'https://t.me/share/url?url=' + url + '&text=' + title,
      mail: 'mailto:?subject=' + title + '&body=' + url
    };
    if (net === 'copy') {
      if (navigator.clipboard) navigator.clipboard.writeText(location.href);
      return;
    }
    if (map[net]) window.open(map[net], '_blank', 'noopener,width=640,height=520');
  }
  qsa('[data-share]').forEach(function (b) {
    b.addEventListener('click', function (e) {
      e.preventDefault();
      share(b.getAttribute('data-share'));
    });
  });

  /* Related posts via Blogger JSON feed */
  var rel = qs('#sb-related');
  if (rel && body.classList.contains('is-post')) {
    var label = rel.getAttribute('data-label') || '';
    var current = rel.getAttribute('data-current') || location.href;
    var feed = '/feeds/posts/summary' + (label ? '/-/' + encodeURIComponent(label) : '') + '?alt=json&max-results=6';
    fetch(feed).then(function (r) { return r.json(); }).then(function (data) {
      var entries = (data.feed && data.feed.entry) || [];
      var html = '';
      var n = 0;
      entries.forEach(function (e) {
        var link = '';
        (e.link || []).forEach(function (l) { if (l.rel === 'alternate') link = l.href; });
        if (!link || current.indexOf(link) !== -1) return;
        if (n >= 3) return;
        n++;
        var img = 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="400" height="225"><rect fill="%23FECDA5" width="100%" height="100%"/></svg>';
        if (e.media$thumbnail && e.media$thumbnail.url) {
          img = e.media$thumbnail.url.replace(/s\d+-c/, 's400');
        }
        var title = e.title && e.title.$t ? e.title.$t : 'Post';
        html += '<a class="sb-rel" href="' + link + '"><img src="' + img + '" alt=""/><div>' + title + '</div></a>';
      });
      if (html) rel.innerHTML = html;
      else rel.parentNode.style.display = 'none';
    }).catch(function () {
      if (rel.parentNode) rel.parentNode.style.display = 'none';
    });
  }

  /* Stats count-up */
  var stats = qsa('.sb-stat b[data-count]');
  if (stats.length && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        var end = parseFloat(el.getAttribute('data-count'));
        var suf = el.getAttribute('data-suf') || '';
        var t0 = performance.now();
        function tick(now) {
          var p = Math.min(1, (now - t0) / 1200);
          var val = end * (1 - Math.pow(1 - p, 3));
          el.textContent = (end % 1 ? val.toFixed(1) : Math.round(val)) + suf;
          if (p < 1) requestAnimationFrame(tick);
        }
        requestAnimationFrame(tick);
        io.unobserve(el);
      });
    }, { threshold: 0.4 });
    stats.forEach(function (s) { io.observe(s); });
  }

  /* Lazy images fallback */
  qsa('img[data-src]').forEach(function (img) {
    img.src = img.getAttribute('data-src');
  });

  /* Year */
  qsa('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
