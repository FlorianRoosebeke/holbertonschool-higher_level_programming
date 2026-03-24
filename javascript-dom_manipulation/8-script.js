document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(res => res.json())
    .then(data => {
      const hello = document.getElementById('hello');
      hello.textContent = data.hello;
    })
    .catch(error => console.error('Error:', error));
});