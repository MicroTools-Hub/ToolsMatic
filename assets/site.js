(() => {
  const ensureAds = () => {
    if (typeof document === 'undefined') return;
    if (!document.querySelector('meta[name="google-adsense-account"]')) {
      const meta = document.createElement('meta');
      meta.name = 'google-adsense-account';
      meta.content = 'ca-pub-6119998481340838';
      document.head.appendChild(meta);
    }
    if (!document.querySelector('script[data-adsbygoogle]')) {
      const script = document.createElement('script');
      script.async = true;
      script.crossOrigin = 'anonymous';
      script.dataset.adsbygoogle = 'true';
      script.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6119998481340838';
      document.head.appendChild(script);
    }
  };

  const ensureToastHost = () => {
    let host = document.querySelector('.toast-host');
    if (!host) {
      host = document.createElement('div');
      host.className = 'toast-host';
      document.body.appendChild(host);
    }
    return host;
  };

  const showToast = (message, variant = 'info') => {
    const host = ensureToastHost();
    const toast = document.createElement('div');
    toast.className = `toast toast-${variant}`;
    toast.textContent = message;
    host.appendChild(toast);
    requestAnimationFrame(() => toast.classList.add('show'));
    setTimeout(() => {
      toast.classList.remove('show');
      setTimeout(() => toast.remove(), 250);
    }, 2200);
  };

  const bindKeyboard = () => {
    document.addEventListener('keydown', (e) => {
      if (e.ctrlKey && e.key === 'Enter') {
        const primary = document.querySelector('[data-primary]');
        if (primary) { e.preventDefault(); primary.click(); }
      }
      if (e.key === 'Escape') {
        const clearBtn = document.querySelector('[data-clear]');
        if (clearBtn) { e.preventDefault(); clearBtn.click(); }
      }
    });
  };

  const initThemeToggle = () => {
    const toggleBtn = document.getElementById('theme-toggle');
    if (!toggleBtn) return;
    const isDark = localStorage.getItem('mt-theme') === 'dark';
    if (isDark) {
      document.documentElement.classList.add('dark-mode');
      toggleBtn.textContent = '☀️';
    } else {
      toggleBtn.textContent = '🌙';
    }
    toggleBtn.addEventListener('click', () => {
      const isDarkMode = document.documentElement.classList.toggle('dark-mode');
      localStorage.setItem('mt-theme', isDarkMode ? 'dark' : 'light');
      toggleBtn.textContent = isDarkMode ? '☀️' : '🌙';
      if (window.toolsMatic) window.toolsMatic.showToast(isDarkMode ? 'Dark mode on' : 'Light mode on', 'info');
    });
  };

  const handoffKey = 'toolsmatic-handoff';

  const setHandoff = (payload) => {
    try {
      sessionStorage.setItem(handoffKey, JSON.stringify({ ...payload, ts: Date.now() }));
    } catch (_) {
      // ignore storage issues
    }
  };

  const consumeHandoff = (expectedKind) => {
    try {
      const raw = sessionStorage.getItem(handoffKey);
      if (!raw) return null;
      const data = JSON.parse(raw);
      if (expectedKind && data.kind !== expectedKind) return null;
      sessionStorage.removeItem(handoffKey);
      return data;
    } catch (_) {
      return null;
    }
  };

  const handoffAndGo = ({ target, kind = 'text', value, slot }) => {
    if (!target || !value) return;
    setHandoff({ kind, value, slot });
    window.location.href = target;
  };

  window.toolsMatic = { showToast, handoffAndGo, consumeHandoff };
  ensureAds();
  bindKeyboard();

  // Initialize theme toggle when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initThemeToggle);
  } else {
    initThemeToggle();
  }
})();
