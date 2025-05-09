import axiosInstance from "../axiosInstanceHTTP";

import Storage from "../myStorage";
import  { PROFILE_ENDPOINT, HOMEPAGE_DATA_ENDPOINT } from '../endpoints';
import { PROFILE_ID } from "../actionTypes";


export async function fetch_profile(){
    try {
        const resposse = await axiosInstance.get(PROFILE_ENDPOINT);
        if (resposse.status === 200) {
            console.log("Profile data fetched successfully:", resposse.data);
            Storage.setItem(PROFILE_ID, resposse.data.id.toString());
            return resposse.data;
            
        } else {
            throw new Error("Failed to fetch profile data");
        }
    }
    catch (error) {
        console.error("Error fetching profile data:", error);
        throw error;
    }
};


export async function fetch_homepage_data(){
    try {
        const response = await axiosInstance.get(HOMEPAGE_DATA_ENDPOINT);
        if (response.status === 200) {
            console.log("Homepage data fetched successfully:", response.data);
            return response.data;
        } else {
            throw new Error("Failed to fetch homepage data");
        }
    }
    catch (error) {
        console.error("Error fetching homepage data:", error);
        throw error;
    }
}
