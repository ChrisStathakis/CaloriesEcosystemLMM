import axiosInstance from "../axiosInstanceHTTP";
import { DAY_CALORIES_DETAIL_ENDPOINT, DAY_CALORIES_LIST_ENDPOINT, DAY_CATEGORY_LIST_ENDPOINT, USER_RECIPES_LIST_ENDPOINT } from "../endpoints";



export async function fetch_day_calorie_detail(selectedDate: string) {
    const url = DAY_CALORIES_DETAIL_ENDPOINT + selectedDate + "/";
    const response = await axiosInstance.get(url);
    try {
        if (response.status === 200) {
            console.log("response", response.data);
            return response.data;
        } else {
            console.error('Error fetching profile:', response.statusText);
            return null;
        }   
    }
    catch (error) {
        console.error("Error fetching profile:", error);
    }
    
};


export async function fetch_day_calorie_list() {
    const response = await axiosInstance.get(DAY_CALORIES_LIST_ENDPOINT);
    try {
        if (response.status === 200) {
            console.log("response", response.data);
            return response.data;
        } else {
            console.error('Error fetching profile:', response.statusText);
            return null;
        }   
    }
    catch (error) {
        console.error("Error fetching profile:", error);
    }
}


export const fetch_day_categories = async (day_calories_id: string) => {
    const endpoint =  `${DAY_CATEGORY_LIST_ENDPOINT}?day_calories=${day_calories_id}`;
    const response = await axiosInstance.get(endpoint);

    try {
        if (response.status === 200) {
            console.log("response", response.data);
            return response.data;
        } else {
            console.error('Error fetching profile:', response.statusText);
            return null;
        }   
    }
    catch (error) {
        console.error("Error fetching profile:", error);
    }
}


export const fetch_user_recipes = async (day_calories_id: string) => {
    const endpoint =  `${USER_RECIPES_LIST_ENDPOINT}?day_calories=${day_calories_id}`;
    const response = await axiosInstance.get(endpoint);

    try {
        if (response.status === 200) {
            console.log("response", response.data);
            return response.data;
        } else {
            console.error('Error fetching profile:', response.statusText);
            return null;
        }   
    }
    catch (error) {
        console.error("Error fetching profile:", error);
    }
}