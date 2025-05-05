import axios from 'axios';
import { API_URL, REFRESH_TOKEN_ENDPOINT } from './endpoints';
import Storage from './myStorage';
import { ACCEES_TOKEN, REFRESH_TOKEN, IS_AUTHENTICATED, IS_AUTHENTICATED_FALSE, IS_AUTHENTICATED_TRUE} from './actionTypes'


const axiosInstance = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

axiosInstance.interceptors.request.use(
    (config) => {
        const token = Storage.getItem(ACCEES_TOKEN);
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => Promise.reject(error)
);

axiosInstance.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;

        if (error.response?.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;

            try {
                const refreshToken = Storage.getItem(REFRESH_TOKEN);
                const response = await axios.post(REFRESH_TOKEN_ENDPOINT, {
                    token: refreshToken,
                });

                const { accessToken } = response.data;
                Storage.setItem(ACCEES_TOKEN, accessToken);

                axiosInstance.defaults.headers.Authorization = `Bearer ${accessToken}`;
                originalRequest.headers.Authorization = `Bearer ${accessToken}`;

                return axiosInstance(originalRequest);
            } catch (refreshError) {
                console.error('Refresh token failed', refreshError);
                // Handle logout or redirect to login
                return Promise.reject(refreshError);
            }
        }

        return Promise.reject(error);
    }
);

export default axiosInstance;