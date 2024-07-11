const fileInput = document.getElementById('file');
const query = document.getElementById('query');
const submitBtn = document.getElementById('submit');
const result = document.getElementById('result');

submitBtn.addEventListener("click", async () => {
    result.innerHTML = 'Processing...';
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);
    formData.append('query', query.value);
    const response = await fetch('http://127.0.0.1:8000/recognize/', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    result.innerHTML = data.response;

})