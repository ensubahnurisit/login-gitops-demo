async function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const response = await fetch(
    "http://192.168.49.2:30001/login",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ username, password })
    }
  );

  const data = await response.json();

  document.getElementById("result").innerText = data.message;
}
