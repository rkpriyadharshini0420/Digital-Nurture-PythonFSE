import axios from 'axios';

const BASE_URL = 'https://jsonplaceholder.typicode.com'; 

const apiClient = axios.create({
  baseURL: BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

apiClient.interceptors.request.use(
  (config) => {
    config.headers.Authorization = 'Bearer mock-token-123';
    return config;
  },
  (error) => Promise.reject(error)
);

apiClient.interceptors.response.use(
  (response) => response.data,
  (error) => {
   
    console.error('API Error:', {
      message: error.message,
      response: error.response,
      config: error.config
    });

    const customError = {
      message: error.response?.data?.message || error.message || 'Something went wrong',
      statusCode: error.response?.status || 500,
    };
    
    return Promise.reject(customError);
  }
);

export default apiClient;