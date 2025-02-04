async function fetchPageDetails() {
    const username = document.getElementById('username').value;
    const resultDiv = document.getElementById('result');
    
    try {
        const response = await fetch(`http://127.0.0.1:8000/api/pages/${username}`);
        
        if (!response.ok) {
            throw new Error('Page not found');
        }
        
        const data = await response.json();
        resultDiv.innerHTML = `
            <h2>Page Details:</h2>
            <p><strong>Page Name:</strong> ${data.page_name}</p>
            <p><strong>Page URL:</strong> ${data.page_url}</p>
            <p><strong>Facebook ID:</strong> ${data.facebook_id}</p>
            <p><strong>Profile Picture:</strong> <img src="${data.profile_pic}" alt="${data.page_name}" width="100"></p>
            <p><strong>Email:</strong> ${data.email || 'N/A'}</p>
            <p><strong>Website:</strong> ${data.website || 'N/A'}</p>
            <p><strong>Category:</strong> ${data.category}</p>
            <p><strong>Followers Count:</strong> ${data.followers_count}</p>
            <p><strong>Likes Count:</strong> ${data.likes_count}</p>
            <p><strong>Creation Date:</strong> ${data.creation_date || 'N/A'}</p>
        `;
    } catch (error) {
        resultDiv.innerHTML = `<p style="color: red;">${error.message}</p>`;
    }
}
