const API_CONFIG = {
    BASE_URL: 'https://jsonplaceholder.typicode.com',
    TIMEOUT: 5000
};

const PostService = {
    async fetchUserPosts(userId = 1) {
        try {
            const { data } = await axios.get(`${API_CONFIG.BASE_URL}/posts`, {
                params: { userId },
                timeout: API_CONFIG.TIMEOUT
            });
            return data;
        } catch (error) {
            throw this._handleError(error);
        }
    },

    _handleError(error) {
        return {
            message: error.response?.statusText || "Network request failed",
            status: error.response?.status || 500
        };
    }
};

const UI = {
    renderPosts(posts) {
        const container = document.querySelector('#content');
        container.innerHTML = posts.map(({ title, body }) => `
            <div class="card">
                <h4>${title}</h4>
                <p>${body.substring(0, 50)}...</p>
            </div>
        `).join('');
    },
    
    toggleLoading(isLoading) {
        document.querySelector('#status').innerText = isLoading ? "Fetching data..." : "";
    }
};

(async () => {
    try {
        UI.toggleLoading(true);
        const posts = await PostService.fetchUserPosts(1);
        UI.renderPosts(posts);
    } catch (err) {
        console.error(`Error ${err.status}: ${err.message}`);
    } finally {
        UI.toggleLoading(false);
    }
})();