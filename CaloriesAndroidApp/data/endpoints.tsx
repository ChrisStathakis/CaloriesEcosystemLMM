export const BASE_URL = "http://192.168.1.5:8000/";
export const API_URL = BASE_URL + "api/";

export const LOGIN_ENDPOINT = API_URL + "token/";
export const REFRESH_TOKEN_ENDPOINT = API_URL + "token/refresh/";
export const PROFILE_ENDPOINT = API_URL + "users/profile/";

export const RECIPE_LIST_ENFDPOINT = API_URL + "recipes/list/";
export const RECIPE_DETAIL_ENFDPOINT = API_URL + "recipes/detail/";

export const GRAPHQL_ENDPOINT = `${BASE_URL}graphql`;



export const getFullUrl = (path: string) => {
    if (!path.startsWith("http://") && !path.startsWith("https://")) {
        return `http://localhost:8081${path}`;
    }
    return path;
};

