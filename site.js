/* Small client-side enhancements for the static GitHub Pages site. */
const INDUSTRYWIRE_EMAIL = window.INDUSTRYWIRE_CONTACT_EMAIL || '';

document.querySelectorAll('[data-current-year]').forEach((node) => {
  node.textContent = String(new Date().getFullYear());
});

document.querySelectorAll('[data-contact-link]').forEach((link) => {
  if (INDUSTRYWIRE_EMAIL) link.href = `mailto:${INDUSTRYWIRE_EMAIL}`;
});
document.querySelectorAll('[data-contact-address]').forEach((node) => {
  node.textContent = INDUSTRYWIRE_EMAIL;
});

const menuButton = document.querySelector('.nav-toggle');
const siteNav = document.querySelector('.site-header nav');
if (menuButton && siteNav) {
  menuButton.addEventListener('click', () => {
    const open = menuButton.getAttribute('aria-expanded') === 'true';
    menuButton.setAttribute('aria-expanded', String(!open));
    siteNav.classList.toggle('open', !open);
  });
  siteNav.addEventListener('click', (event) => {
    if (event.target.closest('a')) {
      menuButton.setAttribute('aria-expanded', 'false');
      siteNav.classList.remove('open');
    }
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') {
      menuButton.setAttribute('aria-expanded', 'false');
      siteNav.classList.remove('open');
      menuButton.focus();
    }
  });
}

const topButton = document.querySelector('.back-top');
if (topButton) {
  const updateTopButton = () => topButton.classList.toggle('visible', window.scrollY > 450);
  window.addEventListener('scroll', updateTopButton, { passive: true });
  updateTopButton();
  topButton.addEventListener('click', () => {
    const behavior = window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth';
    window.scrollTo({ top: 0, behavior });
  });
}

const catalogue = document.querySelector('[data-catalogue]');
if (catalogue) {
  const cards = [...catalogue.querySelectorAll('[data-sector]')];
  const search = document.querySelector('[data-catalogue-search]');
  const count = document.querySelector('[data-result-count]');
  let activeSector = 'all';
  const update = () => {
    const term = (search?.value || '').trim().toLowerCase();
    let visible = 0;
    cards.forEach((card) => {
      const sectorMatch = activeSector === 'all' || card.dataset.sector === activeSector;
      const haystack = (card.dataset.searchText || card.textContent).toLowerCase();
      const words = haystack.match(/[a-z0-9]+/g) || [];
      const terms = term.split(/\s+/).filter(Boolean);
      const textMatch = !term || terms.every((word) => word.length <= 2 ? words.includes(word) : haystack.includes(word));
      const show = sectorMatch && textMatch;
      card.classList.toggle('hidden', !show);
      if (show) visible += 1;
    });
    if (count) count.textContent = `${visible} ${visible === 1 ? 'concept' : 'concepts'} shown`;
  };
  search?.addEventListener('input', update);
  document.querySelectorAll('[data-filter]').forEach((button) => {
    button.addEventListener('click', () => {
      activeSector = button.dataset.filter;
      document.querySelectorAll('[data-filter]').forEach((item) => item.setAttribute('aria-pressed', String(item === button)));
      update();
    });
  });
  update();
}

