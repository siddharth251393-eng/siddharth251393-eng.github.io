/* Optional analytics load only after a visitor chooses to accept. */
(() => {
  const loader = document.currentScript;
  const gaId = loader?.dataset.gaMeasurementId || '';
  const clarityId = loader?.dataset.clarityProjectId || '';
  if (!gaId && !clarityId) return;

  const storageKey = 'sectorjournal-optional-analytics-consent-v1';
  const readChoice = () => {
    try {
      const value = localStorage.getItem(storageKey);
      return value === 'accepted' || value === 'rejected' ? value : null;
    } catch {
      return null;
    }
  };

  let choice = readChoice();
  let panel;

  const eraseCookies = (prefixes) => {
    const cookies = document.cookie ? document.cookie.split(';') : [];
    const host = window.location.hostname;
    const domains = [host, `.${host}`];
    cookies.forEach((cookie) => {
      const name = cookie.split('=', 1)[0].trim();
      if (!prefixes.some((prefix) => name === prefix || name.startsWith(`${prefix}_`))) return;
      domains.forEach((domain) => {
        document.cookie = `${name}=; Max-Age=0; path=/; domain=${domain}; SameSite=Lax`;
      });
      document.cookie = `${name}=; Max-Age=0; path=/; SameSite=Lax`;
    });
  };

  const setClarityConsent = (accepted) => {
    if (typeof window.clarity !== 'function') return;
    window.clarity('consentv2', {
      ad_Storage: 'denied',
      analytics_Storage: accepted ? 'granted' : 'denied'
    });
  };

  const loadClarity = () => {
    if (!clarityId || window.__sectorjournalClarityLoaded) return;
    window.__sectorjournalClarityLoaded = true;
    window.clarity = window.clarity || function clarityQueue(...args) {
      (window.clarity.q = window.clarity.q || []).push(args);
    };
    setClarityConsent(true);
    const script = document.createElement('script');
    script.async = true;
    script.src = `https://www.clarity.ms/tag/${encodeURIComponent(clarityId)}`;
    script.referrerPolicy = 'strict-origin-when-cross-origin';
    document.head.append(script);
  };

  const loadGoogleAnalytics = () => {
    if (!gaId || window.__sectorjournalGoogleAnalyticsLoaded) return;
    window.__sectorjournalGoogleAnalyticsLoaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function gtagQueue() { window.dataLayer.push(arguments); };
    window.gtag('consent', 'default', {
      ad_storage: 'denied',
      ad_user_data: 'denied',
      ad_personalization: 'denied',
      analytics_storage: 'denied'
    });
    window.gtag('consent', 'update', {
      analytics_storage: 'granted',
      ad_storage: 'denied',
      ad_user_data: 'denied',
      ad_personalization: 'denied'
    });
    window.gtag('js', new Date());
    window.gtag('config', gaId, { send_page_view: true });
    const script = document.createElement('script');
    script.async = true;
    script.src = `https://www.googletagmanager.com/gtag/js?id=${encodeURIComponent(gaId)}`;
    script.referrerPolicy = 'strict-origin-when-cross-origin';
    document.head.append(script);
  };

  const stopOptionalAnalytics = () => {
    if (window.__sectorjournalGoogleAnalyticsLoaded && typeof window.gtag === 'function') {
      window.gtag('consent', 'update', {
        analytics_storage: 'denied',
        ad_storage: 'denied',
        ad_user_data: 'denied',
        ad_personalization: 'denied'
      });
    }
    setClarityConsent(false);
    eraseCookies(['_ga', '_gid', '_gat', '_clck', '_clsk']);
  };

  const hidePanel = () => {
    panel?.remove();
    panel = null;
  };

  const saveChoice = (nextChoice) => {
    const wasAccepted = choice === 'accepted';
    choice = nextChoice;
    try { localStorage.setItem(storageKey, nextChoice); } catch { /* Keep the current-page choice. */ }
    if (nextChoice === 'accepted') {
      loadGoogleAnalytics();
      loadClarity();
    } else {
      stopOptionalAnalytics();
    }
    hidePanel();
    // A remote tag cannot be safely unloaded once evaluated. Reloading after
    // withdrawal drops it from the page; the saved rejection keeps it disabled.
    if (wasAccepted && nextChoice === 'rejected') window.location.reload();
  };

  const openPanel = () => {
    if (panel) return;
    panel = document.createElement('section');
    panel.className = 'privacy-consent-panel';
    panel.setAttribute('role', 'region');
    panel.setAttribute('aria-label', 'Optional analytics privacy settings');
    panel.innerHTML = `
      <div class="privacy-consent-inner">
        <div class="privacy-consent-copy">
          <h2>Help improve The Sector Journal</h2>
          <p>With your permission, Google Analytics and Microsoft Clarity measure page visits and site interactions so we can improve the site. They may process device, browser, referral, page-view, click and scroll information. Form text and email-draft contents are not sent as analytics events. <a href="/privacy.html">Read the privacy notice</a>.</p>
        </div>
        <div class="privacy-consent-actions">
          <button type="button" data-consent-reject>Reject optional analytics</button>
          <button type="button" data-consent-accept>Accept optional analytics</button>
        </div>
      </div>`;
    document.body.append(panel);
    panel.querySelector('[data-consent-accept]')?.addEventListener('click', () => saveChoice('accepted'));
    panel.querySelector('[data-consent-reject]')?.addEventListener('click', () => saveChoice('rejected'));
    panel.querySelector('[data-consent-reject]')?.focus();
  };

  document.querySelectorAll('[data-privacy-settings]').forEach((link) => {
    link.addEventListener('click', (event) => {
      event.preventDefault();
      openPanel();
    });
  });

  const footerLinks = document.querySelector('.footer-links');
  if (footerLinks && !footerLinks.querySelector('[data-privacy-settings]')) {
    const settingsLink = document.createElement('a');
    settingsLink.href = '#privacy-settings';
    settingsLink.dataset.privacySettings = '';
    settingsLink.textContent = 'Privacy settings';
    settingsLink.addEventListener('click', (event) => {
      event.preventDefault();
      openPanel();
    });
    footerLinks.append(settingsLink);
  }

  if (choice === 'accepted') {
    loadGoogleAnalytics();
    loadClarity();
  } else if (choice === 'rejected') {
    stopOptionalAnalytics();
  } else {
    openPanel();
  }
})();
