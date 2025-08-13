// Custom JavaScript for Flask Starter Pack

document.addEventListener('DOMContentLoaded', function () {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            if (alert.classList.contains('fade')) {
                alert.classList.remove('show');
            } else {
                alert.style.display = 'none';
            }
        }, 5000);
    });

    // Add fade-in animation to main content
    const mainContent = document.querySelector('main');
    if (mainContent) {
        mainContent.classList.add('fade-in');
    }

    // Form validation enhancement
    const forms = document.querySelectorAll('form');
    forms.forEach(function (form) {
        form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });

    // Back to top button
    const backToTopButton = document.createElement('button');
    backToTopButton.innerHTML = '↑';
    backToTopButton.className = 'btn btn-primary position-fixed';
    backToTopButton.style.cssText = `
        bottom: 20px;
        right: 20px;
        z-index: 1000;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        display: none;
    `;
    backToTopButton.setAttribute('title', 'Back to top');
    document.body.appendChild(backToTopButton);

    // Show/hide back to top button
    window.addEventListener('scroll', function () {
        if (window.pageYOffset > 300) {
            backToTopButton.style.display = 'block';
        } else {
            backToTopButton.style.display = 'none';
        }
    });

    // Smooth scroll to top
    backToTopButton.addEventListener('click', function () {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Console log for development
    console.log('Flask Starter Pack loaded successfully!');
});

// Utility functions
const FlaskApp = {
    // Show notification
    showNotification: function (message, type = 'info') {
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
        alertDiv.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;

        const container = document.querySelector('.container');
        if (container) {
            container.insertBefore(alertDiv, container.firstChild);
        }
    },

    // Confirm dialog
    confirm: function (message, callback) {
        if (confirm(message)) {
            callback();
        }
    },

    // AJAX helper
    ajax: function (url, options = {}) {
        const defaults = {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            }
        };

        const config = Object.assign(defaults, options);

        return fetch(url, config)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .catch(error => {
                console.error('AJAX Error:', error);
                this.showNotification('An error occurred. Please try again.', 'danger');
            });
    }
};

// Make FlaskApp globally available
window.FlaskApp = FlaskApp;