const contactForm = document.querySelector('[data-mailto-form]');
if (contactForm) {
  const params = new URLSearchParams(window.location.search);
  const typeSelect = contactForm.querySelector('[name="type"]');
  const requestedType = params.get('type');
  if (requestedType && typeSelect && [...typeSelect.options].some((option) => option.text === requestedType)) {
    typeSelect.value = requestedType;
  }
  const topic = params.get('topic');
  if (topic) {
    const message = contactForm.querySelector('[name="message"]');
    if (message) message.value = `I would like to discuss: ${topic}\n\n`;
  }
  contactForm.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!contactForm.reportValidity()) return;
    if (!INDUSTRYWIRE_EMAIL) {
      const status = document.querySelector('[data-form-status]');
      if (status) status.textContent = 'Email contact is not configured. Please use the contact address shown on the page.';
      return;
    }
    const values = new FormData(contactForm);
    const subject = `[IndustryWire] ${values.get('type') || 'General enquiry'}`;
    const body = [
      `Name: ${values.get('name')}`,
      `Business email: ${values.get('email')}`,
      `Company: ${values.get('company') || 'Not provided'}`,
      `Country: ${values.get('country') || 'Not provided'}`,
      `Enquiry type: ${values.get('type')}`,
      '',
      String(values.get('message') || '')
    ].join('\n');
    if (typeof window.gtag === 'function') {
      window.gtag('event', 'contact_draft_opened', {
        enquiry_type: String(values.get('type') || 'General enquiry'),
        transport_type: 'beacon'
      });
    }
    window.location.href = `mailto:${INDUSTRYWIRE_EMAIL}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    const status = document.querySelector('[data-form-status]');
    if (status) status.textContent = 'Your email app should open with a draft. Review it and choose Send there; the website does not send or store this form.';
  });
}

const articlesList = document.querySelector('[data-articles-list]');
if (articlesList) {
  fetch('/articles.json')
    .then((response) => {
      if (!response.ok) throw new Error('Article data unavailable');
      return response.json();
    })
    .then((data) => {
      const entries = Array.isArray(data.articles) ? data.articles : [];
      if (!entries.length) return;
      document.querySelector('[data-articles-empty]')?.classList.add('hidden');
      entries.filter((article) => article && article.title && article.url && article.summary)
        .forEach((article) => {
          let target;
          try { target = new URL(article.url, window.location.origin); } catch { return; }
          if (target.origin !== window.location.origin) return;
          const card = document.createElement('article');
          card.className = 'card';
          const tag = document.createElement('span');
          tag.className = 'tag';
          tag.textContent = article.section || 'IndustryWire';
          const heading = document.createElement('h3');
          const link = document.createElement('a');
          link.href = target.pathname;
          link.textContent = article.title;
          heading.append(link);
          const summary = document.createElement('p');
          summary.textContent = article.summary;
          const meta = document.createElement('p');
          meta.className = 'card-meta';
          meta.textContent = [article.author, article.published].filter(Boolean).join(' · ');
          card.append(tag, heading, summary);
          if (meta.textContent) card.append(meta);
          articlesList.append(card);
        });
    })
    .catch(() => {});
}

const sampleList = document.querySelector('[data-sample-list]');
if (sampleList) {
  fetch('/articles.json')
    .then((response) => {
      if (!response.ok) throw new Error('Sample list unavailable');
      return response.json();
    })
    .then((data) => {
      const samples = Array.isArray(data.sampleArticles) ? data.sampleArticles : [];
      samples.filter((sample) => sample && sample.status === 'sample' && sample.title && sample.url && sample.summary)
        .forEach((sample) => {
          let target;
          try { target = new URL(sample.url, window.location.origin); } catch { return; }
          if (target.origin !== window.location.origin) return;
          const card = document.createElement('article');
          card.className = 'card';
          const tag = document.createElement('span');
          tag.className = 'tag tag-warm';
          tag.textContent = 'Sample analysis · not news';
          const section = document.createElement('p');
          section.className = 'card-index';
          section.textContent = sample.section || 'Editorial demonstration';
          const heading = document.createElement('h3');
          const link = document.createElement('a');
          link.href = target.pathname;
          link.textContent = sample.title;
          heading.append(link);
          const summary = document.createElement('p');
          summary.textContent = sample.summary;
          card.append(tag, section, heading, summary);
          sampleList.append(card);
        });
    })
    .catch(() => {});
}

const siteSearch = document.querySelector('[data-site-search]');
if (siteSearch) {
  const items = [...document.querySelectorAll('[data-search-item]')];
  const count = document.querySelector('[data-site-count]');
  const params = new URLSearchParams(window.location.search);
  siteSearch.value = params.get('q') || '';
  const runSearch = () => {
    const term = siteSearch.value.trim().toLowerCase();
    let visible = 0;
    items.forEach((item) => {
      const match = !term || item.textContent.toLowerCase().includes(term);
      item.classList.toggle('hidden', !match);
      if (match) visible += 1;
    });
    if (count) count.textContent = `${visible} ${visible === 1 ? 'result' : 'results'}`;
  };
  siteSearch.addEventListener('input', runSearch);
  document.querySelector('[data-search-clear]')?.addEventListener('click', () => {
    siteSearch.value = '';
    siteSearch.focus();
    runSearch();
  });
  runSearch();
}

document.querySelectorAll('[data-share-copy]').forEach((button) => {
  button.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(window.location.href);
      button.textContent = 'Link copied';
    } catch {
      button.textContent = 'Copy unavailable';
    }
  });
});

document.querySelectorAll('[data-share-native]').forEach((button) => {
  button.addEventListener('click', async () => {
    if (navigator.share) {
      await navigator.share({ title: document.title, url: window.location.href });
    } else {
      await navigator.clipboard?.writeText(window.location.href);
      button.textContent = 'Link copied';
    }
  });
});
