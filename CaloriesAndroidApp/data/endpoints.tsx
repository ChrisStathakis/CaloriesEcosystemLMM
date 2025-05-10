export const  BASE_URL = "http://192.168.1.4:8000/";
// "http://192.168.1.5:8000/";

export const API_URL = BASE_URL + "api/";

export const LOGIN_ENDPOINT = API_URL + "token/";
export const REFRESH_TOKEN_ENDPOINT = API_URL + "token/refresh/";
export const PROFILE_ENDPOINT = API_URL + "profile/detail/";
export const HOMEPAGE_DATA_ENDPOINT = API_URL + "profile/homepage-data/";

export const RECIPE_LIST_ENFDPOINT = API_URL + "recipes/list/";
export const RECIPE_DETAIL_ENFDPOINT = API_URL + "recipes/detail/";

export const GRAPHQL_ENDPOINT = `${BASE_URL}graphql`;


// planning
export const DAY_CALORIES_LIST_ENDPOINT = `${API_URL}planning/day-calories/`
export const DAY_CALORIES_DETAIL_ENDPOINT = `${API_URL}planning/day-calories/`;
export const DAY_CATEGORY_LIST_ENDPOINT = `${API_URL}planning/day-categories/`;
export const USER_RECIPES_LIST_ENDPOINT = `${API_URL}planning/user-recipes/`;




export const getFullUrl = (path: string) => {
    if (!path.startsWith("http://") && !path.startsWith("https://")) {
        return `http://localhost:8081${path}`;
    }
    return path;
};

