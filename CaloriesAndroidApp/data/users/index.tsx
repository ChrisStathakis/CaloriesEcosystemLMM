
import { IS_AUTHENTICATED, IS_AUTHENTICATED_FALSE, ACCESS_TOKEN, REFRESH_TOKEN, IS_AUTHENTICATED_TRUE } from '../actionTypes'
import { LOGIN_ENDPOINT, API_URL } from "../endpoints";
import  Storage from "../myStorage"
import axios from "axios";


const axiosInstance = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },  
})


export const saveAuthToken = async (token: string) => {
  try {
    await Storage.setItem('access_token', token);
  } catch (error) {
    console.error('Error saving access token:', error);
  }
}   


export const fetchAuthToken = async (data: {username: string, password: string}) => {
  const endpoint = LOGIN_ENDPOINT;
  console.log("endpoint", endpoint, data);

  axiosInstance.post(endpoint, data)
    .then((response) => {
      console.log("response", response);
      if (response.status === 200) {
        const access_token = response.data.access;
        const refresh_token = response.data.refresh;
        Storage.setItem(IS_AUTHENTICATED, IS_AUTHENTICATED_TRUE);
        Storage.setItem(ACCESS_TOKEN, access_token);
        Storage.setItem(REFRESH_TOKEN, refresh_token);
        return response.data;
      } else {
        Storage.setItem(IS_AUTHENTICATED, IS_AUTHENTICATED_FALSE);
        console.error('Error fetching access token:', response.statusText);
        return null;
    }})

}

  

export const checkIfAuthenticated = async () => {
  try {
    const token = await Storage.getItem(IS_AUTHENTICATED);
    if (token === null) {
      Storage.setItem(IS_AUTHENTICATED, IS_AUTHENTICATED_FALSE);
      return false;
    }
    return token;
  } catch (error) {
    await Storage.setItem(IS_AUTHENTICATED, IS_AUTHENTICATED_FALSE);
    console.error('Error checking authentication:', error);
    return false;
  }

}


export const fetch_profile = async () => {

}