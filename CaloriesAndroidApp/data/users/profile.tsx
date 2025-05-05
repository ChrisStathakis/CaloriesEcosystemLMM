import axiosInstance from "../axiosInstanceHTTP";

import Storage from "../myStorage";
import  { PROFILE_ENDPOINT } from '../endpoints';
import { PROFILE_ID } from "../actionTypes";


export async function fetch_profile(){
    try {
        const resposse = await axiosInstance.get(PROFILE_ENDPOINT);
        if (resposse.status === 200) {
            return resposse.data;
            Storage.setItem(PROFILE_ID, resposse.data.id.toString());
        } else {
            throw new Error("Failed to fetch profile data");
        }
    }
    catch (error) {
        console.error("Error fetching profile data:", error);
        throw error;
    }
    

}