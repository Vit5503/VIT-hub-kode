document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('signup-form');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Basic validation check (inputs already have 'required' in HTML)
        const firstName = document.getElementById('firstName').value.trim();
        const email = document.getElementById('email').value.trim();

        if (firstName && email) {
            // In a real application, you would send this data to a server here (e.g., using fetch API)
            
            // Simulation of successful submission
            alert(`Thank you, ${firstName}! We've received your sign-up with email: ${email}. Look out for our updates!`);

            // Optional: Clear the form after successful submission
            form.reset();
        } else {
            alert('Please fill in all required fields.');
        }
    });
});