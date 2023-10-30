document.addEventListener('DOMContentLoaded', function () {
    // Target the registration form
    const registerForm = document.getElementById('register-form');

    // Add an event listener for the registration form submission
    registerForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // Send a POST request to register a user
        fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message); // You can replace this with a more user-friendly message
        });
    });

    // Target the login form
    const loginForm = document.getElementById('login-form');

    // Add an event listener for the login form submission
    loginForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // Send a POST request to log in a user
        fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message); // You can replace this with a more user-friendly message
        });
    });

    // Target the add book form
    const addBookForm = document.getElementById('add-book-form');

    // Add an event listener for the add book form submission
    addBookForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const title = document.getElementById('title').value;
        const author = document.getElementById('author').value;

        // Send a POST request to add a book to the reading list
        fetch('/books', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer YOUR_JWT_TOKEN', // Replace with the actual JWT token
            },
            body: JSON.stringify({ title, author }),
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message); // You can replace this with a more user-friendly message
        });
    });
});

// Custom CSS styles can be added to styles.css
