```html
<!DOCTYPE html>
<html>
<head>
    <title>前端向后端请求示例</title>
</head>
<body>
    <h1>前端向后端请求示例</h1>
    <button id="getButton">GET 请求</button>
    <button id="postButton">POST 请求</button>

    <div id="response"></div>

    <script>
        document.getElementById('getButton').addEventListener('click', () => {
            fetch('/api/data', {
                method: 'GET',
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('response').innerText = JSON.stringify(data, null, 2);
            })
            .catch(error => {
                console.error('GET 请求出错:', error);
            });
        });

        document.getElementById('postButton').addEventListener('click', () => {
            const data = {
                key: 'value'
            };

            fetch('/api/data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('response').innerText = JSON.stringify(data, null, 2);
            })
            .catch(error => {
                console.error('POST 请求出错:', error);
            });
        });
    </script>
</body>
</html>

```

```python

```
