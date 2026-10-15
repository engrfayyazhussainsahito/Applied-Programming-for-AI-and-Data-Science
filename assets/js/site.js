/**
 * MS Applied Programming (Python) Interactive Learning Platform
 * Core Engine & Interactive UI Controller
 */

(function () {
  'use strict';

  // State & Storage Keys
  const STORAGE_THEME = 'msap_theme';
  const STORAGE_PROGRESS = 'msap_completed_lessons';
  const STORAGE_BOOKMARKS = 'msap_bookmarks';

  // DOM Elements
  const body = document.body;
  const root = body.getAttribute('data-root') || '';
  const pageId = body.getAttribute('data-page-id') || '';
  const pageTitle = body.getAttribute('data-title') || document.title;

  // Initialize Theme
  function initTheme() {
    const savedTheme = localStorage.getItem(STORAGE_THEME) || 'dark';
    document.documentElement.setAttribute('data-theme', savedTheme);

    document.querySelectorAll('.theme-toggle, .theme-toggle-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem(STORAGE_THEME, newTheme);
      });
    });
  }

  // Reading Progress Bar
  function initReadingProgress() {
    const progressBar = document.getElementById('readingProgress');
    if (!progressBar) return;

    window.addEventListener('scroll', () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
      progressBar.style.width = Math.min(100, Math.max(0, progress)) + '%';
    });
  }

  // Mobile Sidebar
  function initSidebar() {
    const sidebar = document.getElementById('sidebar');
    const openBtn = document.getElementById('openSidebar');
    const closeBtn = document.getElementById('closeSidebar');

    if (openBtn && sidebar) {
      openBtn.addEventListener('click', () => sidebar.classList.add('open'));
    }
    if (closeBtn && sidebar) {
      closeBtn.addEventListener('click', () => sidebar.classList.remove('open'));
    }
    document.addEventListener('click', (e) => {
      if (sidebar && sidebar.classList.contains('open') && !sidebar.contains(e.target) && e.target !== openBtn) {
        sidebar.classList.remove('open');
      }
    });
  }

  // Build Table of Contents & ScrollSpy
  function initTOC() {
    const tocList = document.getElementById('tocList');
    const article = document.querySelector('.article');
    if (!tocList || !article) return;

    const headings = article.querySelectorAll('h2, h3');
    tocList.innerHTML = '';

    headings.forEach((heading, idx) => {
      let id = heading.id;
      if (!id) {
        id = 'heading-' + idx;
        heading.id = id;
      }
      const li = document.createElement('li');
      if (heading.tagName.toLowerCase() === 'h3') {
        li.style.paddingLeft = '0.75rem';
        li.style.fontSize = '0.8rem';
      }
      const link = document.createElement('a');
      link.href = '#' + id;
      link.textContent = heading.textContent.replace(/^\d+\.\s*/, '');
      li.appendChild(link);
      tocList.appendChild(li);
    });

    // ScrollSpy
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.id;
          document.querySelectorAll('#tocList a').forEach(a => {
            if (a.getAttribute('href') === '#' + id) {
              a.classList.add('active');
            } else {
              a.classList.remove('active');
            }
          });
        }
      });
    }, { rootMargin: '0px 0px -65% 0px' });

    headings.forEach(h => observer.observe(h));
  }

  // Progress Tracker & Bookmarks
  function initProgressAndBookmarks() {
    let completed = JSON.parse(localStorage.getItem(STORAGE_PROGRESS) || '[]');
    let bookmarks = JSON.parse(localStorage.getItem(STORAGE_BOOKMARKS) || '[]');

    const completeBtn = document.getElementById('completeBtn');
    const bookmarkBtn = document.getElementById('bookmarkBtn');

    function updateButtons() {
      if (completeBtn) {
        const isDone = completed.includes(pageId);
        completeBtn.textContent = isDone ? '✓ Completed' : 'Mark Complete';
        completeBtn.className = isDone ? 'btn btn-success' : 'btn';
      }
      if (bookmarkBtn) {
        const isBookmarked = bookmarks.includes(pageId);
        bookmarkBtn.textContent = isBookmarked ? '★ Bookmarked' : '☆ Bookmark';
        bookmarkBtn.className = isBookmarked ? 'btn btn-primary' : 'btn';
      }
    }

    if (completeBtn && pageId) {
      completeBtn.addEventListener('click', () => {
        if (completed.includes(pageId)) {
          completed = completed.filter(id => id !== pageId);
        } else {
          completed.push(pageId);
        }
        localStorage.setItem(STORAGE_PROGRESS, JSON.stringify(completed));
        updateButtons();
        updateNavProgressMarkers();
      });
    }

    if (bookmarkBtn && pageId) {
      bookmarkBtn.addEventListener('click', () => {
        if (bookmarks.includes(pageId)) {
          bookmarks = bookmarks.filter(id => id !== pageId);
        } else {
          bookmarks.push(pageId);
        }
        localStorage.setItem(STORAGE_BOOKMARKS, JSON.stringify(bookmarks));
        updateButtons();
      });
    }

    updateButtons();
  }

  // Update Nav Items with Progress Markers
  function updateNavProgressMarkers() {
    const completed = JSON.parse(localStorage.getItem(STORAGE_PROGRESS) || '[]');
    document.querySelectorAll('.nav-lesson-item').forEach(item => {
      const pid = item.getAttribute('data-page-id');
      const check = item.querySelector('.lesson-check');
      if (check && pid) {
        if (completed.includes(pid)) {
          check.textContent = '●';
          check.classList.add('completed');
        } else {
          check.textContent = '○';
          check.classList.remove('completed');
        }
      }
    });
  }

  // Render Dynamic Navigation Tree
  function initCourseNav() {
    const navContainer = document.getElementById('courseNav');
    if (!navContainer || typeof window.COURSE_NAV_DATA === 'undefined') return;

    const weeks = window.COURSE_NAV_DATA;
    let html = `
      <div class="nav-section-title">Core Navigation</div>
      <a class="nav-link ${pageId === 'home' ? 'active' : ''}" href="${root}index.html">🏠 Home & Curriculum</a>
      <a class="nav-link ${pageId === 'interactive-lab' ? 'active' : ''}" href="${root}interactive-lab.html">⚡ Interactive Python Lab</a>
      <a class="nav-link ${pageId === 'architecture' ? 'active' : ''}" href="${root}architecture.html">📐 Course Specs & Blueprint</a>
      <a class="nav-link ${pageId === 'glossary' ? 'active' : ''}" href="${root}glossary.html">📖 Python Glossary</a>
      <a class="nav-link ${pageId === 'search' ? 'active' : ''}" href="${root}search.html">🔍 Course Search</a>
      <div class="nav-section-title">Curriculum Weeks (1 - 15)</div>
    `;

    weeks.forEach(week => {
      const isCurrentWeek = pageId.startsWith(`week-${String(week.num).padStart(2, '0')}`);
      html += `
        <div class="nav-week-group ${isCurrentWeek ? 'open' : ''}">
          <button class="nav-week-btn" type="button">
            <span><strong>W${week.num}:</strong> ${week.title}</span>
            <span class="caret">▶</span>
          </button>
          <div class="nav-lesson-list">
            <a class="nav-lesson-item" href="${root}weeks/${week.slug}/index.html">
              <span class="lesson-check">📑</span>
              <span>Week Overview</span>
            </a>
            ${week.lessons.map(l => {
              const lessonPageId = `week-${String(week.num).padStart(2, '0')}/lesson-${l.num.replace('.', '-')}`;
              const isActive = pageId === lessonPageId;
              return `
                <a class="nav-lesson-item ${isActive ? 'active' : ''}" data-page-id="${lessonPageId}" href="${root}weeks/${week.slug}/${l.slug}.html">
                  <span class="lesson-check">○</span>
                  <span>${l.num} ${l.title}</span>
                </a>
              `;
            }).join('')}
          </div>
        </div>
      `;
    });

    navContainer.innerHTML = html;

    // Accordion interaction
    navContainer.querySelectorAll('.nav-week-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const group = btn.closest('.nav-week-group');
        group.classList.toggle('open');
      });
    });

    updateNavProgressMarkers();
  }

  // Interactive Quiz Toggle
  function initQuizEngine() {
    const quizModeBtn = document.getElementById('quizModeBtn');
    const quizList = document.querySelector('.quiz-list');

    if (quizList) {
      quizList.querySelectorAll('li').forEach(li => {
        const questionText = li.textContent;
        const answer = li.getAttribute('data-answer') || 'Consult lesson core concepts section.';
        li.className = 'quiz-item';
        li.innerHTML = `
          <div class="quiz-question">${questionText}</div>
          <button class="quiz-toggle-btn" type="button">Reveal Solution & Key Insight</button>
          <div class="quiz-answer">${answer}</div>
        `;
        const toggleBtn = li.querySelector('.quiz-toggle-btn');
        const ansBox = li.querySelector('.quiz-answer');
        toggleBtn.addEventListener('click', () => {
          const isVisible = ansBox.classList.toggle('visible');
          toggleBtn.textContent = isVisible ? 'Hide Solution' : 'Reveal Solution & Key Insight';
        });
      });
    }

    if (quizModeBtn && quizList) {
      quizModeBtn.addEventListener('click', () => {
        const allAnswers = quizList.querySelectorAll('.quiz-answer');
        const anyHidden = Array.from(allAnswers).some(a => !a.classList.contains('visible'));
        allAnswers.forEach(a => {
          if (anyHidden) a.classList.add('visible');
          else a.classList.remove('visible');
        });
        quizList.querySelectorAll('.quiz-toggle-btn').forEach(b => {
          b.textContent = anyHidden ? 'Hide Solution' : 'Reveal Solution & Key Insight';
        });
      });
    }
  }

  // Code Copy Buttons
  function initCodeCopy() {
    document.querySelectorAll('pre').forEach(pre => {
      const copyBtn = document.createElement('button');
      copyBtn.className = 'btn btn-sm';
      copyBtn.style.position = 'absolute';
      copyBtn.style.top = '0.5rem';
      copyBtn.style.right = '0.5rem';
      copyBtn.style.fontSize = '0.72rem';
      copyBtn.style.padding = '0.2rem 0.5rem';
      copyBtn.textContent = 'Copy';

      copyBtn.addEventListener('click', () => {
        const code = pre.querySelector('code');
        const text = code ? code.innerText : pre.innerText;
        navigator.clipboard.writeText(text).then(() => {
          copyBtn.textContent = 'Copied!';
          setTimeout(() => { copyBtn.textContent = 'Copy'; }, 1800);
        });
      });

      pre.appendChild(copyBtn);
    });
  }

  // Global Search Modal (Ctrl+K)
  function initSearchModal() {
    const modalBackdrop = document.createElement('div');
    modalBackdrop.className = 'search-modal-backdrop';
    modalBackdrop.innerHTML = `
      <div class="search-modal">
        <div class="search-modal-header">
          <span>🔍</span>
          <input type="text" class="search-modal-input" placeholder="Search 30 lessons, Python topics, algorithms (Ctrl+K)...">
          <span style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono)">ESC</span>
        </div>
        <div class="search-results-list" id="modalSearchResults">
          <div style="padding:1.5rem; text-align:center; color:var(--text-muted); font-size:0.9rem">Type to search across the Applied Python curriculum...</div>
        </div>
      </div>
    `;
    document.body.appendChild(modalBackdrop);

    const input = modalBackdrop.querySelector('.search-modal-input');
    const resultsContainer = modalBackdrop.querySelector('#modalSearchResults');

    function openSearch() {
      modalBackdrop.classList.add('open');
      input.value = '';
      input.focus();
    }

    function closeSearch() {
      modalBackdrop.classList.remove('open');
    }

    window.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        openSearch();
      }
      if (e.key === 'Escape' && modalBackdrop.classList.contains('open')) {
        closeSearch();
      }
    });

    modalBackdrop.addEventListener('click', (e) => {
      if (e.target === modalBackdrop) closeSearch();
    });

    document.querySelectorAll('#navSearch, .site-search-input').forEach(inp => {
      inp.addEventListener('focus', () => {
        openSearch();
        inp.blur();
      });
    });

    input.addEventListener('input', () => {
      const q = input.value.trim().toLowerCase();
      if (!q || typeof window.SEARCH_INDEX === 'undefined') {
        resultsContainer.innerHTML = `<div style="padding:1.5rem; text-align:center; color:var(--text-muted); font-size:0.9rem">Type to search across the Applied Python curriculum...</div>`;
        return;
      }

      const matches = window.SEARCH_INDEX.filter(item => {
        return item.title.toLowerCase().includes(q) ||
               (item.summary && item.summary.toLowerCase().includes(q)) ||
               (item.keywords && item.keywords.toLowerCase().includes(q));
      }).slice(0, 10);

      if (matches.length === 0) {
        resultsContainer.innerHTML = `<div style="padding:1.5rem; text-align:center; color:var(--text-muted); font-size:0.9rem">No matching topics found for "<strong>${q}</strong>".</div>`;
        return;
      }

      resultsContainer.innerHTML = matches.map(m => `
        <a href="${root}${m.url}" class="search-result-item">
          <div class="search-result-title">${m.title}</div>
          <div class="search-result-crumb">${m.week || 'Course Lesson'} · ${m.difficulty || 'Intermediate'}</div>
        </a>
      `).join('');
    });
  }

  // Print PDF Trigger
  function initPrint() {
    document.querySelectorAll('.print-page').forEach(btn => {
      btn.addEventListener('click', () => window.print());
    });
  }

  // Initialize Mermaid if present
  function initMermaid() {
    if (typeof window.mermaid !== 'undefined') {
      window.mermaid.initialize({
        startOnLoad: true,
        theme: document.documentElement.getAttribute('data-theme') === 'light' ? 'default' : 'dark',
        securityLevel: 'loose',
        flowchart: { useMaxWidth: true, htmlLabels: true, curve: 'basis' }
      });
    }
  }

  // DOM Ready
  document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initReadingProgress();
    initSidebar();
    initTOC();
    initCourseNav();
    initProgressAndBookmarks();
    initQuizEngine();
    initCodeCopy();
    initSearchModal();
    initPrint();
    initMermaid();
  });
})();
