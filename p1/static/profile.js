document.addEventListener('DOMContentLoaded', function() {
    // Get the form element
    const form = document.querySelector('#upload-art form');

    // Add event listener for form submission
    form.addEventListener('submit', function(event) {
        // Prevent the default form submission
        event.preventDefault();

        // Validate the form fields
        const artName = document.querySelector('#art-name').value;
        const artDescription = document.querySelector('#art-description').value;
        const artFile = document.querySelector('#art-file').files[0];

        if (!artName || !artDescription || !artFile) {
            alert('Please fill in all fields.');
            return;
        }

        // If all fields are filled, submit the form via AJAX or perform other actions
        // Here, you can use fetch or XMLHttpRequest to send the form data to the server
        // Example using fetch:
        const formData = new FormData();
        formData.append('artName', artName);
        formData.append('artDescription', artDescription);
        formData.append('artFile', artFile);

        fetch('upload.php', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (response.ok) {
                    alert('Art uploaded successfully.');
                    // Reset the form after successful upload
                    form.reset();
                } else {
                    throw new Error('Error uploading art.');
                }
            })
            .catch(error => {
                console.error(error);
                alert('An error occurred while uploading art.');
            });
    });
});