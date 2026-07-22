window.toast = (function () {
  let container = null;
  function getContainer() {
    if (!container) { container = document.createElement('div'); container.className = 'flash-wrap'; document.body.appendChild(container); }
    return container;
  }
  function show(message, type = 'info', duration = 3500) {
    const c = getContainer();
    const el = document.createElement('div');
    el.className = `flash-msg ${type}`;
    const icon = type === 'success' ? 'fa-check-circle' : type === 'error' ? 'fa-exclamation-circle' : 'fa-info-circle';
    el.innerHTML = `<i class="fas ${icon}"></i><span style="flex:1">${message}</span><button style="background:none;border:none;cursor:pointer;color:var(--text-3)" onclick="this.closest('.flash-msg').remove()"><i class="fas fa-times"></i></button>`;
    c.appendChild(el);
    setTimeout(() => { el.style.transition = 'opacity .3s,transform .3s'; el.style.opacity = '0'; el.style.transform = 'translateX(30px)'; setTimeout(() => el.remove(), 320); }, duration);
  }
  return { show, success: m => show(m, 'success'), error: m => show(m, 'error'), info: m => show(m, 'info') };
})();

// Lazy image fade-in
if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (en.isIntersecting) {
        const img = en.target;
        img.addEventListener('load', () => img.classList.add('loaded'), { once: true });
        io.unobserve(img);
      }
    });
  }, { rootMargin: '100px' });
  document.querySelectorAll('img[loading="lazy"]').forEach(img => io.observe(img));
}

// Native form validation → shake + red border instead of silent failure
document.querySelectorAll('form:not([novalidate])').forEach(form => {
  form.addEventListener('submit', e => {
    const invalids = form.querySelectorAll(':invalid');
    if (invalids.length) {
      invalids[0].focus();
      invalids.forEach(el => {
        el.classList.add('error');
        el.addEventListener('input', () => el.classList.remove('error'), { once: true });
      });
    }
  });
});

document.querySelectorAll('.print-btn').forEach(btn => btn.addEventListener('click', () => window.print()));
