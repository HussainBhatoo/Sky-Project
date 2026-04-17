// Sky Engineering Team Registry
// assets/js/app.js
// Author: Maurya Patel (Student 4 — Lead)
// 
// Shared JavaScript for the base template.
// Handles: live search debounce, sidebar 
// collapse/expand with localStorage persistence.

document.addEventListener('DOMContentLoaded', function() {
    /**
     * SEARCH SUBSYSTEM
     * Implements a debounced AJAX search to minimize server load.
     */
    const searchInput = document.getElementById('search-input');
    const resultsDropdown = document.getElementById('search-results');
    
    // Live search — sends a GET request to
    // /search/ after the user stops typing
    // for 300ms. The delay stops us hammering
    // the server on every single keystroke.
    if (searchInput) {
        let debounceTimer;
        searchInput.addEventListener('input', (e) => {
            const query = e.target.value.trim();
            clearTimeout(debounceTimer);

            if (query.length > 1) {
                debounceTimer = setTimeout(() => {
                    fetch(`/search/?q=${encodeURIComponent(query)}`)
                        .then(response => response.json())
                        .then(data => {
                            if (data.results && data.results.length > 0) {
                                resultsDropdown.innerHTML = `
                                    <div class="search-result-header">RESULTS FOR: "${query}"</div>
                                    ${data.results.map(item => `
                                        <a href="${item.url}" class="search-result-item" style="text-decoration: none; color: inherit; display: flex; align-items: center; gap: 12px; transition: background 0.2s ease;">
                                            <i class='bx ${item.icon}' style="color: var(--sky-primary); font-size: 1.2rem;"></i>
                                            <div style="flex: 1; min-width: 0;">
                                                <div style="font-weight: 600; font-size: 0.9rem; color: var(--sky-header-blue); overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${item.title}</div>
                                                <div style="font-size: 0.7rem; color: var(--muted-foreground); text-transform: uppercase; letter-spacing: 0.5px;">${item.category}</div>
                                            </div>
                                        </a>
                                    `).join('')}
                                `;
                                resultsDropdown.classList.add('is-active');
                            } else {
                                resultsDropdown.innerHTML = `
                                    <div class="search-result-header">NO RESULTS FOR: "${query}"</div>
                                    <div class="search-result-item" style="opacity: 0.6; pointer-events: none;">
                                        <i class='bx bx-info-circle'></i>
                                        <span>Try specific team names or departments.</span>
                                    </div>
                                `;
                                resultsDropdown.classList.add('is-active');
                            }
                        })
                        .catch(err => {
                            console.error("Search Fail:", err);
                        });
                }, 300); // 300ms debounce
            } else {
                resultsDropdown.classList.remove('is-active');
                resultsDropdown.innerHTML = '';
            }
        });

        // Close search results when clicking outside the component
        // This keeps the UI clean and focused.
        document.addEventListener('click', (e) => {
            const searchContainer = document.getElementById('global-search');
            if (searchContainer && !searchContainer.contains(e.target)) {
                resultsDropdown.classList.remove('is-active');
            }
        });
    }

    /**
     * LAYOUT SUBSYSTEM
     * Handles sidebar state persistence and responsive toggling.
     */
    const sidebarToggle = document.getElementById('sidebar-toggle');
    if (sidebarToggle) {
        // Remember sidebar state across page loads
        // using localStorage. If the user collapses
        // the sidebar it stays collapsed when they
        // navigate to a new page.
        if (localStorage.getItem('sidebar-collapsed') === 'true') {
            document.body.classList.add('sidebar-collapsed');
        }
        
        sidebarToggle.addEventListener('click', () => {
            document.body.classList.toggle('sidebar-collapsed');
            localStorage.setItem('sidebar-collapsed', document.body.classList.contains('sidebar-collapsed'));
        });
    }

    /**
     * ACCOUNT NAVIGATION
     * Simple click-to-expand logic for the user profile menu.
     */
    const dropdownBtn = document.getElementById('user-dropdown-btn');
    const dropdownMenu = document.getElementById('user-dropdown-menu');
    const dropdownContainer = document.getElementById('user-dropdown-container');
    
    if (dropdownBtn && dropdownMenu) {
        dropdownBtn.addEventListener('click', (e) => {
            dropdownMenu.classList.toggle('active');
        });
        
        // Auto-close dropdown if clicking elsewhere in the workspace
        document.addEventListener('click', (e) => {
            if (dropdownContainer && !dropdownContainer.contains(e.target)) {
                dropdownMenu.classList.remove('active');
            }
        });
    }

});
