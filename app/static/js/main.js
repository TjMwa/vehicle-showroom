// Main JavaScript for Vehicle Showroom

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    if (typeof bootstrap !== 'undefined') {
        var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }
    
    // Price formatter
    function formatPrice(price) {
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
            minimumFractionDigits: 2
        }).format(price);
    }
    
    // Image preview for uploads
    const imageInput = document.getElementById('image');
    if (imageInput) {
        const imagePreview = document.getElementById('image-preview');
        
        imageInput.addEventListener('change', function() {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                
                reader.addEventListener('load', function() {
                    imagePreview.src = reader.result;
                    imagePreview.style.display = 'block';
                });
                
                reader.readAsDataURL(file);
            }
        });
    }
    
    // Form validation enhancement
    const forms = document.querySelectorAll('.needs-validation');
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Vehicle search/filter enhancement
    const filterForm = document.querySelector('form[action*="vehicles"]');
    if (filterForm) {
        const minPriceInput = document.getElementById('min_price');
        const maxPriceInput = document.getElementById('max_price');
        
        // Price validation
        if (minPriceInput && maxPriceInput) {
            filterForm.addEventListener('submit', function(e) {
                const minPrice = parseFloat(minPriceInput.value);
                const maxPrice = parseFloat(maxPriceInput.value);
                
                if (minPrice && maxPrice && minPrice > maxPrice) {
                    e.preventDefault();
                    alert('Minimum price cannot be greater than maximum price');
                    minPriceInput.focus();
                }
            });
        }
    }
    
    // Add loading spinner to submit buttons (optional enhancement)
    // Only apply if form is valid to avoid getting stuck
    const submitButtons = document.querySelectorAll('button[type="submit"]');
    submitButtons.forEach(button => {
        button.addEventListener('click', function() {
            if (this.form && this.form.checkValidity()) {
                // Short delay to allow browser to start submission
                setTimeout(() => {
                    const spinner = document.createElement('span');
                    spinner.className = 'spinner-border spinner-border-sm ms-2';
                    spinner.setAttribute('role', 'status');
                    spinner.setAttribute('aria-hidden', 'true');
                    
                    if (!this.querySelector('.spinner-border')) {
                        this.appendChild(spinner);
                        this.disabled = true;
                    }
                }, 10);
            }
        });
    });
});
