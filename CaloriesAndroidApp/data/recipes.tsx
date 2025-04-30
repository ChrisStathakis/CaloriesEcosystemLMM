import { get } from "react-native/Libraries/TurboModule/TurboModuleRegistry";
import createGraphQLClient from "./axiosInstance";
import { GRAPHQL_ENDPOINT } from "./endpoints";
import AsyncStorage from "@react-native-async-storage/async-storage";


async function getToken() {
    try {
        const token = await AsyncStorage.getItem("token");
        return token;
    } catch (error) {
        console.error("Error fetching token from AsyncStorage:", error);
        return null;
    }
}

const graphQLClient  = createGraphQLClient(GRAPHQL_ENDPOINT, {
    token: getToken(),
    headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${getToken()}`,
    },

    axiosConfig: {
        timeout: 10000,
    },
});


const GET_RECIPES = ` 
   query {
    allRecipes {
   	    title
        calories
        protein
        fats
        carbs
  }
}
`

async function fetchRecipes(){
    try {
        const response = await graphQLClient.query(GET_RECIPES, {limit: 30})
        console.log("try response", response)
        return response.data
    } catch (error) {
        console.error("Error fetching recipes:", error);
        throw error;
    }
}

export {
    fetchRecipes,
}