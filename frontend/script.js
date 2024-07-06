document.getElementById('image-upload').addEventListener('change', () => {
    const imageFile = document.getElementById('image-upload').files[0];

    if (imageFile) {
        const reader = new FileReader();
        reader.onload = (e) => {
            const imgElement = document.createElement('img');
            imgElement.src = e.target.result;
            imgElement.style.width = '100%'; //ensuring image fits within the container width
            imgElement.style.height = '100%'; //ensuring image fits within the container height
            
            const imagePreview = document.getElementById('image-preview');
            imagePreview.innerHTML = ''; // Clear previous image
            imagePreview.appendChild(imgElement);
        };
        reader.readAsDataURL(imageFile);
    }
});

document.getElementById('run-button').addEventListener('click', async () => {
    const apiKey = document.getElementById('api-key').value;
    const prompt = document.getElementById('prompt').value;
    const framework = document.getElementById('framework').value;
    const imageFile = document.getElementById('image-upload').files[0];

    if (!apiKey) {
        alert('API key is required!');
        return;
    }
    if (!imageFile) {
        alert('Image File is required!');
        return;
    }

    alert("Sit back, relax, and let me generate the code for you :D");

    const formData = new FormData();
    formData.append('api-key', apiKey);
    formData.append('prompt', prompt);
    formData.append('framework', framework);
    formData.append('image-upload', imageFile);

    try {
        const response = await fetch('http://127.0.0.1:5000/upload', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        document.getElementById('output').value = result.output || JSON.stringify(result, null, 2);
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while processing your request.');
    }
});

document.getElementById('copy-button').addEventListener('click', async () =>{

    var copyText = document.getElementById("output");
    copyText.select();
    copyText.setSelectionRange(0, 99999); // For mobile devices

    navigator.clipboard.writeText(copyText.value);

    alert("Copied");
});

document.getElementById('download-button').addEventListener('click', () => {
    var text = document.getElementById('output').value;
    var blob = new Blob([text], {type: 'text/html'});
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'text_as_html.html';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
});
