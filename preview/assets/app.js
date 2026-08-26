
    (function () {
      'use strict';
      var d = document, w = window, body = d.body;
      var HOME = (w.RP_HOME || '').replace(/\/+$/, '');

      function $(s, c) { return (c || d).querySelector(s); }
      function $$(s, c) { return Array.prototype.slice.call((c || d).querySelectorAll(s)); }
      function esc(s) { var div = d.createElement('div'); div.textContent = s || ''; return div.innerHTML; }

      /* ----- Current year ----- */
      $$('.rp-year').forEach(function (el) { el.textContent = new Date().getFullYear(); });

      /* ----- Header state / progress / to-top ----- */
      var header = $('#site-header');
      var progress = $('#progress-bar');
      var toTop = $('#to-top');

      function onScroll() {
        var y = w.scrollY || d.documentElement.scrollTop || 0;
        if (header) { if (y > 8) { header.classList.add('scrolled'); } else { header.classList.remove('scrolled'); } }
        if (toTop) { if (y > 600) { toTop.classList.add('show'); } else { toTop.classList.remove('show'); } }
        if (progress) {
          var h = d.documentElement;
          var max = h.scrollHeight - h.clientHeight;
          var p = max > 0 ? y / max : 0;
          progress.style.width = (p * 100) + '%';
        }
      }
      w.addEventListener('scroll', onScroll, { passive: true });
      onScroll();
      if (toTop) { toTop.addEventListener('click', function () { w.scrollTo({ top: 0, behavior: 'smooth' }); }); }

      /* ----- Dark / light mode ----- */
      var themeBtn = $('#theme-toggle');
      var themeMeta = $('#meta-theme-color');
      function applyMeta() {
        if (themeMeta) { themeMeta.setAttribute('content', d.documentElement.getAttribute('data-theme') === 'dark' ? '#0b101c' : '#ffffff'); }
      }
      if (themeBtn) {
        themeBtn.addEventListener('click', function () {
          var root = d.documentElement;
          var dark = root.getAttribute('data-theme') === 'dark';
          if (dark) { root.removeAttribute('data-theme'); } else { root.setAttribute('data-theme', 'dark'); }
          try { localStorage.setItem('rp-theme', dark ? 'light' : 'dark'); } catch (e) {}
          applyMeta();
        });
      }
      applyMeta();

      /* ----- Mobile drawer ----- */
      var drawer = $('#mobile-drawer'), backdrop = $('#drawer-backdrop'), drawerLinks = $('#drawer-links');
      var menu = $('#main-menu-nav');
      if (drawerLinks && menu) { drawerLinks.innerHTML = '<ul>' + menu.innerHTML + '</ul>'; }
      function openDrawer() { if (!drawer) { return; } drawer.classList.add('open'); if (backdrop) { backdrop.classList.add('open'); } body.style.overflow = 'hidden'; }
      function closeDrawer() { if (!drawer) { return; } drawer.classList.remove('open'); if (backdrop) { backdrop.classList.remove('open'); } body.style.overflow = ''; }
      function openSearch() {
        var ov = $('#search-overlay'); if (!ov) { return; }
        ov.classList.add('open'); body.style.overflow = 'hidden';
        setTimeout(function () { var i = $('#search-input'); if (i) { i.focus(); } }, 80);
      }
      function closeSearch() {
        var ov = $('#search-overlay'); if (!ov) { return; }
        ov.classList.remove('open'); body.style.overflow = '';
      }
      var dOpen = $('#drawer-open-btn'), dClose = $('#drawer-close-btn');
      if (dOpen) { dOpen.addEventListener('click', openDrawer); }
      if (dClose) { dClose.addEventListener('click', closeDrawer); }
      if (backdrop) { backdrop.addEventListener('click', closeDrawer); }
      var sOpen = $('#search-open-btn'), eOpen = $('#error-search-btn');
      if (sOpen) { sOpen.addEventListener('click', openSearch); }
      if (eOpen) { eOpen.addEventListener('click', openSearch); }
      var sClose = $('#search-close-btn');
      if (sClose) { sClose.addEventListener('click', closeSearch); }

      /* ----- Lightbox ----- */
      var lb = $('#lightbox');
      function closeLightbox() {
        if (lb && lb.classList.contains('open')) { lb.classList.remove('open'); lb.innerHTML = ''; body.style.overflow = ''; }
      }
      if (lb) { lb.addEventListener('click', closeLightbox); }

      /* ----- Keyboard shortcuts ----- */
      d.addEventListener('keydown', function (e) {
        if ((e.ctrlKey || e.metaKey) && (e.key === 'k' || e.key === 'K')) { e.preventDefault(); openSearch(); }
        if (e.key === 'Escape') { closeSearch(); closeDrawer(); closeLightbox(); }
      });
      var ovEl = $('#search-overlay');
      if (ovEl) { ovEl.addEventListener('click', function (e) { if (e.target === ovEl) { closeSearch(); } }); }

      /* ----- Live search (Blogger feed) ----- */
      function thumbOf(entry, size) {
        var t = entry.media$thumbnail ? entry.media$thumbnail.url : '';
        if (!t) { return ''; }
        return t.replace('/s72-c/', '/' + size + '/').replace('=s72-c', '=' + size);
      }
      function linkOf(entry) {
        var l = entry.link || [];
        for (var i = 0; i < l.length; i++) { if (l[i].rel === 'alternate') { return l[i].href; } }
        return '#';
      }
      function dateOf(entry) { return (entry.published && entry.published.$t || '').substring(0, 10); }

      var searchInput = $('#search-input'), searchResults = $('#search-results'), searchTimer = null;
      function renderResults(entries, q) {
        if (!searchResults) { return; }
        if (!entries || !entries.length) {
          searchResults.innerHTML = '<p class="search-hint">No articles found for \u201C' + esc(q) + '\u201D — press Enter to search everything.</p>';
          return;
        }
        var html = '';
        entries.forEach(function (en) {
          var th = thumbOf(en, 'w120-h90-p-k-no-nu');
          html += '<a class="sr-item" href="' + linkOf(en) + '">' +
            (th ? '<img class="sr-thumb" src="' + th + '" alt=""/>' : '') +
            '<div><p class="sr-title">' + esc(en.title && en.title.$t) + '</p><span class="sr-date">' + dateOf(en) + '</span></div></a>';
        });
        searchResults.innerHTML = html;
      }
      function liveSearch(q) {
        if (!q || q.length < 2) {
          if (searchResults) { searchResults.innerHTML = '<p class="search-hint">Type at least 2 letters to search...</p>'; }
          return;
        }
        fetch(HOME + '/feeds/posts/summary?alt=json&max-results=6&q=' + encodeURIComponent(q))
          .then(function (r) { return r.json(); })
          .then(function (j) { renderResults((j.feed && j.feed.entry) || [], q); })
          .catch(function () {});
      }
      if (searchInput) {
        searchInput.addEventListener('input', function () {
          clearTimeout(searchTimer);
          var v = searchInput.value.trim();
          searchTimer = setTimeout(function () { liveSearch(v); }, 350);
        });
        searchInput.addEventListener('keydown', function (e) {
          if (e.key === 'Enter') {
            var v = searchInput.value.trim();
            if (v) { w.location.href = HOME + '/search?q=' + encodeURIComponent(v); }
          }
        });
      }

      /* ----- Reveal on scroll ----- */
      var reveals = $$('.reveal');
      if ('IntersectionObserver' in w && reveals.length) {
        var io = new IntersectionObserver(function (entries) {
          entries.forEach(function (en) {
            if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
          });
        }, { rootMargin: '0px 0px -40px 0px' });
        reveals.forEach(function (el) { io.observe(el); });
      } else {
        reveals.forEach(function (el) { el.classList.add('in'); });
      }

      /* ----- Count-up stats ----- */
      var counters = $$('[data-count]');
      function animateCount(el) {
        var target = parseFloat(el.getAttribute('data-count')) || 0;
        var suffix = el.getAttribute('data-suffix') || '';
        var t0 = null;
        function step(ts) {
          if (!t0) { t0 = ts; }
          var p = Math.min((ts - t0) / 1300, 1);
          var val = Math.floor(target * (1 - Math.pow(1 - p, 3)));
          el.textContent = val + suffix;
          if (p < 1) { requestAnimationFrame(step); }
        }
        requestAnimationFrame(step);
      }
      if ('IntersectionObserver' in w && counters.length) {
        var cio = new IntersectionObserver(function (entries) {
          entries.forEach(function (en) { if (en.isIntersecting) { animateCount(en.target); cio.unobserve(en.target); } });
        }, { threshold: 0.4 });
        counters.forEach(function (el) { cio.observe(el); });
      } else {
        counters.forEach(animateCount);
      }

      /* ----- Post / page body extras ----- */
      var postBody = $('#post-body');
      if (postBody) {
        /* Reading time (posts only) */
        var rt = $('#read-time');
        if (rt && body.classList.contains('is-post')) {
          var words = (postBody.textContent || '').trim().split(/\s+/).length;
          var mins = Math.max(1, Math.round(words / 200));
          rt.innerHTML = '<svg class="ic" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>' + mins + ' min read';
        }

        /* Lazy images + safe external links */
        $$('img', postBody).forEach(function (img) {
          img.loading = 'lazy';
          img.decoding = 'async';
          if (lb) {
            img.addEventListener('click', function (e) {
              e.preventDefault();
              if (img.src) { lb.innerHTML = '<img src="' + img.src + '" alt=""/>'; lb.classList.add('open'); body.style.overflow = 'hidden'; }
            });
          }
        });
        if (HOME) {
          $$('a[href^="http"]', postBody).forEach(function (a) {
            if (a.href.indexOf(HOME) !== 0) { a.target = '_blank'; a.rel = 'noopener'; }
          });
        }

        /* Table of contents */
        var heads = $$('h2, h3', postBody);
        if (heads.length >= 3) {
          var box = d.createElement('div');
          box.className = 'toc-box';
          var tocHtml = '<div class="toc-head" id="toc-head"><b><svg class="ic" viewBox="0 0 24 24"><line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><line x1="3" y1="6" x2="3.01" y2="6"></line><line x1="3" y1="12" x2="3.01" y2="12"></line><line x1="3" y1="18" x2="3.01" y2="18"></line></svg> Table of Contents</b><svg class="ic toc-arrow" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"></polyline></svg></div><div class="toc-body"><ul>';
          heads.forEach(function (h, i) {
            if (!h.id) { h.id = 'toc-' + (i + 1); }
            tocHtml += '<li class="lvl-' + (h.tagName === 'H2' ? '2' : '3') + '"><a href="#' + h.id + '">' + esc(h.textContent) + '</a></li>';
          });
          tocHtml += '</ul></div>';
          box.innerHTML = tocHtml;
          postBody.parentNode.insertBefore(box, postBody);
          var tHead = $('#toc-head');
          if (tHead) { tHead.addEventListener('click', function () { box.classList.toggle('collapsed'); }); }
        }

        /* Copy-code buttons */
        $$('pre', postBody).forEach(function (pre) {
          var btn = d.createElement('button');
          btn.className = 'copy-code-btn';
          btn.type = 'button';
          var copyIcon = '<svg class="ic" viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>';
          var doneIcon = '<svg class="ic" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg>';
          btn.innerHTML = copyIcon + 'Copy';
          btn.addEventListener('click', function () {
            var txt = pre.innerText || '';
            function done() {
              btn.classList.add('done');
              btn.innerHTML = doneIcon + 'Copied';
              setTimeout(function () { btn.classList.remove('done'); btn.innerHTML = copyIcon + 'Copy'; }, 1600);
            }
            function fallback() {
              var ta = d.createElement('textarea');
              ta.value = txt;
              ta.style.position = 'fixed'; ta.style.opacity = '0';
              d.body.appendChild(ta); ta.select();
              try { d.execCommand('copy'); } catch (err) {}
              d.body.removeChild(ta); done();
            }
            if (navigator.clipboard && navigator.clipboard.writeText) {
              navigator.clipboard.writeText(txt).then(done, fallback);
            } else { fallback(); }
          });
          pre.appendChild(btn);
        });
      }

      /* ----- Related posts (Blogger feed) ----- */
      var rpGrid = $('#rp-grid');
      if (rpGrid && body.classList.contains('is-post')) {
        var tagEl = $('.rp-tag', rpGrid);
        var label = tagEl ? (tagEl.getAttribute('data-label') || '') : '';
        var feedUrl = label
          ? HOME + '/feeds/posts/summary/-/' + encodeURIComponent(label) + '?alt=json&max-results=7'
          : HOME + '/feeds/posts/summary?alt=json&max-results=7';
        fetch(feedUrl)
          .then(function (r) { return r.json(); })
          .then(function (j) {
            var entries = (j.feed && j.feed.entry) || [];
            var here = w.location.href.split('#')[0].split('?')[0];
            var html = '', shown = 0;
            entries.forEach(function (en) {
              if (shown >= 3) { return; }
              var url = linkOf(en);
              if (url.split('#')[0].split('?')[0] === here) { return; }
              var th = thumbOf(en, 'w400-h250-p-k-no-nu');
              html += '<article class="rp-card"><a class="rp-thumb" href="' + url + '">' +
                (th ? '<img src="' + th + '" alt="" loading="lazy"/>' : '') +
                '</a><div class="rp-body"><h4><a href="' + url + '">' + esc(en.title && en.title.$t) + '</a></h4><time>' + dateOf(en) + '</time></div></article>';
              shown++;
            });
            if (html) { rpGrid.innerHTML = html; }
            else { var rp = $('#related-posts'); if (rp) { rp.style.display = 'none'; } }
          })
          .catch(function () {});
      }

      /* ----- Mega menu: Topics # link ----- */
      $$('.has-mega > a[href="#"]').forEach(function (a) {
        a.addEventListener('click', function (e) { e.preventDefault(); });
      });

      /* ----- Cookie notice ----- */
      var cookieBar = $('#cookie-bar');
      var cookieBtn = $('#cookie-accept');
      try {
        if (localStorage.getItem('rp-cookies') === '1' && cookieBar) { cookieBar.setAttribute('hidden', ''); }
        else if (cookieBar) { body.classList.add('has-cookie'); }
      } catch (e) { if (cookieBar) { body.classList.add('has-cookie'); } }
      if (cookieBtn) {
        cookieBtn.addEventListener('click', function () {
          try { localStorage.setItem('rp-cookies', '1'); } catch (err) {}
          if (cookieBar) { cookieBar.setAttribute('hidden', ''); }
          body.classList.remove('has-cookie');
        });
      }

      /* ----- Trending ticker (duplicate track for seamless loop) ----- */
      var tTrack = $('#ticker-track');
      if (tTrack && $$('.ticker-item', tTrack).length) {
        tTrack.innerHTML = tTrack.innerHTML + tTrack.innerHTML;
      }

      /* ----- Featured slider ----- */
      (function initSliderFromSlides() {
        var track = $('#feat-track'), slider = $('#feat-slider'), dotsEl = $('#feat-dots');
        if (!track || !slider) { return; }
        var slides = $$('.feat-slide', track);
        var n = slides.length, idx = 0, timer = null;
        if (!n) { return; }
        function go(i) {
          idx = (i + n) % n;
          track.style.transform = 'translateX(' + (-idx * 100) + '%)';
          if (dotsEl) { $$('.feat-dot', dotsEl).forEach(function (dot, k) { dot.classList.toggle('on', k === idx); }); }
        }
        function stop() { if (timer) { clearInterval(timer); timer = null; } }
        function play() {
          stop();
          if (n < 2) { return; }
          timer = setInterval(function () { go(idx + 1); }, 5200);
        }
        if (dotsEl) {
          var h = '';
          for (var i = 0; i < n; i++) { h += '<button type="button" class="feat-dot' + (i === 0 ? ' on' : '') + '" data-i="' + i + '" aria-label="Slide ' + (i + 1) + '"></button>'; }
          dotsEl.innerHTML = h;
          $$('.feat-dot', dotsEl).forEach(function (dot) {
            dot.addEventListener('click', function () { go(+dot.getAttribute('data-i')); play(); });
          });
        }
        var prev = $('#feat-prev'), next = $('#feat-next');
        if (prev) { prev.addEventListener('click', function () { go(idx - 1); play(); }); }
        if (next) { next.addEventListener('click', function () { go(idx + 1); play(); }); }
        slider.addEventListener('mouseenter', stop);
        slider.addEventListener('mouseleave', play);
        play();
      })();

      /* ----- Copy link button ----- */
      var cpBtn = $('#copy-link-btn');
      if (cpBtn) {
        cpBtn.addEventListener('click', function () {
          var url = w.location.href;
          var copyIcon = '<svg class="ic" viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>';
          var doneIcon = '<svg class="ic" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg>';
          function done() {
            var old = cpBtn.getAttribute('data-old') || copyIcon;
            cpBtn.innerHTML = doneIcon;
            setTimeout(function () { cpBtn.innerHTML = old; }, 1600);
          }
          function fallback() {
            var ta = d.createElement('textarea');
            ta.value = url;
            ta.style.position = 'fixed'; ta.style.opacity = '0';
            d.body.appendChild(ta); ta.select();
            try { d.execCommand('copy'); } catch (err) {}
            d.body.removeChild(ta); done();
          }
          cpBtn.setAttribute('data-old', copyIcon);
          if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(url).then(done, fallback);
          } else { fallback(); }
        });
      }
    })();
    