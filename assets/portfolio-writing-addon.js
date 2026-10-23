(function(){
  'use strict';
  if (document.getElementById('writing-portfolio')) return;
  const section = document.createElement('section');
  section.id='writing-portfolio';
  section.className='maw-section';
  section.setAttribute('aria-labelledby','maw-heading');
  section.innerHTML = `
    <div class="maw-wrap">
      <div class="maw-header">
        <p class="maw-eyebrow">Selected writing · 2026</p>
        <h2 class="maw-heading" id="maw-heading">SEO, Writing &amp; Digital Marketing</h2>
        <p class="maw-intro">Research-led writing that connects search intent, business context, and practical communication. Two English samples drawn from my e-commerce and SaaS work.</p>
      </div>
      <div class="maw-grid">
        <article class="maw-card">
          <span class="maw-label">SEO research · Editorial article</span>
          <h3>Backlinks vs. Referring Domains</h3>
          <p>Why a large backlink count may be misleading, and a five-step review method for e-commerce websites.</p>
          <div class="maw-links"><a href="/writing/backlinks-vs-referring-domains/">Read article →</a><a href="/downloads/SEO_Backlinks_Referring_Domains_Morteza_Ahmadi.pdf">PDF sample</a></div>
        </article>
        <article class="maw-card">
          <span class="maw-label">SaaS · Landing page &amp; outreach copy</span>
          <h3>Revivio: A Clearer Path to WhatsApp</h3>
          <p>Marketing page and outreach email developed around a simple, honest offer for local service businesses.</p>
          <div class="maw-links"><a href="/writing/revivio-marketing-copy/">View copy →</a><a href="/downloads/Revivio_Marketing_Copy_Morteza_Ahmadi.pdf">PDF sample</a></div>
        </article>
      </div>
      <p class="maw-book"><strong>Book in progress:</strong> <em>Data-Driven Off-Page SEO and Link Building</em> — a Persian educational manuscript planned in 7 parts and 28 chapters; early lessons are drafted.</p>
    </div>`;
  const headings=[...document.querySelectorAll('h1,h2,h3')];
  const target=headings.find(el=>/selected\s*work|selected\s*projects|my\s*work|portfolio|projects|نمونه.?کار|پروژه/i.test(el.textContent || ''));
  const workSection=target ? target.closest('section') : null;
  const footer=document.querySelector('footer');
  if(workSection && workSection.parentNode) workSection.insertAdjacentElement('afterend',section);
  else if(footer && footer.parentNode) footer.insertAdjacentElement('beforebegin',section);
  else (document.querySelector('main')||document.body).appendChild(section);
  const nav=document.querySelector('header nav, .navbar, nav[aria-label="Main"], nav[aria-label="Primary"]');
  if(nav && !nav.querySelector('a[href="#writing-portfolio"]')) {
    const link=document.createElement('a'); link.href='#writing-portfolio'; link.textContent='SEO & Writing';link.className='maw-navlink';nav.appendChild(link);
  }
})();
