const menuToggle = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#site-navigation');

menuToggle?.addEventListener('click', () => {
  const expanded = menuToggle.getAttribute('aria-expanded') === 'true';
  menuToggle.setAttribute('aria-expanded', String(!expanded));
  navigation.classList.toggle('navigation--open', !expanded);
});

const searchDialog = document.querySelector('.search-dialog');
const searchInput = document.querySelector('#search-query');
const searchStatus = document.querySelector('.search-dialog__status');
const searchResults = document.querySelector('.search-dialog__results');
let searchDocuments;
let searchRequest;
let searchSequence = 0;

const loadSearch = async () => {
  if (searchDocuments) {
    return searchDocuments;
  }
  if (!searchRequest) {
    searchRequest = fetch(document.body.dataset.searchIndex)
      .then((response) => {
        if (!response.ok) {
          throw new Error('SEARCH_UNAVAILABLE');
        }
        return response.json();
      })
      .then((index) => {
        searchDocuments = index.docs.filter(
          (entry) =>
            !entry.location.includes('#') &&
            entry.location.startsWith('en/') ===
              (document.body.dataset.language === 'en'),
        );
        return searchDocuments;
      })
      .catch((error) => {
        searchRequest = undefined;
        throw error;
      });
  }
  return searchRequest;
};

const updateSearch = async () => {
  const sequence = ++searchSequence;
  const query = searchInput.value.trim().toLocaleLowerCase();
  searchResults.replaceChildren();
  if (!query) {
    searchStatus.textContent = searchDialog.dataset.hint;
    return;
  }
  try {
    const documents = await loadSearch();
    if (sequence !== searchSequence) {
      return;
    }
    const terms = query.split(/\s+/);
    const matches = documents
      .map((entry) => {
        const title = entry.title.toLocaleLowerCase();
        const text = `${title} ${entry.text}`.toLocaleLowerCase();
        return {
          ...entry,
          score: terms.every((term) => text.includes(term))
            ? 1 + terms.filter((term) => title.includes(term)).length
            : 0,
        };
      })
      .filter((entry) => entry.score > 0)
      .sort((first, second) => second.score - first.score)
      .slice(0, 8);
    searchStatus.textContent = matches.length ? '' : searchDialog.dataset.empty;
    for (const entry of matches) {
      const item = document.createElement('li');
      const link = document.createElement('a');
      const destination = new URL(
        entry.location,
        new URL(document.body.dataset.searchBase, location.href),
      );
      if (destination.origin !== location.origin) {
        continue;
      }
      link.href = destination.href;
      link.textContent = entry.title;
      const excerpt = document.createElement('small');
      excerpt.textContent = entry.text.slice(0, 140).replace(/\s+/g, ' ');
      link.append(excerpt);
      item.append(link);
      searchResults.append(item);
    }
  } catch {
    if (sequence === searchSequence) {
      searchStatus.textContent = searchDialog.dataset.error;
    }
  }
};

const openSearch = () => {
  if (!searchDialog.open) {
    searchDialog.showModal();
    searchInput.focus();
    updateSearch();
  }
};

document.querySelectorAll('[data-open-search]').forEach((button) => {
  button.addEventListener('click', openSearch);
});
searchInput?.addEventListener('input', updateSearch);
document.addEventListener('keydown', (event) => {
  const editable = event.target.closest(
    'input, textarea, [contenteditable="true"]',
  );
  if (
    !editable &&
    (event.key === '/' ||
      ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k'))
  ) {
    event.preventDefault();
    openSearch();
  }
});
searchDialog?.addEventListener('click', (event) => {
  if (event.target === searchDialog) {
    const rectangle = searchDialog.getBoundingClientRect();
    if (
      event.clientX < rectangle.left ||
      event.clientX > rectangle.right ||
      event.clientY < rectangle.top ||
      event.clientY > rectangle.bottom
    ) {
      searchDialog.close();
    }
  }
});
