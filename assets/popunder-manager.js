/**
 * Popunder Manager
 * Manages popunder ads with timing and frequency restrictions
 * - Shows popunder after 60 seconds on page
 * - Prevents showing again for 24 hours (or custom period)
 */

(function() {
  'use strict';

  const CONFIG = {
    DELAY_MS: 60000,           // 60 seconds before showing popunder
    COOLDOWN_MS: 12 * 60 * 60 * 1000,  // 24 hours cooldown
    STORAGE_KEY: 'popunder_last_shown',
    SCRIPT_URL: 'https://pl28621542.effectivegatecpm.com/fd/b3/8b/fdb38b98cea3639c3dbca8eea20d0126.js'
  };

  let timeoutId = null;
  let isShown = false;

  /**
   * Check if enough time has passed since last popunder
   */
  function canShowPopunder() {
    const lastShown = localStorage.getItem(CONFIG.STORAGE_KEY);
    if (!lastShown) return true;

    const lastShownTime = parseInt(lastShown, 10);
    const now = Date.now();
    const timePassed = now - lastShownTime;

    return timePassed >= CONFIG.COOLDOWN_MS;
  }

  /**
   * Record that popunder was shown
   */
  function recordPopunderShown() {
    localStorage.setItem(CONFIG.STORAGE_KEY, Date.now().toString());
  }

  /**
   * Show the popunder by loading the external script
   */
  function showPopunder() {
    if (isShown) return;
    if (!canShowPopunder()) return;

    isShown = true;
    recordPopunderShown();

    try {
      const script = document.createElement('script');
      script.src = CONFIG.SCRIPT_URL;
      script.async = true;
      
      // Return focus to original page after 5 seconds (gives ad time to load and register impression)
      script.onload = function() {
        setTimeout(() => {
          window.focus();
        }, 5000);
      };
      
      script.onerror = function() {
        console.error('Error loading popunder script');
        setTimeout(() => {
          window.focus();
        }, 5000);
        isShown = false;
      };
      
      document.head.appendChild(script);
      
      // Fallback: ensure focus returns after 5 seconds even if script doesn't fire events
      setTimeout(() => {
        window.focus();
      }, 5000);
    } catch (error) {
      console.error('Error loading popunder script:', error);
      isShown = false;
    }
  }

  /**
   * Initialize popunder timer
   */
  function init() {
    // Only initialize if user hasn't seen popunder recently
    if (!canShowPopunder()) {
      return;
    }

    // Set timer to show popunder after delay
    timeoutId = setTimeout(showPopunder, CONFIG.DELAY_MS);
  }

  /**
   * Cleanup function
   */
  function cleanup() {
    if (timeoutId) {
      clearTimeout(timeoutId);
      timeoutId = null;
    }
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Cleanup on page unload
  window.addEventListener('beforeunload', cleanup);

  // Expose API for debugging/control
  window.PopunderManager = {
    show: showPopunder,
    canShow: canShowPopunder,
    reset: function() {
      localStorage.removeItem(CONFIG.STORAGE_KEY);
      isShown = false;
    },
    getConfig: function() {
      return { ...CONFIG };
    }
  };
})();
