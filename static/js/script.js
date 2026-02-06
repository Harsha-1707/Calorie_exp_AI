document.getElementById('prediction-form').addEventListener('submit', async function(e) {
    e.preventDefault();

    const form = e.target;
    const btn = document.getElementById('predict-btn');
    const resultContainer = document.getElementById('result-container');
    const resultValue = document.getElementById('result-value');

    // UI Loading State
    btn.classList.add('loading');
    resultContainer.classList.add('hidden');

    // Gather data
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    // Convert types
    for (const key in data) {
        data[key] = parseFloat(data[key]);
    }

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        const result = await response.json();

        if (response.ok) {
            // Simulate a small delay for better UX (so user sees something happening)
            setTimeout(() => {
                resultValue.textContent = result.calories.toFixed(1);
                resultContainer.classList.remove('hidden');
                btn.classList.remove('loading');
            }, 600);
        } else {
            alert('Error: ' + result.error);
            btn.classList.remove('loading');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
        btn.classList.remove('loading');
    }
});
