// static/js/errorHandler.js

const ErrorValidator = {

    clearAllErrors: function() {
        document.querySelectorAll('.error-message').forEach(el => {
            el.textContent = '';
            el.classList.remove('visible');
        });

        document.querySelectorAll('.has-error').forEach(el => {
            el.classList.remove('has-error');
        });
    },

    showFieldError: function(fieldName, message) {
        const errorElement = document.getElementById(`${fieldName}`);
        const inputElement = document.getElementById(fieldName);

        if (errorElement) {
            errorElement.textContent = message;
            errorElement.classList.add('visible');
        }

        if (inputElement) {
            inputElement.classList.add('has-error');
            inputElement.focus();
        }
    },

    displayErrors: function(errors) {
        this.clearAllErrors();
        if (!errors) return;

        Object.keys(errors).forEach(field => {
            const errorMessages = errors[field];
            if (errorMessages && errorMessages.length > 0) {
                const message = errorMessages[0].message || errorMessages[0];
                this.showFieldError(field, message);
            }
        });
    },

    displayGeneralError: function(message) {
        const container = document.getElementById('global-errors');
        if (container) {
            container.innerHTML = `<div class="alert alert-error">${message}</div>`;
        } else {
            alert(message);
        }
    }
};


window.ErrorValidator = ErrorValidator;